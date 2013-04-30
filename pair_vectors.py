# Bismillahi-r-Rahmani-r-Rahim
#
# Extract hyponym-hypernym pairs from wordnet

from nltk.corpus import wordnet

from sklearn.feature_extraction import DictVectorizer
from sklearn.datasets import dump_svmlight_file

import json
import itertools
import collections
import sys
import os

from numpy import random
from scipy.sparse import vstack

def pair_vectors(pairs, features, words, output_path):
    vectorizer = DictVectorizer()
    vectors = vectorizer.fit_transform(x[1] for x in features)

    vector_map = {word:vector for word, vector in
                  itertools.izip((x[0].split('/')[0] for x in features),
                                 vectors)}

    # Positive examples
    positive = []
    record = []
    for specific, general in pairs:
        positive.append(vector_map[general] - vector_map[specific])
        record.append( (specific, general, 1) )

    pair_set = set([tuple(x) for x in pairs])
    non_positive = []
    for i in range(len(positive)):
        first = second = None
        while first == second or (first, second) in pair_set:
            first = words[random.randint(len(words))]
            second = words[random.randint(len(words))]
        non_positive.append(vector_map[second] - vector_map[first])
        record.append( (first, second, 0) )
    
    data = vstack(positive + non_positive)
    target = [1]*len(positive) + [0]*len(non_positive)
    
    # Save dataset
    with open(os.path.join(output_path,'wn-noun-dependencies.mat'), 'wb') as data_file:
        dump_svmlight_file(data, target, data_file)

    with open(os.path.join(output_path,'wn-noun-dependencies.json'), 'w') as record_file:
        json.dump(record, record_file)

if __name__ == "__main__":
    pair_path = sys.argv[1]
    dependency_path = sys.argv[2]
    output_path = sys.argv[3]

    lines = open(pair_path)
    pairs = [x.strip().split() for x in lines]
    print pairs[:5]
    words = {x[0] for x in pairs} | {x[1] for x in pairs}
    print words
    print len(words)

    vectors = open(dependency_path)
    parsed = (json.loads(line) for line in vectors)
    useful = [x for x in parsed if x[0].split('/')[0] in words]

    pair_vectors(pairs, useful, list(words), output_path)
