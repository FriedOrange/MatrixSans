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
video_fix = {"four", "N", "R", "b", "d", "g", "p", "q", "z", "AE", "thorn", "Lslash", "uni2074", "radical", "Eng", "uni1E9E"}

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
# font.appendSFNTName("English (US)", 17, "Regular")
font.save("LibreDotMatrix-Regular.sfd")
# FontForge doesn't export the fsSelection field of the OS/2 table. We need to add it in ourselves
# with open("LibreDotMatrix-Regular.ufo/fontinfo.plist", "rb") as plist_file:
# 	fontinfo = plistlib.load(plist_file)
# with open("LibreDotMatrix-Regular.ufo/fontinfo.plist", "wb") as plist_file:
# 	fontinfo["openTypeOS2Selection"] = [6, 7, 8]
# 	plistlib.dump(fontinfo, plist_file)

#######################################
# Screen style
font.revert()

font.selection.select("dot")
font.round(0.1)
font["dot"].transform((0.88, 0.0, 0.0, 0.88, 10.0, 10.0))
font["dot"].unlinkThisGlyph()
font["dot"].clear()
font.fontname = "LibreDotMatrixScreen"
font.familyname = "Libre Dot Matrix Screen"
font.fullname = "Libre Dot Matrix Screen"
font.appendSFNTName("English (US)", 17, "Screen")
font.appendSFNTName("English (US)", 21, "Libre Dot Matrix Screen")
font.appendSFNTName("English (US)", 22, "Regular")
font.save("LibreDotMatrix-Screen.sfd")
# with open("LibreDotMatrix-Screen.ufo/fontinfo.plist", "rb") as plist_file:
# 	fontinfo = plistlib.load(plist_file)
# with open("LibreDotMatrix-Screen.ufo/fontinfo.plist", "wb") as plist_file:
# 	fontinfo["openTypeOS2Selection"] = [7]
# 	plistlib.dump(fontinfo, plist_file)

#######################################
# Print style
font.revert()

font["dot"].clear()
circle = fontforge.unitShape(0) # creates a unit circle
circle.draw(font["dot"].glyphPen()) # draws the circle into the glyph, replacing previous outlines
font["dot"].transform((48.0, 0.0, 0.0, 48.0, 50.0, 50.0))
font["dot"].round()
font["dot"].width = 100
font["dot"].unlinkThisGlyph()
font["dot"].clear()
font.fontname = "LibreDotMatrixPrint"
font.familyname = "Libre Dot Matrix Print"
font.fullname = "Libre Dot Matrix Print"
font.appendSFNTName("English (US)", 17, "Print")
font.appendSFNTName("English (US)", 21, "Libre Dot Matrix Print")
font.appendSFNTName("English (US)", 22, "Regular")
font.save("LibreDotMatrix-Print.sfd")
# with open("LibreDotMatrix-Print.ufo/fontinfo.plist", "rb") as plist_file:
# 	fontinfo = plistlib.load(plist_file)
# with open("LibreDotMatrix-Print.ufo/fontinfo.plist", "wb") as plist_file:
# 	fontinfo["openTypeOS2Selection"] = [7]
# 	plistlib.dump(fontinfo, plist_file)

#######################################
# Video style
font.revert()

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

font.fontname = "LibreDotMatrixVideo"
font.familyname = "Libre Dot Matrix Video"
font.fullname = "Libre Dot Matrix Video"
font.appendSFNTName("English (US)", 17, "Video")
font.appendSFNTName("English (US)", 21, "Libre Dot Matrix Video")
font.appendSFNTName("English (US)", 22, "Regular")
font.save("LibreDotMatrix-Video.sfd")
# with open("LibreDotMatrix-Video.ufo/fontinfo.plist", "rb") as plist_file:
# 	fontinfo = plistlib.load(plist_file)
# with open("LibreDotMatrix-Video.ufo/fontinfo.plist", "wb") as plist_file:
# 	fontinfo["openTypeOS2Selection"] = [7]
# 	plistlib.dump(fontinfo, plist_file)


# glyph.user_decomp
# glyph.build()