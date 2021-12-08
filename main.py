"""
Classic snake game in python. Code was generated following the
tutorial at: https://www.edureka.co/blog/snake-game-with-pygame/
"""

# import required packages
import pygame  # game development framework
from background import Background
from snake import Snake
from food import Food
from colors import blue, green, red, white
from utilities import resource_path

# initialize the game
pygame.init()


# set the screen size
TILE_SIZE = 16  # one game tile is 16x16 pixels
TILE_WIDTH = 50  # width of screen is 50 tiles = 800 pixels
TILE_HEIGHT = 38  # height of screen is 38 tiles = 608 pixels
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((TILE_WIDTH * TILE_SIZE, TILE_HEIGHT * TILE_SIZE))

# draw the screen
pygame.display.update()

# create the background
background = Background(TILE_SIZE, TILE_WIDTH, TILE_HEIGHT)

# set a caption on the screen
pygame.display.set_caption("Snake game by Edureka and ISAT 252")

# Game clock: controls the speed of the game loop
clock = pygame.time.Clock()
snake_speed = 10  # higher number == faster snake == harder game
snake_color = blue
snake_head_size = 20

# setup for messages to be displayed on the screen
font_style = pygame.font.SysFont(None, 50)
LUCKIEST_GUY_FONT = pygame.font.Font(
    resource_path("./assets/fonts/LuckiestGuy-Regular.ttf"), 40
)
RANCHERS_FONT = pygame.font.Font(
    resource_path("./assets/fonts/Ranchers-Regular.ttf"), 40
)


def display_score(score):
    """Draws the score for the game on the screen"""
    value = RANCHERS_FONT.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [10, 10])


def message(msg, color):
    """Displays a message `msg` in a `color` on the screen, anchored in the middle"""
    mesg = font_style.render(msg, True, color)
    # TODO: figure out how to center the message on the screen and wrap if it's too long
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


def game_loop():
    """Sets up and controls the main game loop"""

    # create variables to keep track of whether or not the game is over and/or closed
    game_over = False
    game_close = False

    # create a snake
    snake = Snake(blue, dis, TILE_SIZE)

    # create a piece of food
    food = Food(green, snake.head_size, dis)

    # arrow keys
    arrow_keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

    # the main game loop. this loop will run infinitely until the value
    # of `game_over` changes from `False` to `True`
    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # if someone clicks an arrow key
            if event.type == pygame.KEYDOWN and event.key in arrow_keys:
                snake.turn(event.key)

        snake.move()

        # draw the background
        dis.blit(background.surface, (0, 0))

        # set `game_close` to True if the snake goes outside of the screen boundary or intersects itself
        game_close = snake.is_out_of_bounds() or snake.has_crashed()

        # clear the display; gives us a blank canvas to re-draw the new snake position
        # dis.fill(white)

        # draw the food
        food.draw()

        snake.draw()
        display_score(snake.length - 1)

        # updates the surface (display area) with whatever changes
        # have been specified in this iteration through the game loop
        pygame.display.update()

        if snake.eats(food):
            food.spawn()  # TODO: make sure food doesn't spawn on top of the snake
            snake.grow()

        # sets clock speed; higher number == faster game (and more difficult!)
        clock.tick(snake_speed)

    # quit the game
    pygame.quit()
    quit()


game_loop()
