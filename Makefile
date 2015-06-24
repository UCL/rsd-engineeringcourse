PANDOC=pandoc

ROOT=""

PANDOCARGS=-t revealjs -s -V theme=night --css=http://lab.hakim.se/reveal-js/css/theme/night.css \
					 --css=$(ROOT)/css/ucl_reveal.css --css=$(ROOT)/site-styles/reveal.css \
           --default-image-extension=png --highlight-style=zenburn --mathjax -V revealjs-url=http://lab.hakim.se/reveal-js

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
	plantuml -p < $< > $@

%.html: %.ipynb Makefile jekyll.tpl
	ipython nbconvert --to html --template jekyll.tpl --execute --stdout $< > $@

%.html: %.ipyhtml Makefile
	yamlheader 

remaster.zip: Makefile
	rm -f remaster.zip
	wget https://github.com/UCL-RITS/indigo-jekyll/archive/remaster.zip

indigo-jekyll-remaster: Makefile remaster.zip
	rm -rf indigo-jekyll-remaster
	unzip remaster.zip
	touch indigo-jekyll-remaster

indigo: indigo-jekyll-remaster Makefile
	cp -r indigo-jekyll-remaster/indigo/images .
	cp -r indigo-jekyll-remaster/indigo/js .
	cp -r indigo-jekyll-remaster/indigo/css .
	cp -r indigo-jekyll-remaster/indigo/_includes .
	cp -r indigo-jekyll-remaster/indigo/_layouts .
	cp -r indigo-jekyll-remaster/indigo/favicon* .
	touch indigo

_site: indigo \
	     session01/01data.html session01/03control.html session01/04functions.html \
			 session01/05modules.html session01/00pythons.html session01/02types.html \
			 session01/06exercise.html
	jekyll build	

clean:
	rm -f session*/generated/*.png
	rm -rf session*/*.html
	rm -f index.html
	rm -rf _site
	rm -rf images js css _includes _layouts favicon* remaster.zip indigo-jekyll-remaster

