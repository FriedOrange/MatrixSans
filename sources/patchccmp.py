# Add additional substitutions to ccmp feature for Video and Smooth styles

import re

with open("common.fea", "r", encoding="utf-8") as feature_file:
	fea_txt = feature_file.read()

# get original rules from ss01, to be added to ccmp
video_subs = re.findall(r"sub \w+ by \w+\.alt;", re.search("ss01 {.+?} ss01;", fea_txt, flags=re.DOTALL).group(0))

# invert the substitutions in ss01
fea_txt = re.sub("ss01 {.+?} ss01;", lambda m: re.sub(r"(\w+) by (\w+\.alt)", r"\2 by \1", m.group(0)), fea_txt, flags=re.DOTALL)

# find the position to insert the original ss01 rules
ccmp_insertion_pos = re.search("### <-- RULES INSERTED AUTOMATICALLY", fea_txt).start(0)

with open("common-video.fea", "w", encoding="utf-8") as video_feature_file:
	video_feature_file.write(fea_txt[:ccmp_insertion_pos])
	video_feature_file.writelines(video_subs)
	video_feature_file.write(fea_txt[ccmp_insertion_pos:])