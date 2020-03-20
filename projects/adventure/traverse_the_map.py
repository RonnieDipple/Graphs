
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


def unexplored_finder(room):
    for direction in room:
        if room[direction] == '?':
            return direction
    return None

def direction_finder(current_room, target_room_id):
    for direction in current_room:
        if current_room[direction] == target_room_id:
            return direction
    return None


# This is where the real logic is
def traverse_map_bfs(player):
    path = []
    starting_room = player.current_room.id
    graph = {}

    graph[starting_room] = {}
    for exits in player.current_room.get_exits():
        graph[starting_room][exits] = '?'

    # print(graph)
    directions = { 'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

    # while there are unexplored paths in graph
    while unexplored(graph):
        # print("graph", graph)
        current_room = player.current_room.id
        # print("current room", current_room)
        # check if current room has unexplored paths
        if '?' in graph[current_room].values():
        # if so,
            # find an unexplored direction from current room
            direction = unexplored_finder(graph[current_room])
            # print("direction", direction)
            # travel in that direction
            player.travel(direction)
            next_room = player.current_room.id
            # print("next room", next_room)
            # add direction to path
            path.append(direction)
            # add directions to graph (replace '?'s)
            graph[current_room][direction] = player.current_room.id
            if not next_room in graph:
                graph[next_room] = {}
                for exits in player.current_room.get_exits():
                    graph[next_room][exits] = '?'
            graph[next_room][directions[direction]] = current_room

        else:
        # if no paths left,
            # perform a bfs to find nearest room with unexplored path '?'

            # create empty queue
            q = Queue()
            # enqueue path to current room
            q.enqueue([current_room])
            # create empty visited set
            visited = set()

            # while the queue is not empty...
            while q.size() > 0:
                # dequeue path
                p = q.dequeue()
                # grab last room from path
                room = p[-1]

                direction = unexplored_finder(graph[room])

                # check if room has any unexplored exits
                if direction is not None:
                # if so,
                    # convert room ids in path to usable direction
                    for i in range(len(p) - 1):
                        d = direction_finder(graph[p[i]], p[i + 1])
                        # add directions to traversal path
                        path.append(d)
                        # move player to room using directions
                        player.travel(d)
                    # break loop
                    break

                else:
                    # check if room has been visited
                    if room not in visited:
                    # if not,
                        # mark as visited
                        visited.add(room)
                        # enqueue paths to neighboring rooms
                        for e in graph[room]:
                            p_copy = p.copy()
                            p_copy.append(graph[room][e])
                            q.enqueue(p_copy)

    return path
