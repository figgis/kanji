TEXFILE = kanji.tex

main:
	./make_kanji.py > $(TEXFILE)
	xelatex $(TEXFILE)

copy:
	cp $(TEXFILE:.tex=.pdf) ../doc/jpn.pdf

view:
	evince $(TEXFILE:.tex=.pdf) &

clean :
	rm -f $(TEXFILE:.tex=*) *~ *.pyc


