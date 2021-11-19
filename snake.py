"""
Implements a Snake class to organize all of the properties
and methods related to the snake in one place
"""
from pygame import draw, K_LEFT, K_RIGHT, K_UP, K_DOWN
from food import Food


class Snake:
    """
    Collects all of the properties and methods of a snake
    """

    def __init__(self, color, display, length: int = 1, head_size: int = 10) -> None:
        """Defines basic properties of a snake"""
        w, h = display.get_size()
        self.color = color
        self.x = w / 2
        self.y = h / 2
        self.display = display
        self.length = 1
        self.head_size = head_size
        self.segments = []  # list of Segments
        self.direction = {
            "x": 0,
            "y": 0,
        }
        self.head = [self.x, self.y]

    def turn(self, direction: str):
        """Change the direction of the snake"""
        if direction == K_LEFT:
            self.direction["x"] = -self.head_size
            self.direction["y"] = 0
        elif direction == K_RIGHT:
            self.direction["x"] = self.head_size
            self.direction["y"] = 0
        elif direction == K_UP:
            self.direction["x"] = 0
            self.direction["y"] = -self.head_size
        elif direction == K_DOWN:
            self.direction["x"] = 0
            self.direction["y"] = self.head_size

    def move(self):
        """Moves the snake by one increment"""
        self.x += self.direction["x"]
        self.y += self.direction["y"]
        self.segments.append(
            Segment(self.x, self.y, self.head_size, self.head_size, self.color)
        )
        if len(self.segments) > self.length:
            del self.segments[0]

    def grow(self):
        """Increase the length of the snake by 1 segment"""
        self.length += 1

    def draw(self):
        """Draws the segments of the snake on the specified display"""
        for segment in self.segments:
            segment.draw(self.display)

    def has_crashed(self):
        """Returns True if snake has collided with itself"""
        head = self.segments[-1]
        for seg in self.segments[:-1]:
            if seg.x == head.x and seg.y == head.y:
                return True
        return False

    def eats(self, food: Food):
        """Returns True if the food and snake head are co-located"""
        return self.x == food.x and self.y == food.y

    def is_out_of_bounds(self):
        """Checks to see if the snake is out of bounds"""
        w, h = self.display.get_size()
        return self.x >= w or self.x < 0 or self.y >= h or self.y < 0


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
