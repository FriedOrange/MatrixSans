# Add additional substitutions to ccmp feature for Video style

import re

with open("features.fea", "r", encoding="utf-8") as feature_file:
	fea_txt = feature_file.read()

video_subs = re.findall(r"sub \w+ by \w+\.alt;", re.search("ss01 {.+?} ss01;", fea_txt, flags=re.DOTALL).group(0))

fea_txt = re.sub("ss01 {.+?} ss01;", lambda m: re.sub(r"(\w+) by (\w+\.alt)", r"\2 by \1", m.group(0)), fea_txt, flags=re.DOTALL)

ccmp_end_pos = re.search("} ccmp;", fea_txt).start(0)

with open("MatrixSansVideo-Regular.ufo\\features.fea", "w", encoding="utf-8") as video_feature_file:
	video_feature_file.write(fea_txt[:ccmp_end_pos])
	video_feature_file.writelines(video_subs)
	video_feature_file.write(fea_txt[ccmp_end_pos:])