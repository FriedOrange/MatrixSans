# step2.py
# pass this script to FontForge to build the intermediate UFO sources for each style

# Copyright 2024 Brad Neil
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import fontforge

DOT_SIZE = 100
GLYPH_WIDTH = 12
GLYPH_HEIGHT = 12
DESCENT_DOTS = 2
LEFT_SIDE_BEARING = 50
SCREEN_DOT_FACTOR = 0.86
PRINT_DOT_RADIUS = 48.0
MAIN_SOURCE = "MatrixSans-MASTER.sfd"
HALFSTEP_SOURCE = "source\\Quantum-MASTER-halfstep.sfd"
BOLD_AUX_SOURCE = "source\\Quantum-MASTER-bold-aux.sfd"
VIDEO_AUX_SOURCE = "MatrixSans-MASTER-video-aux.sfd"
BOLD_TEMP = "source\\temp\\temp bold.sfd"
EXTENDED_TEMP = "source\\temp\\temp extended.sfd"
UNLINK_LIST = ["Aring", "Ccedilla", "aring", "ccedilla", "aogonek",
	"Eogonek", "eogonek", "Gcommaaccent", "Iogonek", "iogonek", "Lcommaaccent", "lcommaaccent",
	"Scedilla", "scedilla", "Tcedilla", "tcedilla", "Uogonek", "Scommaaccent",
	"scommaaccent", "Tcommaaccent", "tcommaaccent", "aring.sc", "eogonek.sc", "gcommaaccent.sc",
	"iogonek.sc", "lcommaaccent.sc", "tcedilla.sc", "tcommaaccent.sc", "uogonek.sc", "Ohorn", "ohorn", "Uhorn", "uhorn.sc", "Aringacute", "aringacute", "Abrevetilde", "abrevetilde"]

def add_names(font, style, suffix=""):
	font.fontname = font.fontname + style + suffix + f"-{font.weight}"
	# font.appendSFNTName("English (US)", 16, font.familyname)
	font.familyname = font.familyname + " " + style + (" " + suffix if suffix else "")
	font.fullname = font.familyname + (" " + font.weight if font.weight != "Regular" else "")
	# font.appendSFNTName("English (US)", 17, style)
	# font.appendSFNTName("English (US)", 21, font.familyname)
	# font.appendSFNTName("English (US)", 22, "Regular")

def get_pattern(font, glyph):
	matrix = [[False]*GLYPH_HEIGHT for _ in range(GLYPH_WIDTH)] # full dots
	if len(font[glyph].references) == 0:
		return matrix, True
	else:
		skip = False
	# for ref, trans, _ in font[glyph].references:
	for ref, trans, _ in font[glyph].references:
		if ref != "dot":
			skip = True
			break # we are only interested in glyphs that directly reference the "dot" glyph
		x = int(trans[4]) # coordinates of glyph reference
		y = int(trans[5])
		x //= DOT_SIZE
		y = y // DOT_SIZE + DESCENT_DOTS
		matrix[x][y] = True
	return matrix, skip

def segmented_panose(panose):
	new_panose = list(panose)
	new_panose[-2] = 4
	new_panose = tuple(new_panose)
	return new_panose

def clear_dots(font):
	for glyph in ["dot", "printdot", "screendot", "rasterdot", "rasterdot2", "quarterdot", "concaveTR", "concaveTL", "convexTR", "convexTL", "midTR", "midTL", "chamferTR", "chamferTL", "concaveBR", "concaveBL", "convexBR", "convexBL", "midBR", "midBL", "chamferBR", "chamferBL"]:
		font[glyph].unlinkThisGlyph()
		font[glyph].clear()

def make_regular(source):
	font = fontforge.open(source)
	clear_dots(font)
	for glyph in UNLINK_LIST:
		font[glyph].unlinkRef() # prevent rendering issues with just-touching components
	font.selection.all()
	font.removeOverlap()
	font.round()
	font.simplify()
	font.round(0.1) # hack: the "dot" glyph is deliberately 1 unit too large so that simplify() produces nicer outlines; this reverses that
	font.fontname = font.fontname + f"-{font.weight}"
	font.save(f"temp\\MatrixSans-{font.weight}.sfd")

def make_screen(source):
	font = fontforge.open(source)
	font.selection.select("screendot")
	font.copy()
	font.selection.select("dot")
	font.paste()
	clear_dots(font)
	add_names(font, "Screen")
	font.uwidth = int(SCREEN_DOT_FACTOR * DOT_SIZE)
	font.os2_strikeysize = int(SCREEN_DOT_FACTOR * DOT_SIZE)
	font.os2_strikeypos += int((DOT_SIZE - font.os2_strikeysize) / 2)
	font.os2_panose = segmented_panose(font.os2_panose)
	font.save(f"temp\\MatrixSansScreen-{font.weight}.sfd")

