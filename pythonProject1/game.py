import pygame
from player import Player
from monster import Monster

# creer une seconde classe qui va representer le jeu
class Game:

    def __init__(self):
        # generer le joueur
        self.player = Player(self)
        # groupe de montres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)