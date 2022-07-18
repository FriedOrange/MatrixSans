# step2.py
# pass this script to FontForge to build the intermediate UFO sources for each style
# arguments: master source file (sfd format)

# Copyright 2022 Brad Neil
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import sys
from turtle import dot
import fontforge

dot_size = 100
glyph_width = 8
glyph_height = 12
descent_dots = 2
left_side_bearing = 50
font = fontforge.open(sys.argv[1])

# Regular style
font["dot"].unlinkThisGlyph()
font["dot"].clear()
font.selection.all()
font.removeOverlap()
font.simplify()
font.round(0.1) # hack: the "dot" glyph is deliberately 1 unit too large so that simplify() produces nicer outlines; this reverses that
font.generate("LibreDotMatrix-Regular.ufo")

# Screen style
font.revert()
font.selection.select("dot")
font.round(0.1)
font["dot"].transform((0.8, 0.0, 0.0, 0.8, 10.0, 10.0))
font.fontname = "LibreDotMatrixScreen"
font.familyname = "Libre Dot Matrix Screen"
font.fullname = "Libre Dot Matrix Screen"
font.generate("LibreDotMatrixScreen-Regular.ufo")

# Print style
font["dot"].clear()
circle = fontforge.unitShape(0) # creates a unit circle
circle.draw(font["dot"].glyphPen()) # draws the circle into the glyph, replacing previous outlines
font["dot"].transform((45.0, 0.0, 0.0, 45.0, 50.0, 50.0))
font["dot"].round()
font["dot"].width = 100
font.fontname = "LibreDotMatrixPrint"
font.familyname = "Libre Dot Matrix Print"
font.fullname = "Libre Dot Matrix Print"
font.generate("LibreDotMatrixPrint-Regular.ufo")

# Video style
font.revert()

font.createChar(-1, "halfdot")
pen = font["halfdot"].glyphPen()
pen.moveTo(0,0)
pen.lineTo(0,dot_size // 2 + 1)
pen.lineTo(dot_size // 2 + 1, dot_size // 2 + 1)
pen.lineTo(dot_size // 2 + 1, 0)
pen.closePath()
pen = None

for glyph in font:
	matrix = [[False]*glyph_height for _ in range(glyph_width)]
	skip = False
	for ref, trans in font[glyph].references:
		if ref != "dot":
			skip = True
			break # we are only interested in glyphs that directly reference the "dot" glyph
		x = int(trans[4]) # coordinates of glyph reference
		y = int(trans[5])
		x //= dot_size
		y = y // dot_size + descent_dots
		matrix[x][y] = True
	if skip:
		continue
	for x in range(glyph_width - 1):
		for y in range(glyph_height - 1):
			if matrix[x][y] and matrix[x + 1][y + 1] and not (matrix[x + 1][y] or matrix[x][y + 1]):
				font[glyph].addReference("halfdot", (1, 0, 0, 1, x * dot_size + dot_size // 2 + left_side_bearing, (y - descent_dots + 1) * dot_size))
				font[glyph].addReference("halfdot", (1, 0, 0, 1, (x + 1) * dot_size + left_side_bearing, (y - descent_dots) * dot_size + dot_size // 2))
			if matrix[x][y + 1] and matrix[x + 1][y] and not (matrix[x][y] or matrix[x + 1][y + 1]):
				font[glyph].addReference("halfdot", (1, 0, 0, 1, x * dot_size + dot_size // 2 + left_side_bearing, (y - descent_dots) * dot_size + dot_size // 2))
				font[glyph].addReference("halfdot", (1, 0, 0, 1, (x + 1) * dot_size + left_side_bearing, (y - descent_dots + 1) * dot_size))

font["dot"].unlinkThisGlyph()
font["halfdot"].unlinkThisGlyph()
font["dot"].clear()
font["halfdot"].clear()
font.selection.all()
font.removeOverlap()
font.simplify()
font.round(0.1)

font.fontname = "LibreDotMatrixVideo"
font.familyname = "Libre Dot Matrix Video"
font.fullname = "Libre Dot Matrix Video"
font.generate("LibreDotMatrixVideo-Regular.ufo")
# glyph.user_decomp
# glyph.build()