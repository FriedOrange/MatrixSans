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
	@echo "  make test:   Tests the fonts with fontspector"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

customize: venv
	. venv/bin/activate; python3 scripts/customize.py

build.stamp: venv sources/config.yaml $(SOURCES)
	rm -rf fonts
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config; done)  && touch build.stamp

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: build.stamp
	which fontspector || (echo "fontspector not found. Please install it with 'cargo install fontspector'." && exit 1)
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; mkdir -p out/ out/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html out/fontspector/fontspector-report.html --badges out/badges $$TOCHECK  || echo '::warning file=sources/config.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'

proof: venv build.stamp
# 	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p out/ out/proof; diffenator2 proof $$TOCHECK -o out/proof
	. venv/bin/activate; mkdir -p out/ out/proof out/proof/sans out/proof/sanssc out/proof/print out/proof/printsc out/proof/screen out/proof/screensc out/proof/raster out/proof/rastersc out/proof/video out/proof/videosc out/proof/smooth out/proof/smoothsc out/proof/mono out/proof/monosc out/proof/monoprint out/proof/monoprintsc out/proof/monoraster out/proof/monorastersc out/proof/monoscreen out/proof/monoscreensc out/proof/monosmooth out/proof/monosmoothsc out/proof/monovideo out/proof/monovideosc; diffenator2 proof -o out/proof/sans fonts/ttf/MatrixSans-Regular.ttf; diffenator2 proof -o out/proof/print fonts/ttf/MatrixSansPrint-Regular.ttf; diffenator2 proof -o out/proof/screen fonts/ttf/MatrixSansScreen-Regular.ttf; diffenator2 proof -o out/proof/video fonts/ttf/MatrixSansVideo-Regular.ttf; diffenator2 proof -o out/proof/raster fonts/ttf/MatrixSansRaster-Regular.ttf; diffenator2 proof -o out/proof/sanssc fonts/ttf/MatrixSansSC-Regular.ttf; diffenator2 proof -o out/proof/printsc fonts/ttf/MatrixSansPrintSC-Regular.ttf; diffenator2 proof -o out/proof/screensc fonts/ttf/MatrixSansScreenSC-Regular.ttf; diffenator2 proof -o out/proof/videosc fonts/ttf/MatrixSansVideoSC-Regular.ttf; diffenator2 proof -o out/proof/rastersc fonts/ttf/MatrixSansRasterSC-Regular.ttf; diffenator2 proof -o out/proof/smooth fonts/ttf/MatrixSansSmooth-Regular.ttf; diffenator2 proof -o out/proof/smoothsc fonts/ttf/MatrixSansSmoothSC-Regular.ttf; diffenator2 proof -o out/proof/mono fonts/ttf/MatrixMono-Regular.ttf; diffenator2 proof -o out/proof/monoprint fonts/ttf/MatrixMonoPrint-Regular.ttf; diffenator2 proof -o out/proof/monoraster fonts/ttf/MatrixMonoRaster-Regular.ttf; diffenator2 proof -o out/proof/monoscreen fonts/ttf/MatrixMonoScreen-Regular.ttf



images: venv $(DRAWBOT_OUTPUT)

%.png: %.py build.stamp
	. venv/bin/activate; python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" -delete

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	git commit -m "Update requirements" requirements.txt
	git push