"""
Implements a Food class to organize all of the properties
and methods related to the snake's food in one place
"""

from typing import List
from random import randrange  # used to put food in random places on the screen
from pygame import draw, image


class Food:
    """
    Collects all of the properties and methods of a snake's food
    """

    def __init__(self, color: List[int], size: int, display) -> None:
        """Create a new piece of food"""
        self.images = [
            image.load("./assets/images/food/apple.png"),
            image.load("./assets/images/food/beer.png"),
            image.load("./assets/images/food/cheese.png"),
            image.load("./assets/images/food/chicken.png"),
            image.load("./assets/images/food/chili.png"),
            image.load("./assets/images/food/salmon.png"),
            image.load("./assets/images/food/shrimp.png"),
            image.load("./assets/images/food/sushi.png"),
        ]
        self.color = color
        self.size = size
        self.display = display
        self.img = None
        self.spawn()

    def spawn(self):
        """Generate random x/y coordinates for the food on the display"""
        dw, dh = self.display.get_size()  # get the width/height of the display
        self.x = round(randrange(0, dw - self.size) / self.size) * self.size
        self.y = round(randrange(0, dh - self.size) / self.size) * self.size
        self.img = self.images[randrange(0, len(self.images))]

    def draw(self):
        """Draw the food on the display"""
        self.display.blit(self.img, (self.x, self.y))
