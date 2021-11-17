"""
Classic snake game in python. Code was generated following the
tutorial at: https://www.edureka.co/blog/snake-game-with-pygame/
"""

# import required packages
import pygame  # game development framework
import random  # used to put food in random places on the screen
from snake import Snake
from colors import blue, green, red, white

# initialize the game
pygame.init()

# set the screen size
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

# draw the screen
pygame.display.update()

# set a caption on the screen
pygame.display.set_caption("Snake game by Edureka and ISAT 252")

# Game clock: controls the speed of the game loop
clock = pygame.time.Clock()
snake_speed = 10  # higher number == faster snake == harder game
snake_color = blue
snake_head_size = 20

# setup for messages to be displayed on the screen
font_style = pygame.font.SysFont(None, 50)


def display_score(score):
    """Draws the score for the game on the screen"""
    value = font_style.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [10, 10])


# def draw_snake(segment_size, snake_list):
#     """Draws the segments of the snake"""
#     for x in snake_list:
#         pygame.draw.rect(dis, snake_color, [x[0], x[1], segment_size, segment_size])


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
    snake = Snake(blue, dis_width / 2, dis_height / 2)

    # get random x/y coordinates for the food
    foodx = (
        round(random.randrange(0, dis_width - snake.head_size) / snake.head_size)
        * snake.head_size
    )
    foody = (
        round(random.randrange(0, dis_height - snake.head_size) / snake.head_size)
        * snake.head_size
    )

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
            # if someone clicks a key on the keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # left arrow key
                    snake.turn("left")
                elif event.key == pygame.K_RIGHT:  # right arrow key
                    snake.turn("right")
                elif event.key == pygame.K_UP:  # up arrow key
                    snake.turn("up")
                elif event.key == pygame.K_DOWN:  # down arrow key
                    snake.turn("down")

        snake.move()

        # set `game_close` to True if the snake goes outside of the screen boundary or intersects itself
        game_close = snake.is_out_of_bounds(dis) or snake.has_crashed()

        # clear the display; gives us a blank canvas to re-draw the new snake position
        dis.fill(white)

        # draw a blue rectangle to represent the food
        pygame.draw.rect(dis, green, [foodx, foody, snake.head_size, snake.head_size])

        snake.draw(dis)
        display_score(snake.length - 1)

        # updates the surface (display area) with whatever changes
        # have been specified in this iteration through the game loop
        pygame.display.update()

        if snake.x == foodx and snake.y == foody:
            foodx = (
                round(
                    random.randrange(0, dis_width - snake_head_size) / snake_head_size
                )
                * snake_head_size
            )
            foody = (
                round(
                    random.randrange(0, dis_height - snake_head_size) / snake_head_size
                )
                * snake_head_size
            )
            snake.grow()

        # sets clock speed; higher number == faster game (and more difficult!)
        clock.tick(snake_speed)

    # quit the game
    pygame.quit()
    quit()


game_loop()
