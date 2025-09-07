SOURCES=$(shell python3 scripts/read-config.py --sources )
FAMILY=$(shell python3 scripts/read-config.py --family )
DRAWBOT_SCRIPTS=$(shell ls documentation/*.py)
DRAWBOT_OUTPUT=$(shell ls documentation/*.py | sed 's/\.py/.png/g')

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontbakery"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

venv-test: venv-test/touchfile

build.stamp: venv .init.stamp sources/config.yaml $(SOURCES)
	. venv/bin/activate; rm -rf fonts/; gftools builder sources/config.yaml && touch build.stamp; 
#find fonts/ -type f -exec ttx -o {} -m {} sources/meta.ttx \;

.init.stamp: venv
	. venv/bin/activate; python3 scripts/first-run.py

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

venv-test/touchfile: requirements-test.txt
	test -d venv-test || python3 -m venv venv-test
	. venv-test/bin/activate; pip install -Ur requirements-test.txt
	touch venv-test/touchfile
	
test: venv-test build.stamp
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; . venv-test/bin/activate; mkdir -p out/ out/fontbakery; fontbakery check-googlefonts -l WARN --full-lists --succinct --badges out/badges --html out/fontbakery/fontbakery-report.html -j $$TOCHECK  || echo '::warning file=sources/config.yaml,title=Fontbakery failures::The fontbakery QA check reported errors in your font. Please check the generated report.'

proof: venv build.stamp
# 	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p out/ out/proof; diffenator2 proof $$TOCHECK -o out/proof
	. venv/bin/activate; mkdir -p out/ out/proof out/proof/regular out/proof/regular-sc out/proof/print out/proof/print-sc out/proof/screen out/proof/screen-sc out/proof/raster out/proof/raster-sc out/proof/video out/proof/video-sc; diffenator2 proof -o out/proof/regular fonts/ttf/MatrixSans-Regular.ttf; diffenator2 proof -o out/proof/print fonts/ttf/MatrixSansPrint-Regular.ttf; diffenator2 proof -o out/proof/screen fonts/ttf/MatrixSansScreen-Regular.ttf; diffenator2 proof -o out/proof/video fonts/ttf/MatrixSansVideo-Regular.ttf; diffenator2 proof -o out/proof/raster fonts/ttf/MatrixSansRaster-Regular.ttf; diffenator2 proof -o out/proof/regular-sc fonts/ttf/MatrixSansSC-Regular.ttf; diffenator2 proof -o out/proof/print-sc fonts/ttf/MatrixSansPrintSC-Regular.ttf; diffenator2 proof -o out/proof/screen-sc fonts/ttf/MatrixSansScreenSC-Regular.ttf; diffenator2 proof -o out/proof/video-sc fonts/ttf/MatrixSansVideoSC-Regular.ttf; diffenator2 proof -o out/proof/raster-sc fonts/ttf/MatrixSansRasterSC-Regular.ttf

images: venv build.stamp $(DRAWBOT_OUTPUT)
	git add documentation/*.png && git commit -m "Rebuild images" documentation/*.png

%.png: %.py build.stamp
	python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" | xargs rm delete

update-ufr:
	npx update-template https://github.com/googlefonts/Unified-Font-Repository/

update:
	pip install --upgrade $(dependency); pip freeze > requirements.txt
