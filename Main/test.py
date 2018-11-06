from Main.Methods import STIDes as st
from Main.Methods import PrePro as pre
from Main.Methods import settings
"""
We start with two interval data sets, with each Interval i = [s_i , e_i] as start point (s_i) and end point (e_i)
"""

P = [[1,2], [4,5], [8,10] ]
Q = [[0,1], [4,5], ]

print(P)
print(Q)
matrix = pre.distances(P, Q, settings.weight_l, settings.weight_o, settings.weight_d, settings.weight_s, settings.weight_e)

pre.print_matrix(matrix)

print("HAHAHAHA")
new_matrix = pre.dummy_fill(matrix)

pre.print_matrix(new_matrix)
#result = st.get_similarity_diff_card(matrix)
#print(result[1])
#print(' ')
#pre.print_matrix(matrix)
#result = st.get_similarity_dummy(matrix, 0)
#print(' ')
#print(result[1])


