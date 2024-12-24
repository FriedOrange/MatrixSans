# step2.py
# pass this script to FontForge to build the intermediate UFO sources for each style

# Copyright 2024 Brad Neil
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import fontforge

DOT_SIZE = 100
GLYPH_WIDTH = 8
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
	skip = False
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

def make_regular(source):
	font = fontforge.open(source)
	font["dot"].unlinkThisGlyph()
	font["dot"].clear()
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
	font.selection.select("dot")
	font.round(0.1)
	font["dot"].transform((SCREEN_DOT_FACTOR, 0.0, 0.0, SCREEN_DOT_FACTOR, (DOT_SIZE - DOT_SIZE * SCREEN_DOT_FACTOR) / 2, (DOT_SIZE - DOT_SIZE * SCREEN_DOT_FACTOR) / 2))
	font["dot"].unlinkThisGlyph()
	font["dot"].clear()
	add_names(font, "Screen")
	font.uwidth = int(SCREEN_DOT_FACTOR * DOT_SIZE)
	font.os2_strikeysize = int(SCREEN_DOT_FACTOR * DOT_SIZE)
	font.os2_strikeypos += int((DOT_SIZE - font.os2_strikeysize) / 2)
	font.os2_panose = segmented_panose(font.os2_panose)
	font.save(f"temp\\MatrixSansScreen-{font.weight}.sfd")

def make_print(source, name_suffix=""):
	font = fontforge.open(source)
	font["dot"].clear()
	circle = fontforge.unitShape(0) # creates a unit circle
	circle.draw(font["dot"].glyphPen()) # draws the circle into the glyph, replacing previous outlines
	font["dot"].transform((PRINT_DOT_RADIUS, 0.0, 0.0, PRINT_DOT_RADIUS, DOT_SIZE / 2, DOT_SIZE / 2))
	font["dot"].round()
	font["dot"].width = 100
	font["dot"].unlinkThisGlyph()
	font["dot"].clear()
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

	font.createChar(-1, "halfdot")
	pen = font["halfdot"].glyphPen()
	pen.moveTo(0,0)
	pen.lineTo(0,DOT_SIZE // 2 + 1)
	pen.lineTo(DOT_SIZE // 2 + 1, DOT_SIZE // 2 + 1)
	pen.lineTo(DOT_SIZE // 2 + 1, 0)
	pen.closePath()
	pen = None

	for glyph in font:

		video_aux_font = fontforge.open(VIDEO_AUX_SOURCE)

		# determine where the dots are in each glyph
		matrix, skip = get_pattern(font, glyph)
		if skip:
			continue

		# basic interpolation, Mullard SAA5050 style
		for x in range(GLYPH_WIDTH - 1):
			for y in range(GLYPH_HEIGHT - 1):
				if matrix[x][y] and matrix[x + 1][y + 1] and not (matrix[x + 1][y] or matrix[x][y + 1]):
					font[glyph].addReference("halfdot", (1, 0, 0, 1, x * DOT_SIZE + DOT_SIZE // 2 + LEFT_SIDE_BEARING, (y - DESCENT_DOTS + 1) * DOT_SIZE))
					font[glyph].addReference("halfdot", (1, 0, 0, 1, (x + 1) * DOT_SIZE + LEFT_SIDE_BEARING, (y - DESCENT_DOTS) * DOT_SIZE + DOT_SIZE // 2))
				if matrix[x][y + 1] and matrix[x + 1][y] and not (matrix[x][y] or matrix[x + 1][y + 1]):
					font[glyph].addReference("halfdot", (1, 0, 0, 1, x * DOT_SIZE + DOT_SIZE // 2 + LEFT_SIDE_BEARING, (y - DESCENT_DOTS) * DOT_SIZE + DOT_SIZE // 2))
					font[glyph].addReference("halfdot", (1, 0, 0, 1, (x + 1) * DOT_SIZE + LEFT_SIDE_BEARING, (y - DESCENT_DOTS + 1) * DOT_SIZE))

	for glyph in video_aux_font:
		video_aux_font.selection.select(glyph)
		video_aux_font.copy()
		font.selection.select(glyph)
		font.paste()

	# interpolation done, now finish it off the same as Regular style
	font["dot"].unlinkThisGlyph()
	font["halfdot"].unlinkThisGlyph()
	font["dot"].clear()
	font["halfdot"].clear()

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

	font["dot"].clear()
	pen = font["dot"].glyphPen()
	pen.moveTo((-15, 50))
	pen.curveTo((-15, 72), (3, 90), (25, 90))

	pen.lineTo((75, 90))
	pen.curveTo((97, 90), (115, 72), (115, 50))
	pen.curveTo((115, 28), (97, 10), (75, 10))

	pen.lineTo(25, 10)
	pen.curveTo((3, 10), (-15, 28), (-15, 50))
	pen.closePath()
	font["dot"].width = 100

	font.createChar(-1, "dot2") # overlaps with dot to the right
	pen = font["dot2"].glyphPen()
	pen.moveTo((74, 90))
	pen.lineTo((126, 90))
	pen.lineTo((126, 10))
	pen.lineTo((74, 10))
	pen.closePath()
	font["dot2"].width = 100

	for glyph in font:

		# determine where the dots are in each glyph
		matrix, skip = get_pattern(font, glyph)
		if skip:
			continue

		for j in range(GLYPH_HEIGHT):
			for i in range(GLYPH_WIDTH - 1):
				if matrix[i][j] and matrix[i + 1][j]:
					if glyph == "underscore" or glyph == "emdash":
						font[glyph].addReference("dot2", (1, 0, 0, 1, i * DOT_SIZE, (j - DESCENT_DOTS) * DOT_SIZE))
					else:
						font[glyph].addReference("dot2", (1, 0, 0, 1, i * DOT_SIZE + LEFT_SIDE_BEARING, (j - DESCENT_DOTS) * DOT_SIZE))

	font["dot"].unlinkThisGlyph()
	font["dot"].clear()
	font["dot2"].unlinkThisGlyph()
	font["dot2"].clear()
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

def main():
	make_regular(MAIN_SOURCE)
	make_print(MAIN_SOURCE)
	make_raster(MAIN_SOURCE)
	make_screen(MAIN_SOURCE)
	make_video(MAIN_SOURCE)
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