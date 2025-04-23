import pygame

# definir la classe qui va gerer le projectile du joueur - entre () héritage
class Projectile(pygame.sprite.Sprite):

    # definir constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle += 2
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    # supprimer le projectile (en dehors de l'ecran)
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # verifier si le projectile n'est plus present sur l'ecran
        if self.rect.x > 1080:
                self.remove()
                print("Projectile removed")

