# Bismillahi-r-Rahmani-r-Rahim
#
# Extract hyponym-hypernym pairs from wordnet

from nltk.corpus import wordnet

import itertools
import collections
import sys

def pairs(words):
    "Find hyponym/hypernym pairs from a set of words"
    # For each word, find its most common sense
    senses = []
    sense_map = collections.defaultdict(lambda:[])
    for word in words:
        lemmas = wordnet.lemmas(word)
        nouns = [l for l in lemmas if l.synset.pos == 'n']
        counts = [l.count() for l in nouns]
        #print counts
        #print nouns
        best = max(nouns, key=lambda x:x.count())
        #print best, best.synset
        sense_map[best.synset.name].append(word)
        senses.append(best.synset)

    #print max([len(x) for x in sense_map.values()])

    #Take out "entity" as it's too general
    sense_set = {s.name for s in senses} - set(['entity.n.01'])
    for word, sense in zip(words, senses):
        hypernyms = list(sense.closure(lambda x:x.hypernyms()))
        common = {h.name for h in hypernyms} & sense_set
        if len(common) > 0:
            for c in common:
                for w in sense_map[c]:
                    print word, w
            #print word, common, [sense_map[x] for x in common]

if __name__ == "__main__":
    lines = open(sys.argv[1])
    words = [x.strip() for x in lines]
    pairs(words)
