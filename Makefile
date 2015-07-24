PANDOC=pandoc

ROOT=""

PANDOCARGS=-t revealjs -s -V theme=night --css=http://lab.hakim.se/reveal-js/css/theme/night.css \
					 --css=$(ROOT)/css/ucl_reveal.css --css=$(ROOT)/site-styles/reveal.css \
           --default-image-extension=png --highlight-style=zenburn --mathjax -V revealjs-url=http://lab.hakim.se/reveal-js

NOTEBOOKS=$(filter-out %.v2.ipynb %.nbconvert.ipynb,$(wildcard session*/*.ipynb))

HTMLS=$(NOTEBOOKS:.ipynb=.html)

EXECUTED=$(NOTEBOOKS:.ipynb=.nbconvert.ipynb)

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

%.png: %.uml Makefile
   java -Djava.awt.headless=true -jar plantuml.jar -p < $< > $@

%.html: %.nbconvert.ipynb Makefile jekyll.tpl
	ipython nbconvert --to html  --template jekyll.tpl --stdout $< > $@

%.v2.ipynb: %.nbconvert.ipynb
	ipython nbconvert --to notebook --nbformat 2 --stdout $< > $@

%.nbconvert.ipynb: %.ipynb
	ipython nbconvert --to notebook --ExecutePreprocessor.timeout=120 --execute --stdout $< > $@

notes.pdf: combined.ipynb Makefile
	ipython nbconvert --to pdf --template latex.tplx $<
	mv combined.pdf notes.pdf

combined.ipynb: $(EXECUTED)
	python nbmerge.py $^ $@

notes.tex: combined.ipynb Makefile
	ipython nbconvert --to latex --template latex.tplx $<
	mv combined.tex notes.tex

notebooks.zip: ${NBV2}
	zip -r notebooks $^

master.zip: Makefile
	rm -f master.zip
	wget https://github.com/UCL-RITS/indigo-jekyll/archive/master.zip

ready: indigo $(HTMLS) notes.pdf notebooks.zip

indigo-jekyll-master: Makefile master.zip
	rm -rf indigo-jekyll-master
	unzip master.zip
	touch indigo-jekyll-master

indigo: indigo-jekyll-master Makefile
	cp -r indigo-jekyll-master/indigo/images .
	cp -r indigo-jekyll-master/indigo/js .
	cp -r indigo-jekyll-master/indigo/css .
	cp -r indigo-jekyll-master/indigo/_includes .
	cp -r indigo-jekyll-master/indigo/_layouts .
	cp -r indigo-jekyll-master/indigo/favicon* .
	touch indigo

plantuml.jar:
	wget http://sourceforge.net/projects/plantuml/files/plantuml.jar/download -O plantuml.jar

.PHONY: ready

_site: ready
	jekyll build	

preview: ready
	jekyll serve

clean:
	rm -f session*/generated/*.png
	rm -rf session*/*.html
	rm -f session*/*.pyc
	rm -f index.html
	rm -rf _site
	rm -rf images js css _includes _layouts favicon* master.zip indigo-jekyll-master
	rm -f indigo
	rm -f session01/analyzer.py
	rm -f session01/eight
	rm -f session01/eight.py
	rm -rf session01/module1/
	rm -f session01/pretty.py
	rm -f session*/*.nbconvert.ipynb
	rm -rf session*/*.v2.ipynb
	rm -rf combined*
	rm -f notes.pdf
	rm -f notes.tex
	rm -f session04/greeter.py
	rm -f session04/map.png
	rm -f session05/anotherfile.py
	rm -f session05/config.yaml
	rm -f session05/context.py
	rm -f session06/fixed.png
	rm -f session07/datasource*.yaml
	rm -f session07/example.yaml
	rm -f notebooks.zip
