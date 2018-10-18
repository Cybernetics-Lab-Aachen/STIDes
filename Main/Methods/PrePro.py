def dummy_fill(matrix):
    """
    For cardinality differences the smaller data set (represented by rows and columns) is filled with the max. occurring
     interval similarity to ensure a quadratic matrix
    :param matrix: the non quadratic distance matrix for the interval distances
    :return: inflated quadratic distance matrix to use in the hungarian algorithm
    """
    new_matrix = []
    max_value = max_value_in_lists(matrix)
    if len(matrix) != len(matrix[0]):
        new_size = max(len(matrix), len(matrix[0]))

        for i in range(new_size):
            current_row = []
            for j in range(new_size):
                current_row.append(max_value)
            new_matrix.append(current_row)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[i][j] = matrix[i][j]

    else:
        new_matrix = matrix

    return new_matrix


def distances(data_set_1, data_set_2, weight_l, weight_o, weight_d , weight_s, weight_e):
    """
    generating the interval distance matrix
    :param data_set_1: time interval data set one
    :param data_set_2: time interval data set two
    :param weight_l: Weighting factor regarding the length
    :param weight_o: weighting factor regarding overlapping 
    :param weight_d: weighting factor regarding the distance
    :param weight_s: weighting factor regarding start point distance 
    :param weight_e: weighting factor regarding end point distance
    :return: Interval distance matrix, where M[i,j] means distance between interval i (data set 1) and j (data set 2)
    """
    result_matrix = []
    for interval_i in data_set_1:
        for interval_j in data_set_2:
            try:
                S = 0
                D = 0
                s_1 = interval_i[0]
                e_1 = interval_i[1]
                s_2 = interval_j[0]
                e_2 = interval_j[1]

                G = abs(max(e_1, e_2) - min(s_1, s_2))
                if max(s_1, s_2) < min(e_1, e_2):
                    S = min(e_1, e_2) - max(s_1, s_2)
                else:
                    D = min(abs(s_1 - e_2), abs(s_2 - e_1))

                result_matrix[interval_i][interval_j] = weight_l * (1 - (float(min((e_1 - s_1), (e_2 - s_2))) / float(max((e_1 - s_1), (e_2 - s_2))))) + weight_s * float(abs(s_2 - s_1)) / float(G) + weight_e * float(abs(e_2 - e_1)) / float(G) + weight_d * float(D) / float(G) + weight_o * (1 - (float(S) / float(min(float(abs(e_2 - s_2)), float(abs(e_1 - s_1))))))
            except: print("error")
    return result_matrix


def get_shifting_factors(data_set_1, data_set_2):
    """
    Gets potential parameters for shifting purposes
    :param data_set_1: time interval data set one
    :param data_set_2: time interval data set two
    :return: a list of factors, which are the candidates to map on the global minimum of distance
    """
    shifting_factors = []
    for interval_i in data_set_1:
        for interval_j in data_set_2:
            s_1 = interval_i[0]
            e_1 = interval_i[1]
            s_2 = interval_j[0]
            e_2 = interval_j[1]
            factor_1 = s_1 - e_2
            factor_2 = s_1 - s_2
            factor_3 = e_1 - e_2
            factor_4 = e_1 - s_2
            if factor_1 not in shifting_factors:
                shifting_factors.append(factor_1)
            if factor_2 not in shifting_factors:
                shifting_factors.append(factor_2)
            if factor_3 not in shifting_factors:
                shifting_factors.append(factor_3)
            if factor_4 not in shifting_factors:
                shifting_factors.append(factor_4)
    return shifting_factors


def get_scaling_factors(data_set_1, data_set_2):
    """
    Gets potential parameters for scaling purposes
    :param data_set_1: time interval data set one
    :param data_set_2: time interval data set two
    :return: a list of factors, which are the candidates to map on the global minimum of distance
    """
    scaling_factors = []
    for interval_i in data_set_1:
        for interval_j in data_set_2:
            s_1 = interval_i[0]
            e_1 = interval_i[1]
            s_2 = interval_j[0]
            e_2 = interval_j[1]
            factor_1 = e_1 / s_2
            factor_2 = s_1 / s_2
            factor_3 = e_1 / e_2
            factor_4 = s_1 / e_2
            factor_5 = (e_1 - s_1)/(e_2 - s_2)
            if factor_1 not in scaling_factors:
                scaling_factors.append(factor_1)
            if factor_2 not in scaling_factors:
                scaling_factors.append(factor_2)
            if factor_3 not in scaling_factors:
                scaling_factors.append(factor_3)
            if factor_4 not in scaling_factors:
                scaling_factors.append(factor_4)
            if factor_5 not in scaling_factors:
                scaling_factors.append(factor_4)
    return scaling_factors


def print_matrix(matrix):
    for row in matrix:
        print(row)


def max_value_in_lists(matrix):
    return max([max(sublist) for sublist in matrix])


def get_best_similarity_data1(matrix, rows):
    result = min(matrix[rows])
    return result


def get_best_similarity_data2(matrix, columns):
    result = min([i[columns] for i in matrix])
    return result