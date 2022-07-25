set PYTHONUTF8=1
cd ..
fontbakery check-googlefonts -C -l PASS --succinct --badges out/badges --html out/fontbakery/fontbakery-report.html fonts/ttf/*.ttf > test.log
cd sources