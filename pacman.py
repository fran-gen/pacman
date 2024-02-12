import pygame

pygame.init()

WIDTH = 900
HEIGHT = 950
# set the game to have those static dimensions
screen = pygame.display.set_mode([WIDTH, HEIGHT])
# set the game's speed
timer = pygame.time.Clock()
# max speed
fps = 60
font = pygame.Font('freesansbold.ttf', 20)

run = True
while run:
    # control the frame rate
    timer.tick(fps)
    # fill the background color
    screen.fill('black')

    # avoid infinite while loop
    # event.get() gets anything pygame can process
    for event in pygame.event.get():
        # pygame.QUIT is a red cross to leave the game
        if event.type == pygame.QUIT:
            run = False

    # draw on the screen every iteration
    pygame.display.flip()
# deinitialize all Pygame modules
pygame.quit()

