@echo off

rem Build OpenType fonts
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-builder.py config.yaml

rem Patch in META table to fonts
@cd ..
for /r fonts %%f in (*) do ttx -o %%f -m %%f sources\meta.ttx

rem Generate sample images
python documentation\image3.py --output documentation\sample.png

rem Generate proof HTML documents
@cd fonts\ttf
set PYTHONUTF8=1
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-gen-html.py proof -o ..\..\out\proof MatrixSansPrint-Regular.ttf MatrixSans-Regular.ttf MatrixSansScreen-Regular.ttf MatrixSansVideo-Regular.ttf MatrixSansRaster-Regular.ttf

@cd ..\..\sources