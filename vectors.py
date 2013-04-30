# Bismillahi-r-Rahmani-r-Rahim
#
# Convert term vectors to scikit learn format

import json
import sys

def get_features(line):
    split = line.split()
    word = split[0]
    features = {}
    for i in range(1, len(split),2):
        #print split[i], split[i+1]
        features[split[i]] = float(split[i+1])
    return word, features

def dependencies(data):
    for line in data:
        word, features = get_features(line)
        features = {x[0]:x[1] for x in features.iteritems()
                    if not x[0].startswith('T:')
                    and not x[0].startswith('__')}
        print json.dumps([word, features])

    

if __name__ == '__main__':
    f = open(sys.argv[1])
    dependencies(f)
