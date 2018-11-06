from Main.Methods import similarity as st
from Main.Methods import PrePro as pre
from Main.Methods import settings
"""
We start with two interval data sets, with each Interval i = [s_i , e_i] as start point (s_i) and end point (e_i)
"""

def stides(data_set_1, data_set_2, mode):
    """
    starts the whole approach of STIDes-Similarity 
    :param data_set_1: First time interval data set
    :param data_set_2: Second time interval data set
    :param mode: Mode for STIDes ( 0 = Default, 1 := STIDes with shifting, 2:= STIDes with scaling)
    :return: Distanzvalue and corresponding shifting/scaling factor if used
    """
    if mode == 0:
        matrix = pre.distances(data_set_1, data_set_2, settings.weight_l, settings.weight_o, settings.weight_d , settings.weight_s, settings.weight_e)
        result = st.get_similarity(matrix)
        return result[1]
    elif mode == 1:
        result_shift = 0
        result = [-1,-1]
        factors = pre.get_shifting_factors(data_set_1, data_set_2)
        for i in factors:
            data_set_2_new = pre.shift_dataset(data_set_2, i)
            matrix = pre.distances(data_set_1, data_set_2_new, settings.weight_l, settings.weight_o, settings.weight_d , settings.weight_s, settings.weight_e)
            result_tmp = st.get_similarity(matrix)
            if result[1] == -1:
                result = result_tmp
                result_shift = i
            elif result[1] > result_tmp[1]:
                result = result_tmp
                result_shift = i
        return result[1], result_shift
    elif mode == 2:
        result_scale = 1
        result = [-1, -1]
        factors = pre.get_scaling_factors(data_set_1, data_set_2)
        for i in factors:
            data_set_2_new = pre.scale_dataset(data_set_2, i)
            matrix = pre.distances(data_set_1, data_set_2_new, settings.weight_l, settings.weight_o, settings.weight_d , settings.weight_s, settings.weight_e)
            result_tmp = st.get_similarity(matrix)
            if result[1] == -1:
                result = result_tmp
                result_scale = i
            elif result[1] > result_tmp[1]:
                result = result_tmp
                result_scale = i
        return result[1], result_scale

