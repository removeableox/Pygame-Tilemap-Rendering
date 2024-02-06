import csv
from entity import Entity

# class for storing and rendering tilmaps for levels
# tilemaps created in tiled and then exported as csv file
# store tilemaps in "levels" directory in the root
class Tilemap:
    def __init__(self, tilemap : str, images : list):
        # variable that stores a list of tiles (in order according to csv made in tiled)
        self.images = images 
        # variable that stores the csv filename for the tilemap
        self.tilemap = tilemap
    
    def render(self, screen):
        # horizontal positioning for placing tiles
        horizontal = 0
        # vertical positioning for placing tiles
        vertical = 0
        with open(self.tilemap, 'r') as file:
            reader = csv.reader(file)
            # loop for rendering individual tiles in their respective positioning
            for row in reader:
                for point in row:
                    # whitespace in tilemap 
                    if point == "-1":
                        horizontal += 30
                        continue
                    tile = Entity(self.images[int(point)], [horizontal, vertical])
                    tile.render(screen)
                    horizontal += 30
                vertical += 30
                horizontal = 0