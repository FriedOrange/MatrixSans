@echo off

cd sources

rem Build OpenType fonts
gftools builder config.yaml

rem Generate kerning demonstration page
fontforge -script ..\scripts\makekerntest.py

cd ..

rem Generate sample images
python documentation\image3.py --output documentation\sample.png

rem Generate proof HTML documents
cd fonts\ttf
diffenator2 proof -o ..\..\out\proof MatrixSansPrint-Regular.ttf MatrixSans-Regular.ttf MatrixSansScreen-Regular.ttf MatrixSansVideo-Regular.ttf MatrixSansRaster-Regular.ttf

cd ..\..