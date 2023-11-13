import pygame

pygame.init()

WIDTH = 900
HEIGHT = 950

# Set the game to have those static dimensions
screen = pygame.display.set_mode([WIDTH, HEIGHT])
# Set the game's speed
timer = pygame.time.Clock()