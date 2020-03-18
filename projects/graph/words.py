# Given two words (begin_word and end_word),
# and a dictionary's word list,
# return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

# HOW TO SOLVE ANY GRAPH PROBLEM
# 1 UNDERSTAND THE PROBLEM
# IS IT ACYCLIC OR CYCLIC?(THIS IS CYCLIC)
# EXAMPLE OF A CYCLE BAT -> BAN -> BIN -> BIT -> BAT SEE HOW IT CYCLES AROUND TO BAT
# THIS IS SPARSE ONE WORD ONLY TO A SMALL NUMBER OF OTHER WORDS

# 2 BUILD YOUR GRAPH
# 3 TRAVERSE YOUR GRAPH


from util import Queue, Stack
import string

# 2 BUILD YOUR GRAPH

# Load words from words.txt which is a dictionary of words
f = open('words.txt', 'r')
word_set = set(f.read().lower().split("\n"))  # set Makes it O(1) look up
f.close()  # this prevents the file from being auto closed immediately


def get_neighbors(word):
    '''Get all words that are one letter
    away from the given word'''
    # Get words of the same length as word above
    results = []
    list_word = list(word)  # makes w1 a list so it can be looped through
    # Go through each letter in the word
    for i in range(len(list_word)):
        # Swap each letter with a letter in the alphabet
        for letter in string.ascii_lowercase:  # Which is the same as for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            # 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            # If resulting word is in the word_set, add to results
            temp_word = list_word.copy()
            temp_word[i] = letter
            joined_word = "".join(temp_word)
            if joined_word in word_set and joined_word != word:
                results.append(joined_word)
    return results


# Create a counter that breaks if it goes higher than one and while loop through comparing
# Go through each word and build an adjacency list with each word one letter away
# Create a function that while check if two neighbors are equal/neighbors
# def words_are_neighbors(w1, w2):
#     '''return True if words are one letter apart'''
#     '''And False otherwise'''
#     list_word = list(w1) #makes w1 a list so it can be looped through
#     # Go through each letter in the word
#     for i in range(len(list_word)):
#     # swap with each letter in the alphabet
#         for letter in  string.ascii_lowercase: # Which is the same as for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#                                                 # 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
#             # Check if that equals given word
#             temp_word = list_word.copy()
#             temp_word[i] = letter
#             if "".join(temp_word) == w2:
#                 return True
#     return False

# If after deleteing one letter we get two matching strings, the left and the right side that means we have a match of True
# def words_are_neighbors(w1, w2):
    # Base case if word1 aka w2 does not equal the same length as word2 aka w2
    # Then it is not the same word with one letter changed so it returns False
    # if len(w1) != len(w2):
    #     return False
    # As the word is the same length
    # i iterates through word1 aka w1
    # as it does that it compares w1 letter in position i with w2 letter in position i,
    # w1[:i] means it is comparing the letters in 0 to position i with w2[:i] letters 0 to position i
    # and also w1 letter in position 1 +1 with w2 letter in position i + 1 so it is comparing 1 ahead
    # w1[i + 1:] means it is comparing the letters in position i + 1 until the end of w1
    # with the letters in w2[i + 1:] which is also the letters in position i + 1 until the end (basically chopping the ends off)
    # if they do not match then they are not neighbors and so it returns False and if they do match then it returns True
#     for i in range(len(w1)):
#         if w1[:i] == w2[:i] and w1[i + 1:] == w2[i + 1:]:
#             return True
#     return False
#
#
# # This version of words_are_neighbors(w1,w2) is more readable and works as well
# def words_are_neighbors(w1, w2):
#     # iterates aka loops through to the end of word1 aka w1
#     for i in range(len(w1)):
#         # Then makes a list out of w1 and w2 so if the w1 was the word dog
#         # then list_word1 = list(w1) would be the equivilent of list_word1 = [d, o, g]
#         list_word1 = list(w1)
#         list_word2 = list(w2)
#         # making it easier to pop letters off
#         # as this is in a for loop it goes through popping letters off
#         list_word1.pop(i)
#         list_word2.pop(i)
#         # and compares the words as it pops of the letter
#         # if they remain the same then it returns True
#         if list_word1 == list_word2:
#             return True

# # An adjacency list
# neighbors = {}
# # Goes through each word
# for word in words:
#     neighbors[word] = set()
#     # Go through each potential neighbor
#     for potential_neighbor in words:
#         # Add to neighbors if they match
#         if words_are_neighbors(word, potential_neighbor):
#             neighbors[word].add(potential_neighbor)

# def get_neighbors(word):
#     return neighbors[word]


# 3 TRAVERSE YOUR GRAPH
def word_ladder(begin_word, end_word):
    # This algorithm should be used and memorized
    # Create a queue
    q = Queue()
    # Enqueue the starting vertex aka word
    q.enqueue([begin_word])  # IT IS A PATH SO AN ARRAY IS NEEDED
    # Create a set to store visited vertices
    visited = set()
    # While the queue is not empty....
    while q.size() > 0:
        # Dequeue PATH
        path = q.dequeue()
        # GRAB THE LAST WORD FROM THE PATH
        w = path[-1]  # this is python syntax for counting backwards
        # CHECK IF IT IS THE TARGET WORD
        if w == end_word:
            # IF IT IS, RETURN PATH
            return path
        # Check if it has been visited
        # If it has not been visited.....
        # THEN Mark it as visited
        if w not in visited:
            visited.add(w)
            # Enqueue A PATH TO all of it's neighbors AKA Enqueue A PATH TO EACH NEIGHBORING WORD
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)






# BELOW IS THE VERSION COPIED FROM GRAPH.PY AND ABOVE IS AN ADAPTATION OF THAT
# def bfs(self, starting_vertex, destination_vertex):
#     """
#     Return a list containing the shortest path from
#     starting_vertex to destination_vertex in
#     breath-first order.
#     """
#     # This algorithm should be used and memorized
#     # Create a queue
#     q = Queue()
#     # Enqueue A PATH TO the starting vertex
#     q.enqueue([starting_vertex])  # IT IS A PATH SO AN ARRAY IS NEEDED
#     # Create a set to store visited vertices
#     visited = set()
#     # While the queue is not empty....
#     while q.size() > 0:
#         # Dequeue the first PATH vertex
#         path = q.dequeue()
#         # GRAB THE VERTEX FROM THE END OF THE PATH
#         v = path[-1]  # this is python syntax for counting backwards
#         # Check if it has been visited
#         # If it has not been visited.....
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
#                 # ENQUEUE THE COPY
#                 q.enqueue(path_copy)

#######################TESTING###################################
print("HERE")
print(word_ladder("sail", "boat"))
print("END")
