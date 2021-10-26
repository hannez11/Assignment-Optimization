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
adjusted (plus one) array indices of best solution: [3 1 2]

S1 gets topic3, S2 gets topic 1, S3 gets topic 2

example 2:

not an issue, if more topics than students

[4,3,1,2], 

[2,4,1,3], 

[2,1,3,4], 

->

adjusted (plus one) array indices of best solution: [3 1 2]

example 3:
if less topics than students, and each topic is assigned more than once:
list each topic accordingly to the number it is assigned. eg, topic1 can be chosen 4 times and topic2 3 times
[1,1,1,1,2,2,2]
[2,2,2,2,1,1,1]
