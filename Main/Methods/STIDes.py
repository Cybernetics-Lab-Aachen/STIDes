import numpy as np
import munkres as munk
from Main.Methods import PrePro as pre


def get_similarity(matrix):
    """
    calculates the best matching between the two data set, by using the interval distance Matrix as input 
    :param matrix: quadratic interval distance matrix
    :return: List of tuples of indexes, which indicates the matching of Intervals as well es the total similarity score.
    """
    m = munk.Munkres()
    n_matrix = np.copy(matrix)
    indexes = m.compute(n_matrix)

    total = 0
    for cur_index in indexes:
        total += matrix[cur_index[0]][cur_index[1]]

    return indexes, total


def get_similarity_diff_card(matrix):
    """
    basic consideration of cardinality differences by using non quadratic interval distance Matrices as input.
    :param matrix: (non quadratic) interval distance matrix
    :return: List of matched intervals (tuples of indexes from the distance matrix), total similarity score and cardinality difference
    """
    max_value = pre.max_value_in_lists(matrix)
    new_matrix = pre.dummy_fill(matrix)
    result = get_similarity(new_matrix)

    return result[0], (result[1]-(abs(len(matrix)-len(matrix[0]))*max_value)), abs(len(matrix) - len(matrix[0]))


def get_similarity_dummy(matrix, dummy_weight):
    """
    "two turn similarity" of non quadratic matrices by using punishing cardinality differences statical and depending on the interval distances
    :param matrix: (non quadratic) interval distance matrix
    :param dummy_weight: static punishing input for the cardinality difference
    :return: List of matched intervals (tuples of indexes from the distance matrix), total similarity score and cardinality difference
    """
    temp = 0
    result = get_similarity_diff_card(matrix)
    if len(matrix) > len(matrix[0]):
        for i in result[0]:
            if i[1] >= len(matrix[0]):
                temp += dummy_weight + pre.get_best_similarity_data1(matrix, i[0])
    elif len(matrix) < len(matrix[0]):
        for i in result[0]:
            if i[0] >= len(matrix):
                temp += dummy_weight + pre.get_best_similarity_data2(matrix, i[1])
    return result[0], (result[1] + temp), result[2]

