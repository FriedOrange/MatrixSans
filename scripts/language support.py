import json

with open("matrix sans 1.800 chars.txt", encoding="utf-8") as input_file:
	supported_chars = set(input_file.read())

with open("languages.json", encoding="utf-8") as input_file:
	langs = json.load(input_file)

supported_langs = []
for key in langs.keys():
	if all(char in supported_chars for char in langs[key]["base_chars"] + (langs[key]["aux_chars"] if "aux_chars" in langs[key] else "")):
		supported_langs.append(key)

print(", ".join(langs[key]["name"] for key in sorted(supported_langs, key=(lambda x: langs[x].get("speakers", 0)), reverse=True)))
print(len(supported_langs))

supported_langs_10m = list(filter(lambda x: langs[x].get("speakers", 0) >= 10000000, supported_langs))
supported_langs_1m = list(filter(lambda x: 1000000 <= langs[x].get("speakers", 0) < 10000000, supported_langs))
supported_langs_100k = list(filter(lambda x: 100000 <= langs[x].get("speakers", 0) < 1000000, supported_langs))
supported_langs_10k = list(filter(lambda x: 10000 <= langs[x].get("speakers", 0) < 100000, supported_langs))
supported_langs_1k = list(filter(lambda x: 1000 <= langs[x].get("speakers", 0) < 10000, supported_langs))

print("Languages with at least 10,000,000 speakers:")
print(", ".join(sorted(langs[key]["name"] for key in supported_langs_10m)))
print("Languages with at least 1,000,000 speakers:")
print(", ".join(sorted(langs[key]["name"] for key in supported_langs_1m)))
print("Languages with at least 100,000 speakers:")
print(", ".join(sorted(langs[key]["name"] for key in supported_langs_100k)))
print("Languages with at least 10,000 speakers:")
print(", ".join(sorted(langs[key]["name"] for key in supported_langs_10k)))
print("Languages with at least 1,000 speakers:")
print(", ".join(sorted(langs[key]["name"] for key in supported_langs_1k)))