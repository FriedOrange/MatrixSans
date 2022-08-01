sfd2ufo LibreDotMatrix-Regular.sfd LibreDotMatrix-Regular.ufo
sfd2ufo LibreDotMatrix-Print.sfd LibreDotMatrix-Print.ufo
sfd2ufo LibreDotMatrix-Screen.sfd LibreDotMatrix-Screen.ufo
sfd2ufo LibreDotMatrix-Video.sfd LibreDotMatrix-Video.ufo
copy features.fea LibreDotMatrix-Regular.ufo\features.fea
copy features.fea LibreDotMatrix-Print.ufo\features.fea
copy features.fea LibreDotMatrix-Screen.ufo\features.fea
copy features.fea LibreDotMatrix-Video.ufo\features.fea
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-builder.py config.yaml
@cd .. 
python documentation\image1.py --output documentation\4styles.png
python documentation\image2.py --output documentation\sample.png
@cd fonts\ttf
set PYTHONUTF8=1
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-gen-html.py proof -o ..\..\out\proof LibreDotMatrix-Print.ttf LibreDotMatrix-Regular.ttf LibreDotMatrix-Screen.ttf LibreDotMatrix-Video.ttf
@cd ..\..\sources