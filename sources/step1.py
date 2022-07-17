# step1.py
# pass this script to FontForge to create a temporary font with glyphs built from references
# arguments: source image (pbm format); table of codepoints/glyphs names (csv format); output filename

# Copyright 2022 Brad Neil
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import sys
import fontforge

em_size = 1000
headroom = 3 # no. of dots above cap height in source image
dot_size = 100

def get_pbm_int(pbm_file):
	result = ""
	while True:
		c = pbm_file.read(1)
		if c == "#":
			pbm_file.readline()
		elif c.isspace():
			if result != "":
				return int(result)
		else:
			result += c
	

def main():

	# read source image (PBM)
	with open(sys.argv[1]) as pbm_file:
		if pbm_file.read(2) != "P1":
			raise Exception(f"Source image {sys.argv[0]} is incorrect format or corrupted")
		image_width = get_pbm_int(pbm_file)
		image_height = get_pbm_int(pbm_file)
		source_image = []
		for j in range(image_height):
			source_image.append([])
			for i in range(image_width):
				source_image[-1].append(get_pbm_int(pbm_file))
	
	# read glyph map (CSV)
	with open(sys.argv[2]) as csv_file:
		glyph_map = []
		for line in csv_file:
			glyph_map.append(line.strip().split(","))
	
		glyph_map_width = max([len(x) for x in glyph_map])
		glyph_map_height = len(glyph_map)
		glyph_width = image_width // glyph_map_width
		glyph_height = image_height // glyph_map_height

	# initialise font
	font = fontforge.font()
	font.encoding = "UnicodeFull"
	font.em = em_size

	# make "dot" glyph
	font.createChar(-1, "dot")
	pen = font["dot"].glyphPen()
	pen.moveTo(0,0)
	pen.lineTo(0,dot_size + 1) # make the dots overlap by 1 unit so FontForge produces nicer outlines later
	pen.lineTo(dot_size + 1, dot_size + 1)
	pen.lineTo(dot_size + 1, 0)
	pen.closePath()
	pen = None

	# make glyphs
	for j in range(len(glyph_map)):
		for i in range(len(glyph_map[j])):
			name = glyph_map[j][i]
			if name.startswith("0x"):
				codepoint = int(name, 16)
				if codepoint == 0:
					continue
				else:
					font.createChar(codepoint)
					name = font[codepoint].glyphname
			else:
				font.createChar(-1, name)
					
			for y in range(glyph_height):
				for x in range(glyph_width):
					if source_image[j*glyph_height + y][i*glyph_width + x]:
						font[name].addReference("dot", (1, 0, 0, 1, x * dot_size, (glyph_height - y - headroom) * dot_size))

			font[name].width = glyph_width * dot_size

	# finished step 1!
	font.save(sys.argv[3])


if __name__ == "__main__":
	main()