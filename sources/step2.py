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

dot_size = 100
filename = sys.argv[1][:-4]
font = fontforge.open(sys.argv[1])

# Regular style
font["dot"].unlinkThisGlyph()
font["dot"].clear()
font.selection.all()
font.removeOverlap()
font.simplify()
font.round(0.1) # hack: the "dot" glyph is deliberately 1 unit too large so that simplify() produces nicer outlines; this reverses that
font.generate(filename + "-Regular.ufo")

# Screen style
font.revert()
font.selection.select("dot")
font.round(0.1)
font["dot"].transform((0.8, 0.0, 0.0, 0.8, 10.0, 10.0))
font.generate(filename + "Screen-Regular.ufo")

# Print style
font["dot"].clear()
circle = fontforge.unitShape(0) # creates a unit circle
circle.draw(font["dot"].glyphPen()) # draws the circle into the glyph, replacing previous outlines
font["dot"].transform((45.0, 0.0, 0.0, 45.0, 50.0, 50.0))
font["dot"].round()
font["dot"].width = 100
font.generate(filename + "Print-Regular.ufo")

# glyph.user_decomp
# glyph.build()