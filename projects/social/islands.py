# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west. For example:
from util import Stack

islands = [[0, 1, 0, 1, 0], # Currently not an adjacency matrix 1s are nodes , in an adjacency matrix rows nodes are rows and columns
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]

more_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]



# Groups of Islands are 1s aka connected components
# Below would be two islands, this is a simplified version of the one above
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]


# Plan


# Build your graph
def island_counter(matrix):
    # Create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0])) # False means it has been visited and len(matrix[0]) is the first row
    island_count = 0
    # Go through all nodes aka ones
    # For all nodes as we have a 2 dimensional array we will need 2 for loops :
    # matrix[0] returns a row at [0]
    for column in range(len(matrix[0])):
        # Then we are iterating over each column in that row at matrix[0]
        for row in range(len(matrix)):
            # If node is not visited:
            if not visited[row][column]:
                #If we hit a 1 that has not been visited
                if matrix [row][column] == 1:
                    # Mark visited
                    # increment visited count
                    # Traverse all CONNECTED nodes, marking as visited
                    visited = dft(row, column, matrix, visited)
                    island_count += 1
    return island_count

# Traverse your graph
def dft(start_row, start_column, matrix, visited):
    # Do a DF traversal

    # Create a stack
    s = Stack()
    # PUSH A PATH TO the starting vertex
    s.push((start_row, start_column))
    # While the stack is not empty....
    while s.size() > 0:
        # Pop the first PATH vertex
        v = s.pop()
        row = v[0]
        column = v[1]
        # Check if it has been visited
        # If it has not been visited..
        if not visited[row][column]:
            # Mark it as visited
            visited[row][column] = True
            # Push all of it's neighbors on to the stack
            for neighbor in get_neighbors(row, column, matrix):
                s.push(neighbor)
    # Visited is a 2d matrix
    return visited




def get_neighbors(row, column, matrix):
    '''
    Return a list of neighboring 1 tuples in the form [(row, col)]
    '''
    neighbors = []
    # Check North of 1 aka node in islands
    if row > 0 and matrix [row -1][column] == 1:
        neighbors.append((row - 1, column))
    # Check South
    if row < len(matrix)-1 and matrix[row + 1][column] == 1:
        neighbors.append((row + 1, column))
    # Check East
    if column < len(matrix[0]) -1 and matrix[row][column + 1] == 1:
        neighbors.append((row, column +1))
    # Check West
    if column > 0 and matrix[row][column - 1] == 1:
        neighbors.append((row, column -1))
    return neighbors

print(island_counter(islands)) # returns 4
print(island_counter(more_islands)) # returns 13

