# step2.py
# pass this script to FontForge to build the intermediate UFO sources for each style
# arguments: master source file (sfd format)

# Copyright 2022 Brad Neil
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import sys
import fontforge
import plistlib

DOT_SIZE = 100
GLYPH_WIDTH = 8
GLYPH_HEIGHT = 12
DESCENT_DOTS = 2
LEFT_SIDE_BEARING = 50
font = fontforge.open(sys.argv[1])

unlink_list = ["Aring", "Ccedilla", "aring", "ccedilla", "aogonek", "dcaron", 
	"Eogonek", "eogonek", "uni0122", "Iogonek", "iogonek", "uni013B", "uni013C",
	"lcaron", "Scedilla", "scedilla", "uni0162", "uni0163", "Uogonek", "uni0218",
	"uni0219", "uni021A", "uni021B"]

def add_names(style):
	font.fontname = font.fontname + style + "-Regular"
	font.appendSFNTName("English (US)", 16, font.familyname)
	font.familyname = font.familyname + " " + style
	font.fullname = font.familyname
	font.appendSFNTName("English (US)", 17, style)
	font.appendSFNTName("English (US)", 21, font.familyname)
	font.appendSFNTName("English (US)", 22, "Regular")


#######################################
# Regular style
font["dot"].unlinkThisGlyph()
font["dot"].clear()
for glyph in unlink_list:
	font[glyph].unlinkRef() # prevent rendering issues with just-touching components
font.selection.all()
font.removeOverlap()
font.simplify()
font.round(0.1) # hack: the "dot" glyph is deliberately 1 unit too large so that simplify() produces nicer outlines; this reverses that
font.fontname = font.fontname + "-Regular"
font.save("MatrixSans-Regular.sfd")

#######################################
# Screen style
font = fontforge.open(sys.argv[1])

font.selection.select("dot")
font.round(0.1)
font["dot"].transform((0.88, 0.0, 0.0, 0.88, 6.0, 6.0))
font["dot"].unlinkThisGlyph()
font["dot"].clear()
add_names("Screen")
font.save("MatrixSans-Screen.sfd")

#######################################
# Print style
font = fontforge.open(sys.argv[1])

font["dot"].clear()
circle = fontforge.unitShape(0) # creates a unit circle
circle.draw(font["dot"].glyphPen()) # draws the circle into the glyph, replacing previous outlines
font["dot"].transform((48.0, 0.0, 0.0, 48.0, 50.0, 50.0))
font["dot"].round()
font["dot"].width = 100
font["dot"].unlinkThisGlyph()
font["dot"].clear()
add_names("Print")
font.save("MatrixSans-Print.sfd")

#######################################
# Video style

video_fix = {"four", "N", "R", "b", "d", "g", "p", "q", "z", "AE", "thorn", "Lslash", "uni2074", "radical", "Eng.loclNSM", "uni1E9E"}
unlink_list += ["Aogonek", "uogonek"]

font = fontforge.open(sys.argv[1])

