"""
Creates the background for the game screen
"""

from random import randrange
from pygame import image, Surface
from main import resource_path


class Background:
    """Defines the game background"""

    def __init__(self, tile_size: int, tile_width: int, tile_height: int) -> None:
        """Initializes the background given the number of tiles in the x and y directions"""
        self.surface = Surface((tile_width * tile_size, tile_height * tile_size))
        for y in range(0, tile_height):
            for x in range(0, tile_width):
                img_file = resource_path(
                    "./assets/images/grass/grass" + str(randrange(0, 10)) + ".png"
                )
                img = image.load(img_file)
                self.surface.blit(img, (x * tile_size, y * tile_size))
