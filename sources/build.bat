@echo off

rem Generate intermediate UFO sources
for %%f in (MatrixSans-*.sfd) do (
	sfd2ufo %%f %%~nf.ufo
	copy features.fea %%~nf.ufo\features.fea
)

rem Build OpenType fonts
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-builder.py config.yaml

rem Patch in META table to fonts
@cd ..
for /r fonts %%f in (*) do ttx -o %%f -m %%f sources\meta.ttx

rem Generate sample images
python documentation\image1.py --output documentation\4styles.png
python documentation\image2.py --output documentation\sample.png

rem Generate proof HTML documents
@cd fonts\ttf
set PYTHONUTF8=1
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-gen-html.py proof -o ..\..\out\proof MatrixSans-Print.ttf MatrixSans-Regular.ttf MatrixSans-Screen.ttf MatrixSans-Video.ttf MatrixSans-Raster.ttf

@cd ..\..\sources