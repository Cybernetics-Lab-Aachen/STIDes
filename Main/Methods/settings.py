"""
needed Settings
"""

weight_l = 1                #Weight for length distance
weight_o = 1               #Weight for overlapping distance
weight_d = 1                #Weight for displacement distance
weight_s = 1                #Weight for start point distance
weight_e = 1                #Weight for end point distance

dummy_weight = 0            #dummy weighting factor as lower bound for changes in the similarity for each dummy node

dummy_mode = 2              #Settings regarding cardinality differences:
                                    # 0: basic STIDes without cardinality differences (not recommended)
                                    # 1: basic STIDes ignoring occuring cardinality differences
                                    # 2: recursive STIDes, punishing cardinality differences by dummy weight and secondary matching

STIDes_Mode = 0             #Setting for scaling or shifting:
                                    # 0: no shifting or scaling used
                                    # 1: enables shifting of the second data set
                                    # 2: enables scaling of the second data set