@echo off
cd sources

fontforge -script step2.py

rem Generate intermediate UFO sources
for %%f in (temp\MatrixSans*-Regular.sfd) do (
	sfd2ufo %%f %%~nf.ufo
	copy features.fea %%~nf.ufo\features.fea
)

cd ..