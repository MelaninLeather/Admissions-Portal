from itertools import permutations
#Create all matrices which are permutation spf the rows of A
A=[[0,15,50,22,10],[15,0,45,27,40],[50,45,0,55,20],[22,27,55,0,25],[10,40,20,25,0]]
permutations=list(permutations(A))

print(permutations[0])
print(permutations[1])
print(permutations[2])
print(permutations[3])
#permutations of [A][[2]]
B=permutations[1]
#using the off diagonal to find another route
for i in range(len(B)):
    for j in range(len(B)):
        total_time=

#
#     off_diagonal_of_B=[B[i][j]]


# perm = permutations(
#     [[0, 15, 20, 40, 10], [15, 0, 22, 27, 45], [50, 22, 0, 20, 55], [40, 27, 20, 0, 25], [10, 45, 55, 25, 0]],5)
#
# matrix = list(perm)
# print(len(matrix))
#
# for i in matrix:
#     print(i)