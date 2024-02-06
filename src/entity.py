import pygame

# class for storing and rendering entities
# images stored in assets folder in the root
# entities are anything that is rendered (sprites, tiles, etc)
class Entity:
    def __init__(self, src : str, dest : list):
        self.object = pygame.image.load(src)
        # entity location EX: [0, 0]
        self.dest = dest

    def render(self, screen):
        screen.blit(self.object, self.dest)