# Bismillahi-r-Rahmani-r-Rahim

# Make sklearn vector data from vector text file and wordnet

VECTORS = /home/daoud/Documents/conewordnetdata/vectors_1000
DATA = /home/daoud/Documents/conewordnetdata/data

VPATH = $(DATA)

default: wn-noun-dependencies-10.mat wn-noun-dependencies-100.mat

wn-noun-dependencies-10.mat wn-noun-dependencies-100.mat: wn-noun-dependencies.mat project.py
	( python project.py $(DATA)/wn-noun-dependencies.mat 10 )
	( python project.py $(DATA)/wn-noun-dependencies.mat 100 )

wn-noun-dependencies.mat: pairs dependencies.json pair_vectors.py
	( python pair_vectors.py $(DATA)/pairs $(DATA)/dependencies.json $(DATA) )

dependencies.json: vectors.py $(VECTORS)
	( python vectors.py $(VECTORS) > $(DATA)/dependencies.json )

pairs: unambiguous pairs.py
	( python pairs.py $(DATA)/unambiguous > $(DATA)/pairs )

unambiguous: words unambiguous.py
	( python unambiguous.py $(DATA)/words > $(DATA)/unambiguous )

words: $(VECTORS)
	( grep '/N' $(VECTORS) | cut -d/ -f1 > $(DATA)/words )

clean:
	( rm $(DATA)/* )