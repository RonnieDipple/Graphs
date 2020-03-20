
# Standard Queue
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# returns bool of true if room is unexplored
def unexplored(graph):
    for room in graph:
        if '?' in graph[room].values():
            return True
    return False


# This is where the real logic is
# While unexplored is true do something
