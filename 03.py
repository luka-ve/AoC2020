import numpy as np
from math import ceil, prod


def part1(data):
    forest, width, height = construct_binary_forest(data)

    stride = (1, 3)
    n_trees = 0

    for row in range(0, forest.shape[0], stride[0]):
        n_trees = n_trees + forest[row, (row * stride[1]) % width]

    return n_trees


def part2(data):
    forest, width, height = construct_binary_forest(data)

    strides = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    n_trees = []

    for stride in strides:
        _trees = 0

        for row in range(0, ceil(forest.shape[0] / stride[0]), 1):
            _trees = _trees + forest[row * stride[0], (row * stride[1]) % width]

        n_trees.append(_trees)

    print(n_trees)

    return prod(n_trees)


def construct_binary_forest(data):
    forest = np.array(data.split())

    width = len(forest[0])
    height = len(forest)

    forest = ''.join(forest)
    forest_binary = [x == '#' for x in forest]

    forest_binary = np.reshape(np.array(forest_binary), (height, width))

    return (forest_binary, width, height)
