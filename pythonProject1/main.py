import pygame
from game import Game
from player import Player

pygame.init()

# générer fenetre du jeu
pygame.display.set_caption("Simple Pygame Game")

# definir dimension fenetre
screen = pygame.display.set_mode((1080, 720))
# recuperer comme variable dans screen pour appliquer fond ecran en superpo
# on va dessiner sur la surface screen l'arreire plan background

# importer arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# charger le jeu
game = Game()

# charger le joueur
player = Player()

# maintenir fenetre éveillée
running = True

# boucle qui va s'executer tant que cette condition est vraie
while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    # appliquer image du joueur
    screen.blit(game.player.image, game.player.rect)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # Appliquer l'ensemble des images de mon groupe de monstres
    game.all_projectiles.draw(screen)
    # verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
    # if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < screen.get_width() - 200:
            game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre

    # en faisant ctrl sur get on arrive sur la liste d'evenement sur laquelle on veut boucler
    for event in pygame.event.get():
        # pour verifier que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            # on entre dans la condition et je commence par stopper ma boucle avec chgt de valeur
            running = False
            # fermeture du jeu
            pygame.quit()
            print("Quitting")

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
