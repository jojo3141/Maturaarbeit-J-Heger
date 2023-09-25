import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1300, 660
SQUARE_SIZE = 160
TEXT_FONT_SIZE = 400
# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Square")

# Load the image for the square
square_image = pygame.image.load("airplane_pam.png")

# Initialize the position of the square
x = 0
y = 130
text_x = 0
text_y = 300  # Adjust the Y position of the text

font = pygame.font.Font(None, TEXT_FONT_SIZE)

# Main game loop
clock = pygame.time.Clock()

mode = "picture"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update the square position and wrap around if needed
    if mode == "picture":
        x -= 0  # Move the square to the left
    else:
        text_x -= 0

    # Wrap around to the right side if the square goes off the screen
    if x + SQUARE_SIZE + 700 < 0:
        mode = "text"
        x = WIDTH



    if text_x + len("This is my example text") * TEXT_FONT_SIZE < 0+2000:
        mode = "picture"
        text_x = WIDTH

    text = font.render("This is my example text. Can you read it?", True, "black")
    if mode == "text":
        screen.blit(text, (text_x, text_y))
    else:
        screen.blit(square_image, (x, y))

    for i in range(10):
        pygame.draw.rect(screen, "black", (0 + 130*i, 0, 129, 2000))

    print(mode)

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(150)
