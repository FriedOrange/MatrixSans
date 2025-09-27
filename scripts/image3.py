# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/image1.py --output documentation/image1.png

# Import moduels from external python packages: https://pypi.org/
from drawbot_skia.drawbot import *
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

# Import moduels from the Python Standard Library: https://docs.python.org/3/library/
import subprocess
import sys
import argparse

# Constants, these are the main "settings" for the image
DRAW_AUX_TEXT = False

WIDTH, HEIGHT, MARGIN, FRAMES = 1024, 512, 32, 1
FONT_PATH = "fonts/otf/MatrixSans-Regular.otf"
FONT_LICENSE = "Open Font License v1.1"
AUXILIARY_FONT = "Bahnschrift"
AUXILIARY_FONT_SIZE = 22
BIG_TEXT = "Aa"
BIG_TEXT_FONT_SIZE = 80
BIG_TEXT_SIDE_MARGIN = WIDTH // 2
BIG_TEXT_INTERLINE = BIG_TEXT_FONT_SIZE * (1.1 if DRAW_AUX_TEXT else 1.3)
BIG_TEXT_BOTTOM_MARGIN = (HEIGHT - (BIG_TEXT_INTERLINE * 4)) / 2 + BIG_TEXT_FONT_SIZE * (0.2 if DRAW_AUX_TEXT else 0.3)
GRID_VIEW = False # Change this to "True" for a grid overlay

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()



# Constants that are worked out dynamically
MY_URL = subprocess.check_output("git remote get-url origin", shell=True).decode()
MY_HASH = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()



# Draws a grid
def grid():
	stroke(1, 0, 0, 0.75)
	strokeWidth(2)
	STEP_X, STEP_Y = 0, 0
	INCREMENT_X, INCREMENT_Y = MARGIN / 2, MARGIN / 2
	rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
	for x in range(29):
		polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
		STEP_X += INCREMENT_X
	for y in range(29):
		polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
		STEP_Y += INCREMENT_Y
	polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
	polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
	inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
	outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
	valueScaled = float(value - inputMin) / float(inputSpan)
	return outputMin + (valueScaled * outputSpan)


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background(colour, height):
	newPage(WIDTH, height)
	fill(colour[0], colour[1], colour[2])
	rect(-2, -2, WIDTH + 2, height + 2)
	if GRID_VIEW:
		grid()
	else:
		pass


# Draw main text
def draw_main_text(text_list, colour):
	fill(colour[0], colour[1], colour[2])
	stroke(None)
	font(FONT_PATH)
	fontSize(BIG_TEXT_FONT_SIZE)
	# Adjust this line to center main text manually.
	# TODO: This should be done automatically when drawbot-skia
	# has support for textBox() and FormattedString
	#text(BIG_TEXT, ((WIDTH / 2) - MARGIN * 4.75, (HEIGHT / 2) - MARGIN * 2.5))
	text(text_list[0], (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN + BIG_TEXT_INTERLINE*3), "center")
	text(text_list[1], (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN + BIG_TEXT_INTERLINE*2), "center")
	text(text_list[2], (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN + BIG_TEXT_INTERLINE*1), "center")
	text(text_list[3], (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN + BIG_TEXT_INTERLINE*0), "center")


# Divider lines
def draw_divider_lines(colour):
	stroke(colour)
	strokeWidth(0)
	lineCap("round")
	line((MARGIN, HEIGHT - MARGIN * 2), (WIDTH - MARGIN, HEIGHT - MARGIN * 2))
	line((MARGIN, MARGIN * 2), (WIDTH - MARGIN, MARGIN * 2))
	stroke(None)


