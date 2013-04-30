# Bismillahi-r-Rahmani-r-Rahim
#
# Extract hyponym-hypernym pairs from wordnet

from nltk.corpus import wordnet
import itertools

import sys

def unambiguous(words):
    "Get a list of (mainly) unambiguous terms"
    for word in words:
        lemmas = wordnet.lemmas(word)
        counts = [x.count() for x in lemmas
                  if x.synset.pos == 'n']
        if len(counts) == 0:
            continue
        m = max(counts)
        if m == 0:
            continue
        p = float(m)/sum(counts)
        if m > 2 and p > 0.8:
            print word

if __name__ == "__main__":
    word_path = sys.argv[1]
    lines = open(word_path)
    words = itertools.imap(
        lambda x: x.strip(),
        lines)
    unambiguous(words)
