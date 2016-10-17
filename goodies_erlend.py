'''
    goodies_erlend.py
'''

from maze import Goody, UP, LEFT, DOWN, UP, STAY, PING

import random

from maze import Goody, UP, DOWN, LEFT, RIGHT, STAY, PING

class StaticGoody(Goody):
    ''' A static goody - does not move from its initial position '''

    def take_turn(self, _obstruction, _ping_response):
        ''' Stay where we are '''
        return STAY

class RandomGoody(Goody):
    ''' A random-walking goody '''

    def take_turn(self, obstruction, _ping_response):
        ''' Ignore any ping information, just choose a random direction to walk in, or ping '''
        possibilities = filter(lambda direction: not obstruction[direction], [UP, DOWN, LEFT, RIGHT]) + [PING]
        return random.choice(possibilities)
		
class ErlendGoody(Goody):
	def __init__

class FirstGoody(Goody):
    '''A first try at implementing a goody'''
    def take_turn(self, _obstruction, _ping_response):
        def distance(pos):
            return abs(pos[0]) + abs(pos[1])
        if _ping_response == None:
            
        else: 
            players = keys(_ping_response)
            baddy = next(player for player in players if isinstance(player, Baddy))
            other_goody = next(player for player in players if isinstance(player, Goody) and player != self)
            #If baddy comes too close, move in opposite direction
            if distance(_ping_response[baddy]) < 4:
				if _ping_response[baddy][0]