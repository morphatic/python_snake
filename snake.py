"""
Implements a Snake class to organize all of the properties
and methods related to the snake in one place
"""
from pygame import draw


class Snake:
    """
    Collects all of the properties and methods of a snake
    """

    def __init__(
        self, color, x: int, y: int, length: int = 1, head_size: int = 10
    ) -> None:
        """Defines basic properties of a snake"""
        self.color = color
        self.x = x
        self.y = y
        self.length = 1
        self.head_size = head_size
        self.segments = []  # list of Segments
        self.direction = {
            x: 0,
            y: 0,
        }
        self.head = [x, y]

    def move(self, direction: str):
        """Change the direction of the snake"""
        if direction == "left":
            self.direction.x = -self.head_size
            self.direction.y = 0
        elif direction == "right":
            self.direction.x = self.head_size
            self.direction.y = 0
        elif direction == "up":
            self.direction.x = 0
            self.direction.y = -self.head_size
        elif direction == "down":
            self.direction.x = 0
            self.direction.y = self.head_size

    def grow(self):
        """Increase the length of the snake by 1 segment"""
        self.length += 1

    def draw(self, display):
        """Draws the segments of the snake on the specified display"""
        for segment in self.segments:
            segment.draw(display)


class Segment:
    """Represents one segment of a snake"""

    def __init__(self, x: int, y: int, width: int, height: int, color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, display):
        """Draws the segment"""
        draw.rect(display, self.color, [self.x, self.y, self.width, self.height])
