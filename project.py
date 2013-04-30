# Bismillahi-r-Rahmani-r-Rahim
# Rabbi zidni ilma
#
# Project a dataset using random projections

import sys
from sklearn.random_projection import SparseRandomProjection
from sklearn.datasets import load_svmlight_file, dump_svmlight_file


def project(file_name, dimensions):
    data = load_svmlight_file(file_name)
    projector = SparseRandomProjection(dimensions, 1/3.0,
                                       dense_output=True)
    projected = projector.fit_transform(data[0])
    
    new_file_name = file_name[:-4] + '-' + str(dimensions) + '.mat'
    new_file = open(new_file_name, 'wb')
    dump_svmlight_file(projected, data[1], new_file)

if __name__ == "__main__":
    dataset_file_name = sys.argv[1]
    assert dataset_file_name.endswith('.mat')
    dimensions = int(sys.argv[2])
    project(dataset_file_name, dimensions)
