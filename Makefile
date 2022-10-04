PANDOC=pandoc

ROOT=""

PANDOCARGS=-t revealjs -s -V theme=night --css=http://lab.hakim.se/reveal-js/css/theme/night.css \
					 --css=$(ROOT)/css/ucl_reveal.css --css=$(ROOT)/site-styles/reveal.css \
           --default-image-extension=png --highlight-style=zenburn --mathjax -V revealjs-url=http://lab.hakim.se/reveal-js

NOTEBOOKS=$(filter-out %.v2.ipynb %.nbconvert.ipynb,$(sort $(wildcard ch*/*.ipynb)))
SVGS=$(wildcard ch*/*.svg)

HTMLS=$(NOTEBOOKS:.ipynb=.html)

EXECUTED=$(NOTEBOOKS:.ipynb=.nbconvert.ipynb)
PNGS=$(SVGS:.svg=.png)
NBV2=$(NOTEBOOKS:.ipynb=.v2.ipynb)

default: _site

%/slides.html: %/*.md Makefile
	cat $^ | $(PANDOC) $(PANDOCARGS) -o $@

%.png: %.py Makefile
	python $< $@

%.png: %.nto Makefile
	neato $< -T png -o $@

%.png: %.dot Makefile
	dot $< -T png -o $@

%.png: %.svg Makefile
	dbus-run-session inkscape -z -e $@ -w 600 $<

%.png: %.uml plantuml.jar Makefile
	java -Djava.awt.headless=true -jar plantuml.jar -p < $< > $@

%.html: %.nbconvert.ipynb Makefile jekyll_template
	jupyter nbconvert --to html  --template jekyll_template --stdout $< > $@

%.v2.ipynb: %.nbconvert.ipynb
	jupyter nbconvert --to notebook --nbformat 2 --stdout $< > $@

%.nbconvert.ipynb: %.ipynb
	jupyter nbconvert --to notebook --allow-errors --ExecutePreprocessor.timeout=120 --execute --stdout $< > $@

notes.pdf: combined.ipynb $(PNGS) Makefile
	jupyter nbconvert --to pdf --template latex_template $<
	mv combined.pdf notes.pdf

combined.ipynb: $(EXECUTED)
	python nbmerge.py $^ $@
	sed -i -e 's/\.svg/\.png/g' $@

notes.tex: combined.ipynb $(PNGS) Makefile
	jupyter nbconvert --to latex --template latex_template $<
	mv combined.tex notes.tex

notebooks.zip: ${NBV2}
	zip -r notebooks $^

ready:  $(HTMLS) # notes.pdf notebooks.zip

plantuml.jar:
	wget http://sourceforge.net/projects/plantuml/files/plantuml.jar/download -O plantuml.jar

.PHONY: ready

_site: ready
	jekyll build --verbose

preview: ready
	jekyll serve --verbose

clean:
	rm -f ch*/generated/*.png
	rm -rf ch*/*.html
	rm -f ch*/*.pyc
	rm -f index.html
	rm -rf _site
	rm -rf images js css _includes _layouts favicon* master.zip indigo-jekyll-master
	rm -f indigo
	rm -f ch01python/analyzer.py
	rm -f ch01python/eight
	rm -f ch01python/eight.py
	rm -rf ch01python/module1/
	rm -f ch01python/pretty.py
	rm -f ch*/*.nbconvert.ipynb
	rm -rf ch*/*.v2.ipynb
	rm -rf combined*
	rm -f notes.pdf
	rm -f notes.tex
	rm -f ch04packaging/greeter.py
	rm -f ch04packaging/map.png
	rm -f ch05construction/anotherfile.py
	rm -f ch05construction/config.yaml
	rm -f ch05construction/context.py
	rm -f ch06design/fixed.png
	rm -f ch07dry/datasource*.yaml
	rm -f ch07dry/example.yaml
	rm -f notebooks.zip
