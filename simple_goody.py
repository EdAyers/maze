

from maze import Goody, UP, LEFT, DOWN, RIGHT, STAY, PING

class SimpleGoody(Goody):

    def take_turn(self, _obstruction, _ping_response):
        if _ping_response:
            players = _ping_response.keys()
            baddy = next(player for player in players if isinstance(player, Baddy))
            other_goody = next(player for player in players if isinstance(player, Goody) and player != self)

            weights = [(_ping_response[other_goody] - Position(x)).l1_norm() / (_ping_response[baddy] - Position(x)).l1_norm() 
                                                                    for x in [(0, 1), (1, 0), (0, -1), (-1, 0)]]

            positions = [UP, RIGHT, DOWN, LEFT]

            for (k, v) in zip(weights, positions).sort(key = lambda tup: tup[0]):
                if not _obstruction[v]:
                    return v
        else: 
            return STAY

        

            

