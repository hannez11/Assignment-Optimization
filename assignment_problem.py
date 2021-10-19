import numpy as np
from scipy.optimize import linear_sum_assignment

'''
https://en.wikipedia.org/wiki/Assignment_problem
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html


order of lists is important. in case of draw the preferences of the first list are preferred
student1    [3, 2, 1] -> student 1 prefers topic 3, then 2 and lastly the first topic (C > B > A)

weight topic1 topic2 topic3
student1    [3, 2, 1], 
student2    [1, 3, 2], 
student3    [2, 1, 3]

array indizes of best solution: [2 0 1]

'''

# import from xlxs file. ideally lists are sorted by grades. output to same xlsx

preferences = [
    [3, 2, 1], 
    [3, 2, 1], 
    [2, 1, 3]
    ]

cost = np.array(preferences)
row_ind, col_ind = linear_sum_assignment(cost)

print(f"array indizes of best solution: {col_ind}")
print(f"adjusted (plus one) array indizes of best solution: {col_ind+1}")
print(f"Total Sum of preferences (lowest sum possible): {cost[row_ind, col_ind].sum()}")

