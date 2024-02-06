import pygame
from entity import Entity
from tilemap import Tilemap

# window initialization
pygame.init()
size = width, height = 900, 500
screen = pygame.display.set_mode(size)

# colours
black = 0, 0, 0
white = 255, 255, 255
blue = 81, 172, 224

# tile source images
images = [
    "../assets/player.png",
    "../assets/ground.png",
]

# tilemaps
levelOne = Tilemap("../levels/levelOne.csv", images)

# game loop
while True:
    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()

    # rendering operations
    screen.fill(blue)

    levelOne.render(screen)

    pygame.display.flip()