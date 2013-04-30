# Bismillahi-r-Rahmanir-Rahim
# Rabbi Zidni ilma
#
# Create random vectors using wordnet classifications, as a baseline


import sys
import json

from sklearn.random_projection import SparseRandomProjection
from sklearn.datasets import load_svmlight_file, dump_svmlight_file
from numpy import random

from scipy.sparse import vstack

def baseline(pairs, dimensions):
    words = set(p[0] for p in pairs) | set(p[1] for p in pairs)
    vectors = {w: random.random_sample(dimensions) for w in words}
    #print vectors
    data = []
    for p in pairs:
        pair_vector = vectors[p[1]] - vectors[p[0]]
        data.append(pair_vector)
    target = [p[2] for p in pairs]
    return data, target

if __name__ == "__main__":
    pairs = json.load(open(
            '/home/daoud/Documents/conewordnetdata/wn-noun-dependencies.json'))
    dimensions = int(sys.argv[1])
    data, target = baseline(pairs, dimensions)
    
    file_name = '/home/daoud/Documents/conewordnetdata/wn-noun-dependencies-random-%d.mat' % dimensions
    with open(file_name, 'wb') as data_file:
        dump_svmlight_file(data, target, data_file)




# def project(file_name, dimensions):
#     data = load_svmlight_file(file_name)
#     shape = (data[0].shape[0], dimensions)
#     print "Creating data with shape: ", str(shape)
#     random_data = random.random_sample(shape[0]*shape[1])*2 - 1
#     random_data = random_data.reshape(shape)
    
#     new_file_name = file_name[:-4] + '-random-' + str(dimensions) + '.mat'
#     new_file = open(new_file_name, 'wb')
#     dump_svmlight_file(random_data, data[1], new_file)

# if __name__ == "__main__":
#     dataset_file_name = sys.argv[1]
#     assert dataset_file_name.endswith('.mat')
#     dimensions = int(sys.argv[2])
#     project(dataset_file_name, dimensions)