font.createChar(-1, "halfdot")
pen = font["halfdot"].glyphPen()
pen.moveTo(0,0)
pen.lineTo(0,DOT_SIZE // 2 + 1)
pen.lineTo(DOT_SIZE // 2 + 1, DOT_SIZE // 2 + 1)
pen.lineTo(DOT_SIZE // 2 + 1, 0)
pen.closePath()
pen = None

patterns = [
	[[15, 15, -1],
	[0, 15, -1],
	[0, 8, 15], 
	(0.5, 1.0)], # x offset, y offset
	[[0, 2, 15],
	[0, 15, -1],
	[15, 15, -1],
	(0.5, 1.5)],
	[[-1, 15, 15],
	[-1, 15, 0],
	[15, 4, 0],
	(2.0, 1.0)],
	[[15, 1, 0],
	[-1, 15, 0],
	[-1, 15, 15],
	(2.0, 1.5)],
	[[0, 0, 15],
	[2, 15, 15],
	[15, -1, -1],
	(1.5, 0.5)],
	[[15, -1, -1],
	[8, 15, 15],
	[0, 0, 15],
	(1.5, 2.0)],
	[[15, 0, 0],
	[15, 15, 1],
	[-1, -1, 15],
	(1.0, 0.5)],
	[[-1, -1, 15],
	[15, 15, 4],
	[15, 0, 0],
	(1.0, 2.0)]]

for glyph in font:

	# determine where the dots are in each glyph
	matrix = [[False]*GLYPH_HEIGHT for _ in range(GLYPH_WIDTH)] # full dots
	matrix2 = [[0]*GLYPH_HEIGHT for _ in range(GLYPH_WIDTH)] # occupied quadrants
	skip = False
	for ref, trans in font[glyph].references:
		if ref != "dot":
			skip = True
			break # we are only interested in glyphs that directly reference the "dot" glyph
		x = int(trans[4]) # coordinates of glyph reference
		y = int(trans[5])
		x //= DOT_SIZE
		y = y // DOT_SIZE + DESCENT_DOTS
		matrix[x][y] = True
		matrix2[x][y] = 15
	if skip:
		continue

	# basic interpolation, Mullard SAA5050 style
	for x in range(GLYPH_WIDTH - 1):
		for y in range(GLYPH_HEIGHT - 1):
			if matrix[x][y] and matrix[x + 1][y + 1] and not (matrix[x + 1][y] or matrix[x][y + 1]):
				font[glyph].addReference("halfdot", (1, 0, 0, 1, x * DOT_SIZE + DOT_SIZE // 2 + LEFT_SIDE_BEARING, (y - DESCENT_DOTS + 1) * DOT_SIZE))
				font[glyph].addReference("halfdot", (1, 0, 0, 1, (x + 1) * DOT_SIZE + LEFT_SIDE_BEARING, (y - DESCENT_DOTS) * DOT_SIZE + DOT_SIZE // 2))
				matrix2[x][y + 1] = 8 # bottom right quarter-dot
				matrix2[x + 1][y] = 1 # top left
			if matrix[x][y + 1] and matrix[x + 1][y] and not (matrix[x][y] or matrix[x + 1][y + 1]):
				font[glyph].addReference("halfdot", (1, 0, 0, 1, x * DOT_SIZE + DOT_SIZE // 2 + LEFT_SIDE_BEARING, (y - DESCENT_DOTS) * DOT_SIZE + DOT_SIZE // 2))
				font[glyph].addReference("halfdot", (1, 0, 0, 1, (x + 1) * DOT_SIZE + LEFT_SIDE_BEARING, (y - DESCENT_DOTS + 1) * DOT_SIZE))
				matrix2[x][y] = 2 # top right
				matrix2[x + 1][y + 1] = 4 # bottom right

	if str(glyph) in video_fix:
		# more complicated interpolation, to fix ugly spots left by the basic method
		for i in range(GLYPH_WIDTH - 2):
			for j in range(GLYPH_HEIGHT - 2):
				for pattern in patterns:
					skip = False
					for a in range(3):
						for b in range(3):
							if pattern[b][a] >= 0 and pattern[b][a] != matrix2[i + a][j + b]:
								skip = True
								break
						if skip:
							break
					if skip:
						continue
					# we found a matching pattern: need to add half-dot
					x, y, = pattern[3]
					font[glyph].addReference("halfdot", (1, 0, 0, 1, (i + x) * DOT_SIZE + LEFT_SIDE_BEARING, (j + y - DESCENT_DOTS) * DOT_SIZE))

# hack for the counters in ae, oe
refs = []
for refname, trans in font["ae"].references:
	if refname == "halfdot":
		if trans[4] == 150 or trans[4] == 200 and trans[5] == 100 or trans[4] >= 350 and trans[5] == 350:
			continue
	refs.append((refname, trans))
font["ae"].references = tuple(refs)

refs = []
for refname, trans in font["oe"].references:
	if refname == "halfdot":
		if trans[4] >= 350 and trans[5] == 350:
			continue
	refs.append((refname, trans))
font["oe"].references = tuple(refs)

refs = []
for refname, trans in font["registered"].references:
	if refname == "halfdot":
		if (trans[4] == 200 or trans[4] == 250 or trans[4] == 600 or trans[4] == 650) and (trans[5] >= 50 and trans[5] <= 500):
			continue
	refs.append((refname, trans))
font["registered"].references = tuple(refs)

font["Lslash"].addReference("halfdot", (1, 0, 0, 1, 100, 300))
font["lslash"].addReference("halfdot", (1, 0, 0, 1, 100, 300))
font["lslash"].addReference("halfdot", (1, 0, 0, 1, 250, 350))
font["Aogonek"].addReference("halfdot", (1, 0, 0, 1, 400, 0))
font["Aogonek"].addReference("halfdot", (1, 0, 0, 1, 450, -50))
font["uogonek"].addReference("halfdot", (1, 0, 0, 1, 400, 0))
font["uogonek"].addReference("halfdot", (1, 0, 0, 1, 450, -50))
font["uni2113"].addReference("halfdot", (1, 0, 0, 1, 250, 250))
font["paragraph"].addReference("halfdot", (1, 0, 0, 1, 100, 350))
font["paragraph"].addReference("halfdot", (1, 0, 0, 1, 100, 600))
font["one"].addReference("halfdot", (1, 0, 0, 1, 100, 600))

# interpolation done, now finish it off the same as Regular style
font["dot"].unlinkThisGlyph()
font["halfdot"].unlinkThisGlyph()
font["dot"].clear()
font["halfdot"].clear()

# hack to preserve the counter of the ring diacritic
font["ring"].unlinkRef()
font["ring"].removeOverlap()
font["ring"].addReference("period", (1, 0, 0, 1, 100, 600))
font["ring"].unlinkRef()
font["ring"].correctDirection()

for glyph in unlink_list:
	font[glyph].unlinkRef() # prevent rendering issues with just-touching components
font.selection.all()
font.removeOverlap()
font.simplify()
font.round(0.1)

add_names("Video")
font.save("MatrixSans-Video.sfd")

#######################################
# Raster style
font = fontforge.open(sys.argv[1])

font["dot"].clear()
pen = font["dot"].glyphPen()
pen.moveTo((-10, 50))
pen.curveTo((-10, 72), (8, 90), (30, 90))
pen.lineTo((70, 90))
pen.curveTo((92, 90), (110, 72), (110, 50))
pen.curveTo((110, 28), (92, 10), (70, 10))
pen.lineTo(30, 10)
pen.curveTo((8, 10), (-10, 28), (-10, 50))
pen.closePath()
font["dot"].width = 100

font.createChar(-1, "dot2") # overlaps with dot to the right
pen = font["dot2"].glyphPen()
pen.moveTo((69, 90))
pen.lineTo((151, 90))
pen.lineTo((151, 10))
pen.lineTo((69, 10))
pen.closePath()
font["dot2"].width = 100

for glyph in font:
	# determine where the dots are in each glyph
	matrix = [[False]*GLYPH_HEIGHT for _ in range(GLYPH_WIDTH)]
	skip = False
	for ref, trans in font[glyph].references:
		if ref != "dot":
			skip = True
			break # we are only interested in glyphs that directly reference the "dot" glyph
		x = int(trans[4]) # coordinates of glyph reference
		y = int(trans[5])
		x //= DOT_SIZE
		y = y // DOT_SIZE + DESCENT_DOTS
		matrix[x][y] = True
	if skip:
		continue

	for j in range(GLYPH_HEIGHT):
		for i in range(GLYPH_WIDTH - 1):
			if matrix[i][j] and matrix[i + 1][j]:
				font[glyph].addReference("dot2", (1, 0, 0, 1, i * DOT_SIZE + LEFT_SIDE_BEARING, (j - DESCENT_DOTS) * DOT_SIZE))

font["dot"].unlinkThisGlyph()
font["dot"].clear()
font["dot2"].unlinkThisGlyph()
font["dot2"].clear()
font.selection.all()
font.removeOverlap()
font.simplify()
add_names("Raster")
font.save("MatrixSans-Raster.sfd")


# glyph.user_decomp
# glyph.build()