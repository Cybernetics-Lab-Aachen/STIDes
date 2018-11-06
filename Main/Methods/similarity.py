import numpy as np
import munkres as munk
from Main.Methods import PrePro as pre
from Main.Methods import settings


def get_similarity(matrix):
    """
    calculates the best matching between the two data set, by using the interval distance Matrix as input 
    :param matrix: quadratic or non quadratic interval distance matrix
    :return: List of matched intervals (tuples of indexes from the distance matrix), total similarity score and cardinality difference (if existing)
    """

    max_value = pre.max_value_in_lists(matrix)
    if settings.dummy_mode != 0:
        new_matrix = pre.dummy_fill(matrix)
    else:
        new_matrix = matrix
    if len(new_matrix) != len(new_matrix[0]):
        return -5, -5, -5
    m = munk.Munkres()
    n_matrix = np.copy(new_matrix)
    indexes = m.compute(n_matrix)

    total = 0
    for cur_index in indexes:
        total += new_matrix[cur_index[0]][cur_index[1]]

    if settings.dummy_mode == 0:
        return indexes, total
    elif settings.dummy_mode == 1:
        return indexes, (total -(abs(len(matrix)-len(matrix[0]))*max_value)), abs(len(matrix) - len(matrix[0]))
    elif settings.dummy_mode == 2:
        temp = 0
        if len(matrix) > len(matrix[0]):
            for i in indexes:
                if i[1] >= len(matrix[0]):
                    temp += settings.dummy_weight + pre.get_best_similarity_data1(matrix, i[0])
        elif len(matrix) < len(matrix[0]):
            for i in indexes:
                if i[0] >= len(matrix):
                    temp += settings.dummy_weight + pre.get_best_similarity_data2(matrix, i[1])
        return indexes, (total -(abs(len(matrix)-len(matrix[0]))*max_value) + temp), abs(len(matrix) - len(matrix[0]))
    else:
        return -1, -1, -1
