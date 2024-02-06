# Pygame Tilemap Rendering

Simple python code for rendering tilemaps with pygame.  
Im using tiled to create tilemaps and exporting them in csv.  
All useful code is split into entity.py and tilemap.py in the src directory for use in other projects.

# Dependencies

pygame:  
`pip intall pygame`

# Installation and Use

## Clone Important Files

Clone the repo and take out use important files  
(tilemap.py and entity.py in src directory)  
`git clone https://github.com/removeableox/Pygame-Tilemap-Rendering`

## Use in Your Project

Import Tilemap class from tilemap.py and create a new Tilemap instance

```
from tilemap import Tilemap

tilemap = Tilemap("/PATH/TO/YOUR/TILEMAP.csv", LIST_OF_TILES_IN_ORDER)
```

Render your tilemap in your game loop

```
levelOne.render(screen)
```