def make_print(source, name_suffix=""):
	font = fontforge.open(source)
	font.selection.select("printdot")
	font.copy()
	font.selection.select("dot")
	font.paste()
	clear_dots(font)
	add_names(font, "Print", name_suffix)
	font.uwidth = int(PRINT_DOT_RADIUS * 10/6)
	font.os2_strikeysize = int(PRINT_DOT_RADIUS * 10/6)
	font.os2_strikeypos += int((DOT_SIZE - font.os2_strikeysize) / 2)
	font.os2_panose = segmented_panose(font.os2_panose)
	font.save("temp\\MatrixSansPrint" + name_suffix + f"-{font.weight}.sfd")

def make_video(source):
	font = fontforge.open(source)

	UNLINK_LIST.append("Aogonek")
	UNLINK_LIST.append("uogonek")
	UNLINK_LIST.append("aogonek.sc")

	video_aux_font = fontforge.open(VIDEO_AUX_SOURCE)

	for glyph in font:

		# determine where the dots are in each glyph
		matrix, skip = get_pattern(font, glyph)
		if skip:
			continue

		# basic interpolation, Mullard SAA5050 style
		for x in range(GLYPH_WIDTH - 1):
			for y in range(GLYPH_HEIGHT - 1):
				if matrix[x][y] and matrix[x + 1][y + 1] and not (matrix[x + 1][y] or matrix[x][y + 1]):
					font[glyph].addReference("quarterdot", (1, 0, 0, 1, x * DOT_SIZE + DOT_SIZE // 2 + LEFT_SIDE_BEARING, (y - DESCENT_DOTS + 1) * DOT_SIZE))
					font[glyph].addReference("quarterdot", (1, 0, 0, 1, (x + 1) * DOT_SIZE + LEFT_SIDE_BEARING, (y - DESCENT_DOTS) * DOT_SIZE + DOT_SIZE // 2))
				if matrix[x][y + 1] and matrix[x + 1][y] and not (matrix[x][y] or matrix[x + 1][y + 1]):
					font[glyph].addReference("quarterdot", (1, 0, 0, 1, x * DOT_SIZE + DOT_SIZE // 2 + LEFT_SIDE_BEARING, (y - DESCENT_DOTS) * DOT_SIZE + DOT_SIZE // 2))
					font[glyph].addReference("quarterdot", (1, 0, 0, 1, (x + 1) * DOT_SIZE + LEFT_SIDE_BEARING, (y - DESCENT_DOTS + 1) * DOT_SIZE))

	for glyph in video_aux_font:
		video_aux_font.selection.select(glyph)
		video_aux_font.copy()
		font.selection.select(glyph)
		font.paste()

	# interpolation done, now finish it off the same as Regular style
	clear_dots(font)

	for glyph in UNLINK_LIST:
		font[glyph].unlinkRef() # prevent rendering issues with just-touching components
	font.selection.all()
	font.removeOverlap()
	font.round()
	font.simplify()
	font.round(0.1)

	add_names(font, "Video")
	font.save(f"temp\\MatrixSansVideo-{font.weight}.sfd")

def make_raster(source):
	font = fontforge.open(source)

	font.selection.select("rasterdot")
	font.copy()
	font.selection.select("dot")
	font.paste()

	for glyph in font:

		# determine where the dots are in each glyph
		matrix, skip = get_pattern(font, glyph)
		if skip:
			continue

		for j in range(GLYPH_HEIGHT):
			for i in range(GLYPH_WIDTH - 1):
				if matrix[i][j] and matrix[i + 1][j]:
					if glyph == "underscore" or glyph == "emdash":
						font[glyph].addReference("rasterdot2", (1, 0, 0, 1, i * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))
					else:
						font[glyph].addReference("rasterdot2", (1, 0, 0, 1, i * DOT_SIZE + LEFT_SIDE_BEARING, (j - DESCENT_DOTS) * DOT_SIZE))

	clear_dots(font)
	font.selection.all()
	font.removeOverlap()
	font.simplify()
	add_names(font, "Raster")
	font.uwidth = 80
	font.os2_strikeysize = 80
	font.os2_strikeypos += int((DOT_SIZE - font.os2_strikeysize) / 2)
	font.os2_panose = segmented_panose(font.os2_panose)
	font.save(f"temp\\MatrixSansRaster-{font.weight}.sfd")

def make_bold(source):
	font = fontforge.open(source)
	bold_aux_font = fontforge.open(BOLD_AUX_SOURCE)

	for glyph in font:
	
		# determine where the dots are in each glyph
		matrix, skip = get_pattern(font, glyph)
		if skip:
			continue

		for j in range(GLYPH_HEIGHT):
			for i in range(GLYPH_WIDTH - 1):
				if matrix[i][j] and not matrix[i + 1][j]:
					font[glyph].addReference("dot", (1, 0, 0, 1, (i + 1) * DOT_SIZE + LEFT_SIDE_BEARING, (j - DESCENT_DOTS) * DOT_SIZE))

		if font[glyph].right_side_bearing <= 0:
			font[glyph].right_side_bearing = LEFT_SIDE_BEARING - 1

	for glyph in bold_aux_font:
		bold_aux_font.selection.select(glyph)
		bold_aux_font.copy()
		font.selection.select(glyph)
		font.paste()

	font.weight = "Bold"
	font.os2_weight = 700
	font.save(BOLD_TEMP)

def make_extended(source):
	font = fontforge.open(source)

	for glyph in font:

		width = font[glyph].width
		font[glyph].width = width * 2

		# determine where the dots are in each glyph
		matrix = [[False]*GLYPH_HEIGHT for _ in range(GLYPH_WIDTH*2)] # full dots
		skip = False
		for ref, trans in font[glyph].references:
			if ref != "dot":
				skip = True
				break # we are only interested in glyphs that directly reference the "dot" glyph
			x = int(trans[4]) # coordinates of glyph reference
			y = int(trans[5])
			x //= DOT_SIZE // 2
			y = y // DOT_SIZE + DESCENT_DOTS
			matrix[x][y] = True
		if skip or not font[glyph].references:
			continue

		font[glyph].references = ()

		for j in range(GLYPH_HEIGHT):
			for i in range(GLYPH_WIDTH * 2):
				if matrix[i][j]:
					font[glyph].addReference("dot", (1, 0, 0, 1, i * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))
					font[glyph].addReference("dot", (1, 0, 0, 1, (i + 1) * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))

	font.weight = "Bold"
	font.os2_weight = 700
	font.save(EXTENDED_TEMP)

def make_smooth(source):

	def refs_to_dots(source, x, y, destination):
		for ref, trans, _ in font[source].references:
			x2 = x + trans[4]
			y2 = y + trans[5]
			if ref == "dot":
				font[destination].addReference("dot", (1, 0, 0, 1, x2, y2))
			else:
				refs_to_dots(ref, x2, y2, destination)

	font = fontforge.open(source)

	# make glyphs with diagonally-touching components directly reference "dot"
	font.createChar(-1, "temp")
	for glyph in ["Aogonek", "aogonek.sc"]:
		font["temp"].clear()
		refs_to_dots(glyph, 0, 0, "temp")
		font.selection.select("temp")
		font.copy()
		font.selection.select(glyph)
		font.paste()
	font["temp"].clear()

	# cell connection (neighbour) criteria, mask, component reference by cell quadrant
	topright = [
		(0b00010000, 0b11111000, "convexTR"),
		(0b00000001, 0b11110011, "chamferTR"),
		(0b01000000, 0b11100000, "midTR"),
		(0b10010000, 0b10111000, "concaveTR"),
	]
	bottomleft = [
		(0b00000001, 0b10001111, "convexBL"),
		(0b00010000, 0b00111110, "chamferBL"),
		(0b00000100, 0b00001110, "midBL"),
		(0b00001001, 0b10001011, "concaveBL"),
	]
	topleft = [
		(0b00000100, 0b10001111, "convexTL"),
		(0b01000000, 0b11100011, "chamferTL"),
		(0b00000001, 0b10000011, "midTL"),
		(0b10000100, 0b10001110, "concaveTL"),
	]
	bottomright = [
		(0b01000000, 0b11111000, "convexBR"),
		(0b00000100, 0b00111110, "chamferBR"),
		(0b00010000, 0b00111000, "midBR"),
		(0b01001000, 0b11101000, "concaveBR"),
	]

	for glyph in font:

		# determine where the dots are in each glyph
		matrix, skip = get_pattern(font, glyph)
		if skip:
			continue # ignore glyphs that don't reference "dot"

		# print(f"Interpolating \"{glyph}\"")
		# for j in range(GLYPH_HEIGHT - 1, -1, -1):
		# 	for i in range(GLYPH_WIDTH):
		# 		print("\u2588" if matrix[i][j] else " ", end="")
		# 	print()

		# remove existing (ordinary) "dot" glyphs
		font[glyph].references = ()

		# determine which directions have a connected (neighbouring) dot
		for j in range(GLYPH_HEIGHT - 1, -1, -1):
			for i in range(GLYPH_WIDTH):
				if not matrix[i][j]:
					continue
				connections = 0
				if j < GLYPH_HEIGHT - 1:
					if matrix[i][j + 1]: 
						connections |= 0b10000000
					if i < GLYPH_WIDTH - 1 and matrix[i + 1][j + 1]: 
						connections |= 0b01000000
				if i < GLYPH_WIDTH - 1:
					if matrix[i + 1][j]: 
						connections |= 0b00100000
					if j > 0 and matrix[i + 1][j - 1]: 
						connections |= 0b00010000
				if j > 0:
					if matrix[i][j - 1]: 
						connections |= 0b00001000
					if i > 0 and matrix[i - 1][j - 1]: 
						connections |= 0b00000100
				if i > 0:
					if matrix[i - 1][j]: 
						connections |= 0b00000010
					if j < GLYPH_HEIGHT - 1 and matrix [i - 1][j + 1]: 
						connections |= 0b00000001

				if glyph == "x":
					print(f"x: {i} y: {j - DESCENT_DOTS}")
					print(f"connections: {connections:08b}")

				# add quarter blocks depending on matrix cell connections
				for criteria, mask, block in topleft:
					if connections & mask == criteria:
						if glyph == "x":
							print(f"block: {block}")
							print(f"mask:        {mask:08b}")
							print(f"criteria:    {criteria:08b}")
						font[glyph].addReference(block, (1, 0, 0, 1, i * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))
						break
				else:
					font[glyph].addReference("quarterdot", (1, 0, 0, 1, i * DOT_SIZE, (j - DESCENT_DOTS + 0.5) * DOT_SIZE))
				for criteria, mask, block in topright:
					if connections & mask == criteria:
						if glyph == "x":
							print(f"block: {block}")
							print(f"mask:        {mask:08b}")
							print(f"criteria:    {criteria:08b}")
						font[glyph].addReference(block, (1, 0, 0, 1, i * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))
						break
				else:
					font[glyph].addReference("quarterdot", (1, 0, 0, 1, (i + 0.5) * DOT_SIZE, (j - DESCENT_DOTS + 0.5) * DOT_SIZE))
				for criteria, mask, block in bottomleft:
					if connections & mask == criteria:
						if glyph == "x":
							print(f"block: {block}")
							print(f"mask:        {mask:08b}")
							print(f"criteria:    {criteria:08b}")
						font[glyph].addReference(block, (1, 0, 0, 1, i * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))
						break
				else:
					font[glyph].addReference("quarterdot", (1, 0, 0, 1, i * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))
				for criteria, mask, block in bottomright:
					if connections & mask == criteria:
						if glyph == "x":
							print(f"block: {block}")
							print(f"mask:        {mask:08b}")
							print(f"criteria:    {criteria:08b}")
						font[glyph].addReference(block, (1, 0, 0, 1, i * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))
						break
				else:
					font[glyph].addReference("quarterdot", (1, 0, 0, 1, (i + 0.5) * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))

	# clear_dots(font)

	# for glyph in UNLINK_LIST:
	# 	font[glyph].unlinkRef() # prevent rendering issues with just-touching components
	# font.selection.all()
	# font.removeOverlap()
	# font.round()
	# font.simplify()

	add_names(font, "Smooth")
	font.save(f"temp\\MatrixSansSmooth-{font.weight}.sfd")

def main():
	# make_regular(MAIN_SOURCE)
	# make_print(MAIN_SOURCE)
	# make_raster(MAIN_SOURCE)
	# make_screen(MAIN_SOURCE)
	# make_video(MAIN_SOURCE)
	make_smooth(MAIN_SOURCE)
	# make_print(HALFSTEP_SOURCE, "Mono")
	# make_extended(HALFSTEP_SOURCE)
	# make_print(EXTENDED_TEMP, "Mono")
	# make_bold(MAIN_SOURCE)
	# make_regular(BOLD_TEMP)
	# make_print(BOLD_TEMP)
	# make_raster(BOLD_TEMP)
	# make_screen(BOLD_TEMP)
	# make_video(BOLD_TEMP)

if __name__ == "__main__":
	main()