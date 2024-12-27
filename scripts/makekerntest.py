import re, fontforge

font = fontforge.open("MatrixSans-MASTER.sfd")

with open("features.fea", "r", encoding="utf-8") as feature_file:
	fea = feature_file.read()
	start_pos = fea.find("# Classes for kerning")
	end_pos = fea.find("kern;", start_pos)
	fea_lines = fea[start_pos:end_pos].splitlines()
	classes = {}
	output_lines = []
	smcp_lines = []
	n_of_pairs = 1
	first_of_pairs = set()
	second_of_pairs = set()
	for line in fea_lines:
		if line.startswith("@"):
			classname = re.search(r"\w+", line).group(0)
			classes[classname] = re.search(r"\[(.+)\]", line).group(1).split(" ")
			if n_of_pairs == 1:
				for glyph in classes[classname]:
					if glyph in first_of_pairs:
						print(f"Warning: {glyph} in > 1 1st-of-pair class")
					first_of_pairs.add(glyph)
			else:
				for glyph in classes[classname]:
					if glyph in second_of_pairs:
						print(f"Warning: {glyph} in > 1 2nd-of-pair class")
					second_of_pairs.add(glyph)
		elif line == "# Second-of-pair classes":
			n_of_pairs = 2
		elif line.startswith("\tpos") or line.startswith("\tenum pos"):
			try:
				left, right = re.search(r"pos ([^ ]+|\[.+\]) ([^ ]+|\[.+\]) -?\d", line).group(1, 2)
				def enum_class(classname):
					if classname.startswith("@"):
						result = classes[classname[1:]]
					elif classname.startswith("["):
						result = classname[1:-1].split(" ")
					else:
						result = [classname]
					return result
				left_class = enum_class(left)
				right_class = enum_class(right)
				output_lines.append(f"<h4>{left} {right}</h4>\n<pre contenteditable spellcheck='false'>")
				for glyph1 in left_class:
					uni1 = font[glyph1].unicode
					prefix = ""
					suffix = ""
					if uni1 == -1:
						if glyph1.endswith(".sc") and glyph1 != "idotaccent.sc":
							prefix = "<span class='sc'>"
							suffix = "</span>"
							uni1 = font[glyph1[:-3]].unicode
						else:
							continue
					new_output_line = []
					for glyph2 in right_class:
						if glyph1.endswith(".sc") and not (glyph2[0].isupper() or glyph2.endswith(".sc")):
							continue
						uni2 = font[glyph2].unicode
						prefix2 = ""
						suffix2 = ""
						if uni2 == -1:
							if glyph2.endswith(".sc") and glyph2 != "idotaccent.sc" and glyph1[0].isupper():
								prefix2 = "<span class='sc'>"
								suffix2 = "</span>"
								uni2 = font[glyph2[:-3]].unicode
							elif glyph2.endswith(".sc") and glyph2 != "idotaccent.sc" and glyph1.endswith(".sc"):
								uni2 = font[glyph2[:-3]].unicode
							else:
								continue
						new_output_line.append(f"{prefix2}{chr(uni1)}{chr(uni2)}{suffix2}")
					if len(new_output_line):
						output_lines.append(prefix + " ".join(new_output_line) + f"{suffix}\n")
				output_lines.append("</pre>")
			except Exception as e:
				print(e)
				print(glyph1)
				print(glyph2)

html_pre = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Matrix Sans kerning test</title>
<style>
	@font-face {
			font-family: "Matrix Sans";
			src: url("proof/MatrixSans-Regular.ttf"),
				 url("../fonts/ttf/MatrixSans-Regular.ttf");
		}
	body {
		color: white;
		background-color: black;
		margin: 1em;
	}
	body, pre {
		font-family: "Matrix Sans";
		font-size: 24px;
	}
	.sc {
		font-feature-settings: "smcp";
	}
	h4 {
		font-weight: normal;
		color: silver;
	}
</style>
</head>
<body>

<pre contenteditable spellcheck="false">
Matrix Sans kern test
Not shown: small cap + lower case kern pairs
</pre>

"""

html_post = """

</body>
</html>
"""
# print(classes)

with open("..\\scripts\\kerntest.html", "w", encoding="utf-8") as output_file:
	output_file.write(html_pre)
	output_file.writelines(output_lines)
	output_file.write(html_post)
