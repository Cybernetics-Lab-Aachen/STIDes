from Methods import STIDes as st
from Methods import PrePro as pre


"""needed Settings"""

weight_l = 1                #Weight for length distance
weight_o = 1                #Weight for overlapping distance
weight_d = 1                #Weight for displacement distance
weight_s = 1                #Weight for start point distance
weight_e = 1                #Weight for end point distance
weight_Start = 0            #Weight for start  deadline
weight_End = 0              #Weight for end deadline
dummy_weight = 0            #dummy wtighting factor for cardinality differences

"""
We start with two interval data sets, with each Interval i = [s_i , e_i] as start point (s_i) and end point (e_i)
"""

P = [[1,2],[4,5],[8,10]]
Q = [[0,1],[4,5],[9,11]]

"""
"""
matrix = [[10,1,10],[1,10,3]]
result = st.get_similarity_diff_card(matrix)
print(result[1])
print(' ')
pre.print_matrix(matrix)
result = st.get_similarity_dummy(matrix, 0)
print(' ')
print(result[1])


