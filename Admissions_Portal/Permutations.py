#   Create all matrices, which are permutations of the rows of A, and select the best time(Shortest time)
from itertools import permutations

#   A weighted adjacency matrix, A representing the time traveled by the driver, assuming time is measured in minutes
A = [
    [0, 15, 50, 40, 10],
    [15, 0, 22, 27, 45],
    [50, 22, 0, 20, 55],
    [40, 27, 20, 0, 25],
    [10, 45, 55, 25, 0]
]

#   The first row A[0] represents his starting point so should not be changed
#   Hence, permutations of the four rows

permutable_rows = [1, 2, 3, 4]

#   Forming list of permutated rows
permutated_rows = list(permutations(permutable_rows))


#   Finding the time of each possible route
def find_time(rows):
    for route in rows:
        path = []
        time = 0
        i = 0
        for j in route:
            time += A[i][j]  # i represents starting point
            i = j

    time += A[i][0]  # Adding up the time moved to each location
    return time


#   Finding the route with the shortest possible time
def find_shortest_time(rows):
    best_time = 0  # A variable that would be used to compare the time
    for event in rows:
        current_time = find_time(rows)

        if current_time > best_time:
            best_time = current_time

    return best_time


#   Function to show the route taken
def show_route(rows):
    count = 1
    for route in rows:
        path = []
        i = 0
        for j in route:
            path.append(f'A{i}{j}')
            i = j
        path.append(f'A{i}0')
        print(f"route {count}: {path[0]} + {path[1]} + {path[2]} + {path[3]} + {path[4]}")
        count += 1


#   Function to show the new matrix based on the route taken taken
def show_matrices(perms):
    for path in perms:
        matrix = []
        matrix.append(A[0])
        for loc in path:
            matrix.append(A[loc])
        for row in matrix:
            print(row)
        print()


print('The matrices of the possible routes are:')
show_matrices(permutated_rows)
print('*\n')
print('The possible routes are:')
show_route(permutated_rows)
print('\n')
print('The shortest route takes a time of', find_shortest_time(permutated_rows), 'minutes.')
