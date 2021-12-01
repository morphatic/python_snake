"""
Implements a Snake class to organize all of the properties
and methods related to the snake in one place
"""
from pygame import draw, K_LEFT, K_RIGHT, K_UP, K_DOWN, image, transform
from food import Food


class Snake:
    """
    Collects all of the properties and methods of a snake
    """

    def __init__(self, color, display, head_size: int = 10) -> None:
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
        self.orientation = 0

    def turn(self, direction: str):
        """Change the direction of the snake"""
        if direction == K_LEFT:
            self.direction["x"] = -self.head_size
            self.direction["y"] = 0
            self.orientation = 90
        elif direction == K_RIGHT:
            self.direction["x"] = self.head_size
            self.direction["y"] = 0
            self.orientation = 270
        elif direction == K_UP:
            self.direction["x"] = 0
            self.direction["y"] = -self.head_size
            self.orientation = 0
        elif direction == K_DOWN:
            self.direction["x"] = 0
            self.direction["y"] = self.head_size
            self.orientation = 180

    def move(self):
        """Moves the snake by one increment"""
        self.x += self.direction["x"]
        self.y += self.direction["y"]
        self.segments.append(
            Segment(self.x, self.y, self.head_size, self.head_size, self.orientation)
        )
        if len(self.segments) > self.length:
            del self.segments[0]

    def grow(self):
        """Increase the length of the snake by 1 segment"""
        self.length += 1

    def draw(self):
        """Draws the segments of the snake on the specified display"""
        for i, segment in enumerate(self.segments):
            is_turn = (
                i != len(self.segments) - 1
                and self.segments[i].orientation - self.segments[i + 1].orientation != 0
            )
            is_ccw = is_turn and (
                self.segments[i].orientation - self.segments[i + 1].orientation == 90
                or self.segments[i].orientation - self.segments[i + 1].orientation
                == -270
            )
            segment.draw(self.display, i, i == len(self.segments) - 1, is_turn, is_ccw)

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

    def __init__(
        self, x: int, y: int, width: int, height: int, orientation: int = 0
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.images = [
            image.load("./assets/images/snake/head.png"),
            image.load("./assets/images/snake/body.png"),
            image.load("./assets/images/snake/turn.png"),
            image.load("./assets/images/snake/tail.png"),
        ]
        self.img = self.images[0]
        self.orientation = orientation

    def draw(self, display, pos, is_head, is_turn, is_ccw):
        """Draws the segment"""
        if is_head:
            self.img = self.images[0]  # head
        elif pos == 0:
            self.img = self.images[3]  # tail
        elif is_turn:
            self.img = self.images[2]  # turn
        else:
            self.img = self.images[1]  # body
        rotation = self.orientation + 90 if is_ccw else self.orientation
        img, rect = self.rotate(rotation)
        display.blit(img, rect)
        # draw.rect(display, self.color, [self.x, self.y, self.width, self.height])

    def rotate(self, angle: int):
        """Rotates a segment"""
        rotated_img = transform.rotate(self.img, angle)
        rotated_rect = rotated_img.get_rect(
            center=self.img.get_rect(
                center=(self.x + self.width / 2, self.y + self.height / 2)
            ).center
        )
        return rotated_img, rotated_rect
