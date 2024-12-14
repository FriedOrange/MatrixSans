import fontforge
import plistlib

OLD_FILE = "MatrixSans-Regular.ufo/lib.plist"
NEW_FILE = "temp/lib.plist"
MASTER_FONT = "MatrixSans-MASTER.sfd"

# get production glyph names that differ from development names
ps_names = {}
for glyph in fontforge.open(MASTER_FONT):
	uni = fontforge.unicodeFromName(glyph)
	if glyph.endswith("-cy.sc"):
		aglfn_name = glyph.replace("-", "_") # hyphen not allowed in PS names
	elif uni < 0:
		continue # other unencoded glyphs are OK (currently)
	else:
		aglfn_name = fontforge.nameFromUnicode(uni, "AGL For New Fonts")
	if glyph != aglfn_name:
		ps_names[glyph] = aglfn_name

with open(OLD_FILE, "rb") as input_file:
	lib = plistlib.load(input_file)

# specify production names
lib["public.postscriptNames"] = ps_names
# add 'meta' OpenType table
lib["public.openTypeMeta"] = {
		"dlng": ["Latn", "Cyrl"],
		"slng": ["Latn", "Cyrl"]
	}

with open(NEW_FILE, "wb") as output_file:
	plistlib.dump(lib, output_file, sort_keys=False)
