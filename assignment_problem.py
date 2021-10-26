import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment

'''
https://en.wikipedia.org/wiki/Assignment_problem
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html


order of lists is important (eg, student 1 before student 2). in case of draw the preferences of the first list are preferred
student1    [3, 2, 1] -> student 1 prefers topic 3, then 2 and lastly the first topic (C > B > A)

example 1:
weight_of topic1 topic2 topic3
student1    [3, 2, 1], 
student2    [1, 3, 2], 
student3    [2, 1, 3]
->
array indizes of best solution: [2 0 1]
adjusted (plus one) array indizes of best solution: [3 1 2]

example 2:
not an issue, if more topics than students
[4,3,1,2], 
[2,4,1,3], 
[2,1,3,4], 
->
adjusted (plus one) array indizes of best solution: [3 1 2]


example 3:
if less topics than students, and each topic is assigned more than once:
list each topic accordingly to the number it is assigned. eg, topic1 can be chosen 4 times and topic2 3 times
[1,1,1,1,2,2,2]
[2,2,2,2,1,1,1]
'''

# import from xlxs file. ideally lists are sorted by grades. output to same xlsx

df = pd.read_excel(r"D:\Dokumente\WMA\Veranstaltungen\4 WissArbeiten\W21\Übersicht_Teilnehmer_Master-Thesis.xlsx")

preferences = [
    [4,3,1,2], 
    [2,4,1,3], 
    [2,1,3,4], 
    ]

cost = np.array(preferences)
row_ind, col_ind = linear_sum_assignment(cost)

print(f"array indizes of best solution: {col_ind}")
print(f"adjusted (plus one) array indizes of best solution: {col_ind+1}")
print(f"Total Sum of preferences (lowest sum possible): {cost[row_ind, col_ind].sum()}")

