"""MyGame
"""
import os.path
import pygame

current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path,
                             '/home/angel/Documentos/Holberton/MyGameProject/')
image_path = os.path.join(resource_path, 'img')


# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Allien Killer')
icon = pygame.image.load(os.path.join(image_path, 'alien.png'))
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(os.path.join(image_path, 'spaceship.png'))
PLAYER_X = 350
PLAYER_Y = 500
PLAYER_X_CHANGE = 0


def player(x, y):
    """player function
    """
    screen.blit(playerImg, (x, y))


# Game Loop
RUNNING = True
while RUNNING:
    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER_X_CHANGE -= 0.5
            if event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE += 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE = 0

    PLAYER_X += PLAYER_X_CHANGE
    player(PLAYER_X, PLAYER_Y)
    pygame.display.update()
