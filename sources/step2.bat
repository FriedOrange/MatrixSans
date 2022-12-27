@echo off

fontforge -script step2.py "MatrixSans-MASTER.sfd"

rem Generate intermediate UFO sources
for %%f in (temp\MatrixSans*-Regular.sfd) do (
	sfd2ufo %%f %%~nf.ufo
	copy features.fea %%~nf.ufo\features.fea
)