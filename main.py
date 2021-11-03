"""
Classic snake game in python. Code was generated following the
tutorial at: https://www.edureka.co/blog/snake-game-with-pygame/
"""

# import required packages
import pygame

# initialize the game
pygame.init()

# set the screen size
dis = pygame.display.set_mode((800, 600))

# draw the screen
pygame.display.update()

# set a caption on the screen
pygame.display.set_caption("Snake game by Edureka")

# variables to hold different colors
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

# create a variable to keep track of whether or not the game is over
game_over = False

# variables to control the x/y coordinates of the snake head
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0

# I don't know what this does (yet)
clock = pygame.time.Clock()

# the main game loop. this loop will run infinitely until the value
# of `game_over` changes from `False` to `True`
while not game_over:
    # loops over all of the events (like keypresses and mouse moves
    # and button clicks) that happen during one game loop cycle
    # print(event)  # prints out all the actions that take place on the screen
    for event in pygame.event.get():
        # if someone clicks the red X in the upper right, quit the game
        if event.type == pygame.QUIT:
            game_over = True
        # if someone clicks a key on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # left arrow key
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:  # right arrow key
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:  # up arrow key
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:  # down arrow key
                y1_change = 10
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    # draw a yellow rectangle to represent the head of the snake
    # see: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
    pygame.draw.rect(dis, blue, [x1, y1, 10, 10])

    # updates the surface (display area) with whatever changes
    # have been specified in this iteration through the game loop
    pygame.display.update()

    # what does this do???
    clock.tick(30)

# quit the game
pygame.quit()
quit()
