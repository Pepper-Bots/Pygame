import pygame

# créer une classe qui va gérer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()


