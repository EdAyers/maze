import random

from collections inport defaultdict

from maze import Goody, UP, DOWN, LEFT, RIGHT, STAY, PING, DX, DY

#some stuff shamelessly copied from http://www.redblobgames.com/pathfinding/a-star/implementation.html

import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

def neighbors(graph, pos):
    near = [pos + DX, pos - DX, pos + DY, pos - DY]
    return filter((lambda p: not graph[p]),near)

# to each node on the grid
# assign none if its unreachable
# assign none if the algorithm timed out 
# assign none if the algorithm hit the finish before the algorithm finished
# assign a point of l1length 1 to indicate one of the fastest routes from that node to the start node. 
def breadth_first_search(graph, start, finish):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    ttl = 100 * 100
    while (not frontier.empty()) and (ttl > 0):
        current = frontier.get()
        ttl--
        if (current == finish): break
        for next in neighbors(graph, current):
            if next not in came_from:
                frontier.put(next)
                delta = next - current
                came_from[next] = delta
    return came_from


class MemGoody(Goody):
    mymap = defaultdict(bool) # my understanding of the map
    pos = (0,0) # my current position relative to starting point
    route = [] # the sequence of up/down/left/right commands that I should follow 
    target = (0,0) # the point I'm trying to get to
    
    # return a point that I should try and get to
    def get_target():
        # IMPLEMENT ME!
        return (10,10)

    # return a list of UP, DOWN etc commands to get to target
    def get_route():
        # IMPLEMENT ME!
        return []

    def take_turn(self, obstructions, ping_request):
      
        #update mymap
        for (dir, isFree) in obstructions.items():
            if not isFree:
                self.mymap[self.pos] = true

        

        #update route if we pinged
        if ping_request:
            self.target = get_target(self,ping_request)
            self.route = get_route()

        if not route:
            self.route = get_route()

        next = self.route.pop()
        if (next == UP): self.pos -= DY
        if (next == DOWN): self.pos += DY
        if (next == RIGHT): self.pos -= DX
        if (next == LEFT): self.pos += DX
        return next