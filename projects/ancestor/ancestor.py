from util import Stack

# Write a function that, given the dataset and the ID of an individual in the dataset,
# returns their earliest known ancestor – the one at the farthest distance from the input individual.
# If there is more than one ancestor tied for "earliest",
# return the one with the lowest numeric ID. If the input individual has no parents, the function should return -
ancestor_set = set()
def get_neighbors(ancestor):
    '''Get all words that are one letter
    away from the given word'''
    # Get words of the same length as word above
    results = []
    list_ancestor = list(ancestor)  # makes w1 a list so it can be looped through
    # Go through each letter in the word
    for i in range(len(list_ancestor)):
        # Swap each letter with a letter in the alphabet
        for letter in string.ascii_lowercase:  # Which is the same as for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            # 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            # If resulting word is in the word_set, add to results
            temp_word = list_ancestor.copy()
            temp_word[i] = letter
            joined_word = "".join(temp_word)
            if joined_word in ancestor_set and joined_word != ancestor:
                results.append(joined_word)
    return result


def earliest_ancestor(ancestor, starting_node):
    # This algorithm should be used and memorized
    # Create a stack
    s = Stack()
    # PUSH A PATH TO the starting vertex
    s.push([starting_node])  # IT IS A PATH SO AN ARRAY IS NEEDED
    # Create a set to store visited vertices
    visited = set()
    # While the stack is not empty....
    while s.size() > 0:
        # Pop the first PATH vertex
        path = s.pop()
        # GRAB THE VERTEX FROM THE END OF THE PATH
        v = path[-1]  # this is python syntax for counting backwards
        # Check if it has been visited
        # If it has not been visited..
        if v not in visited:
            # Mark it as visited
            visited.add(v)
            # CHECK IF IT IS THE TARGET
            if v == ancestor:
                # IF SO, RETURN THE PATH
                return path
            # Enqueue A PATH TO all of it's neighbors
            for neighbor in self.get_neighbors(v):
                # MAKE A COPY OF THE PATH
                path_copy = path.copy()  # pass by reference not value
                path_copy.append(neighbor)
                # PUSH THE COPY
                s.push(path_copy)

# def dfs(self, starting_vertex, destination_vertex):
#     """
#     Return a list containing a path from
#     starting_vertex to destination_vertex in
#     depth-first order.
#     """
#     # This algorithm should be used and memorized
#     # Create a stack
#     s = Stack()
#     # PUSH A PATH TO the starting vertex
#     s.push([starting_vertex]  )# IT IS A PATH SO AN ARRAY IS NEEDED
#     # Create a set to store visited vertices
#     visited = set()
#     # While the stack is not empty....
#     while s.size( )> 0:
#         # Pop the first PATH vertex
#         path = s.pop()
#         # GRAB THE VERTEX FROM THE END OF THE PATH
#         v = path[-1  ]# this is python syntax for counting backwards
#         # Check if it has been visited
#         # If it has not been visited..
#         if v not in visited:
#             # Mark it as visited
#             visited.add(v)
#             # CHECK IF IT IS THE TARGET
#             if v == destination_vertex:
#                 # IF SO, RETURN THE PATH
#                 return path
#             # Enqueue A PATH TO all of it's neighbors
#             for neighbor in self.get_neighbors(v):
#                 # MAKE A COPY OF THE PATH
#                 path_copy = path.copy()  # pass by reference not value
#                 path_copy.append(neighbor)
#                 # PUSH THE COPY
#                 s.push(path_copy)





