import pygame
from projectile import Projectile

# creer une 1ʳᵉ classe qui va representer le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        # creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))


    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity