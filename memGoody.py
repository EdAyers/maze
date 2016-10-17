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

# finds a route between start and finish given a defaultdict(bool)
def breadth_first_search(graph, start, finish):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
        if (current == finish): break
        for next in neighbors(graph, current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    current = finish
    route = [] 
    while not (current == start):
      current = came_from[current]
      route.append(current)     
    return route

class MemGoody(Goody):
    mymap = defaultdict(bool)
    pos = (0,0)

    def take_turn(self, obstructions, ping_request):
      
        #update mymap
        for (dir, isFree) in obstructions.items():
            if not isFree:
                self.mymap[self.pos] = true

        #update route if we pinged
        if ping_request:
            self.target = get_target(self,ping_request)
            self.route = get_route(self)

        if not route:
            self.route = get_route(self)

        next = self.route.pop()
        if (next == UP): self.pos -= DY
        if (next == DOWN): self.pos += DY
        if (next == RIGHT): self.pos -= DX
        if (next == LEFT): self.pos += DX
        return next