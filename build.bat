@echo off

rem Build OpenType fonts
@cd sources
gftools builder config.yaml

rem Patch in META table to fonts
@cd ..
rem for /r fonts %%f in (*) do ttx -o %%f -m %%f sources\meta.ttx

rem Generate sample images
python documentation\image3.py --output documentation\sample.png

rem Generate proof HTML documents
@cd fonts\ttf
diffenator2 proof -o ..\..\out\proof MatrixSansPrint-Regular.ttf MatrixSans-Regular.ttf MatrixSansScreen-Regular.ttf MatrixSansVideo-Regular.ttf MatrixSansRaster-Regular.ttf

@cd ..\..