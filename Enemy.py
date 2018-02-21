from random import randint
from Character import Character

class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'a goblin'
    self.health = randint(1, player.health)
