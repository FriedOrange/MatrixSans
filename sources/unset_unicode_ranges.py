
def checksum(data: bytes) -> int:
	"""
	Calculates the OpenType font table checksum. len(data) must be a multiple of 4.
	"""
	result = 0
	for i in range(0, len(data), 4):
		result += int.from_bytes(data[i:i + 4])
		result %= 1 << 32
	return result

def remap_bit(bit):
	q, r = divmod(bit, 32)
	return (3 - q) * 32 + r

def main():
	from argparse import ArgumentParser
	from functools import reduce

	parser = ArgumentParser(
				description = "Unsets the specified bits in the Unicode Ranges field of the OS/2 table in an OpenType font, to prevent Windows from showing non-representative characters in the file's thumbnail.",
				epilog="See https://learn.microsoft.com/en-us/typography/opentype/spec/os2#ur for details of Unicode ranges specified by each bit.")
	parser.add_argument("input_file", nargs = 1)
	parser.add_argument("output_file", nargs = 1)
	parser.add_argument("bits", type = int,  choices = range(128), nargs = "+", metavar = "bit")
	args = parser.parse_args()

	# remap requested bits, since the Unicode ranges are in 4x32-bit units, 
	#   where each unit is big-endian but the 4 units are stored in little-endian order
	bits = list(map(remap_bit, args.bits))
	bitmask = (2**128 - 1) ^ reduce(lambda mask, b: mask | 2**b , bits, 0)

	with open(args.input_file[0], "rb") as input_file:
		input_font = input_file.read()

	if int.from_bytes(input_font[:4]) not in (0x00010000, 0x4F54544F):
		raise ValueError("Input file is incorrect type or corrupt")

	# search for OS/2 table entry in tableRecords, get table checksum and Unicode ranges field
	numTables = int.from_bytes(input_font[4:6])
	lo = 0
	hi = numTables
	os2tag = int.from_bytes(b"OS/2")
	while lo < hi:
		mid = (lo + hi) // 2
		table_entry_offset = 12 + mid * 16 # offset of tableRecords = 12, size of TableRecord = 16
		tableTag = int.from_bytes(input_font[table_entry_offset:table_entry_offset + 4])
		if tableTag < os2tag:
			lo = mid + 1
		elif tableTag > os2tag:
			hi = mid
		else:
			os2_checksum_offset = table_entry_offset + 4
			old_checksum = int.from_bytes(input_font[os2_checksum_offset: os2_checksum_offset + 4])
			os2_table_offset = int.from_bytes(input_font[table_entry_offset + 8: table_entry_offset + 12])
			os2_ur_offset = os2_table_offset + 42
			break
	else:
		raise ValueError("Input file is incorrect type or corrupt")

	# unset specified bits from unicode ranges field
	old_unicode_ranges = int.from_bytes(input_font[os2_ur_offset:os2_ur_offset + 16])
	new_unicode_ranges = old_unicode_ranges & bitmask

	# calculate new checksum for OS/2 table
	# unicode ranges field is not uint32-aligned, so pad with zeroes to get correct checksum
	checksum_delta = checksum(b"\0\0" + new_unicode_ranges.to_bytes(16) + b"\0\0") - checksum(b"\0\0"+ old_unicode_ranges.to_bytes(16) + b"\0\0")
	new_checksum = (old_checksum + checksum_delta) % (1 << 32)

	with open(args.output_file[0], "wb") as output_file:
		output_file.write(input_font[:os2_checksum_offset])
		output_file.write(new_checksum.to_bytes(4))
		output_file.write(input_font[os2_checksum_offset + 4: os2_ur_offset])
		output_file.write(new_unicode_ranges.to_bytes(16))
		output_file.write(input_font[os2_ur_offset + 16:])


if __name__ == "__main__":
	main()