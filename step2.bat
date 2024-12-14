@echo off
cd sources

fontforge -script step2.py

rem Generate intermediate UFO sources
for %%f in (temp\MatrixSans*-Regular.sfd) do (
	sfd2ufo %%f %%~nf.ufo
	copy features.fea %%~nf.ufo\features.fea
)

rem Add fixed lib.plist to UFO sources
fontforge -script fixufo.py
for %%f in (temp\MatrixSans*.sfd) do copy temp\lib.plist %%~nf.ufo\lib.plist
cd ..