import random

from maze import Goody, UP, DOWN, LEFT, RIGHT, STAY, PING, DX, DY

def norm(p):
   return abs(p.x) + abs(p.y)

class EdGoody(Goody):

    gohere = (0,0)

    def on_ping(self, pr):
          self.gohere = (0,0)
          badpos = (0,0)
          goodpos = (0,0)
          for player, position in pr.iteritems():
            if isinstance(player, Goody):
              #friend
              goodpos = position
            else:
              #run away
              badpos = -position
          if (norm(badpos) > norm(goodpos)):
              self.gohere = goodpos
          else: self.gohere = -badpos      

    def take_turn(self, obstr, pr):
        if pr: on_ping(self, pr);

        # given self.gohere, decide where to go.
        if (self.gohere == (0,0)): return PING
        if (random.randint(0,100) == 0): return PING
        
        def weightfn(dir):
          if (dir == UP)    & (self.gohere.y > 0): return dir, 5
          if (dir == UP)    & (self.gohere.y <= 0): return dir, 1 
          if (dir == DOWN)  & (self.gohere.y > 0): return dir, 1
          if (dir == DOWN)  & (self.gohere.y <= 0): return dir, 5 
          if (dir == RIGHT) & (self.gohere.x > 0): return dir, 5
          if (dir == RIGHT) & (self.gohere.x <= 0): return dir, 1 
          if (dir == LEFT)  & (self.gohere.x > 0): return dir, 1
          if (dir == LEFT)  & (self.gohere.x <= 0): return dir, 5 

        possibilities = map(weightfn , filter(lambda direction: not obstr[direction], [UP, DOWN, LEFT, RIGHT]))
        
        if possibilities:
            
            total = 0
            for d, w in possibilities: total += w
            map((lambda (d,w): (d,(w / total))), possibilities)
            ds,ws = zip(*possibilities)
            return random.choice(ds)
            #return random.choice(ds, p=ws)

          
            

        return STAY

