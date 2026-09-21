@echo off
cd sources

fontforge -script step2.py

rem Generate intermediate UFO sources
for %%f in (temp\Matrix*-Regular.sfd) do (
	sfd2ufo %%f %%~nf.ufo
)
for %%f in (temp\MatrixSans*-Regular.sfd) do (
	echo include(common.fea^); > %%~nf.ufo\features.fea
	echo include(proportional.fea^); >> %%~nf.ufo\features.fea
)

rem Add fixed lib.plist to UFO sources
fontforge -script fixufo.py
for %%f in (temp\Matrix*-Regular.sfd) do copy temp\lib.plist %%~nf.ufo\lib.plist

rem Patch Video style feature file
python patchccmp.py
echo include(common-video.fea); > MatrixSansVideo-Regular.ufo\features.fea
echo include(proportional.fea); >> MatrixSansVideo-Regular.ufo\features.fea
echo include(common-video.fea); > MatrixSansSmooth-Regular.ufo\features.fea
echo include(proportional.fea); >> MatrixSansSmooth-Regular.ufo\features.fea

cd ..