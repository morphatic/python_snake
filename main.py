"""
Classic snake game in python. Code was generated following the
tutorial at: https://www.edureka.co/blog/snake-game-with-pygame/
"""

# import required packages
import pygame

# initialize the game
pygame.init()

# set the screen size
dis = pygame.display.set_mode((400, 300))

# draw the screen
pygame.display.update()

# set a caption on the screen
pygame.display.set_caption("Snake game by Edureka")

# variables to hold different colors
blue = (0, 0, 255)
red = (255, 0, 0)
purple = (255, 0, 255)

# create a variable to keep track of whether or not the game is over
game_over = False

# the main game loop. this loop will run infinitely until the value
# of `game_over` changes from `False` to `True`
while not game_over:
    # loops over all of the events (like keypresses and mouse moves
    # and button clicks) that happen during one game loop cycle
    for event in pygame.event.get():
        # if someone clicks the red X in the upper right
        if event.type == pygame.QUIT:
            game_over = True
        # print(event)  # prints out all the actions that take place on the screen


# quit the game
pygame.quit()
quit()
