@echo off

cd sources

rem Build OpenType fonts
gftools builder config.yaml

rem Generate kerning demonstration page
rem for /f %%h in ('git rev-parse --short HEAD') do fontforge -script ..\scripts\makekerntest.py %%h

cd ..

rem Generate sample images
rem python scripts\image3.py --output documentation\sample.png

rem Generate proof HTML documents
cd fonts\ttf
..\..\proof
cd ..\..