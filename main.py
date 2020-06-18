import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Allien Killer")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("alienbig.png")
playerX = 150
playerY = 50

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:
    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()