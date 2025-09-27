@echo off

cd sources

rem Build OpenType fonts
gftools builder config.yaml

rem Generate kerning demonstration page
fontforge -script ..\documentation\makekerntest.py

cd ..

rem Generate sample images
rem python scripts\image3.py --output documentation\sample.png

rem Generate proof HTML documents
cd fonts\ttf
..\..\proof
cd ..\..