# Draw text describing the font and it's git status & repo URL
def draw_auxiliary_text(text_colour):
	# Load the font with the parts of fonttools that are imported with the line:
	# from fontTools.ttLib import TTFont
	# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
	ttFont = TTFont(FONT_PATH)
	# FONT_NAME = ttFont["name"].getDebugName(4)
	# FONT_NAME = ttFont["name"].getBestFamilyName()
	FONT_NAME = ttFont["name"].getBestFullName()
	if str(FONT_NAME) == "Matrix Sans":
		FONT_NAME = "Matrix Sans Regular"
	# FONT_VERSION = "v%s" % floatToFixedToStr(ttFont["head"].fontRevision, 16)
	FONT_VERSION = str(ttFont["name"].getName(5, 3, 1))
	# Setup
	fill(text_colour)
	font(AUXILIARY_FONT)
	fontSize(AUXILIARY_FONT_SIZE)
	# print(listFontVariations())
	fontVariations(wdth=100, wght=350)
	POS_TOP_LEFT = (MARGIN, HEIGHT - MARGIN * 1.75)
	POS_TOP_RIGHT = (WIDTH - MARGIN, HEIGHT - MARGIN * 1.75)
	POS_BOTTOM_LEFT = (MARGIN, MARGIN * 1.25)
	POS_BOTTOM_RIGHT = (WIDTH - MARGIN * 0.95, MARGIN * 1.25)
	URL_AND_HASH = MY_URL + "at commit " + MY_HASH
	# URL_AND_HASH = MY_URL
	URL_AND_HASH = URL_AND_HASH.replace("\n", " ")
	# Draw Text
	text(FONT_NAME, POS_TOP_LEFT, align="left")
	text(FONT_VERSION, POS_TOP_RIGHT, align="right")
	text(URL_AND_HASH, POS_BOTTOM_LEFT, align="left")
	text(FONT_LICENSE, POS_BOTTOM_RIGHT, align="right")


def make_image(text_list, text_colour, bg_colour, stripes=False):
	draw_background(bg_colour, HEIGHT)
	if stripes:
		stripe_margin = BIG_TEXT_BOTTOM_MARGIN - (BIG_TEXT_INTERLINE - BIG_TEXT_FONT_SIZE) * (2 if DRAW_AUX_TEXT else 1)
		fill(0.65, 0.85, 0.75)
		rect(0, stripe_margin + BIG_TEXT_INTERLINE * 3, WIDTH, BIG_TEXT_INTERLINE)
		rect(0, stripe_margin + BIG_TEXT_INTERLINE, WIDTH, BIG_TEXT_INTERLINE)
		rect(0, stripe_margin - BIG_TEXT_INTERLINE, WIDTH, BIG_TEXT_INTERLINE)
	draw_main_text(text_list, text_colour)
	aux_colour = (text_avg := sum(text_colour) / 3) + (0.5 - text_avg) * 0.625
	if DRAW_AUX_TEXT:
		draw_divider_lines(aux_colour)
		draw_auxiliary_text(aux_colour)

# Build and save the image
if __name__ == "__main__":
	FONT_PATH = "fonts/otf/MatrixSans-Regular.otf"
	make_image(["MATRIX SANS REGULAR","The quick brown fox","jumps over a lazy dog.","§27 ¶14; { 35°29′10″ }"], [0.1, 0.1, 0.1], [0.9, 0.9, 0.9])
	FONT_PATH = "fonts/otf/MatrixSansPrint-Regular.otf"
	make_image(["MATRIX SANS PRINT","Quick wafting zephyrs","#vex “bold” @Jim :-)","$18.99 €38,76 £1.50 75%"], [0, 0, 0], [0.99, 0.97, 0.95], True)
	FONT_PATH = "fonts/otf/MatrixSansRaster-Regular.otf"
	make_image(["MATRIX SANS RASTER","Pack my box with five","dozen liquor jugs*","150 IF X>32 THEN N=0"], [1, 0.6, 0], [0, 0, 0])
	FONT_PATH = "fonts/otf/MatrixSansScreen-Regular.otf"
	make_image(["MATRIX SANS SCREEN","Jackdaws love my big","sphinx of quartz?","3×(5+1)²−6÷2=105"], [0, 0, 0], [202/255, 228/255, 175/255])
	FONT_PATH = "fonts/otf/MatrixSansVideo-Regular.otf"
	make_image(["MATRIX SANS VIDEO","▶ How quickly daft","jumping zebras vex!","23/04/1987 12:56 PM"], [216/255, 216/255, 216/255], [0, 0, 160/255])
	FONT_PATH = "fonts/otf/MatrixSansSmooth-Regular.otf"
	make_image(["MATRIX SANS SMOOTH", "Bright vixens jump", "& dozy fowl quack.", "«№3½» ±0.5µm ↑ 68Ω"], [0.9, 0.9, 0.9], [0.1, 0.1, 0.1])
	# Save output, using the "--output" flag location
	saveImage(args.output)
	# Print done in the terminal
	print("DrawBot: Done")
	