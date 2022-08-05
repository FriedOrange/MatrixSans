sfd2ufo MatrixSans-Regular.sfd MatrixSans-Regular.ufo
sfd2ufo MatrixSans-Print.sfd MatrixSans-Print.ufo
sfd2ufo MatrixSans-Screen.sfd MatrixSans-Screen.ufo
sfd2ufo MatrixSans-Video.sfd MatrixSans-Video.ufo
copy features.fea MatrixSans-Regular.ufo\features.fea
copy features.fea MatrixSans-Print.ufo\features.fea
copy features.fea MatrixSans-Screen.ufo\features.fea
copy features.fea MatrixSans-Video.ufo\features.fea
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-builder.py config.yaml
@cd .. 
python documentation\image1.py --output documentation\4styles.png
python documentation\image2.py --output documentation\sample.png
@cd fonts\ttf
set PYTHONUTF8=1
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-gen-html.py proof -o ..\..\out\proof MatrixSans-Print.ttf MatrixSans-Regular.ttf MatrixSans-Screen.ttf MatrixSans-Video.ttf
@cd ..\..\sources