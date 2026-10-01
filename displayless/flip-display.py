import os
import pygame

# Resolve input.txt relative to this script, not the current working directory
input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

screen_scale = 50
screen_width = 28
screen_height = 7
pygame.init()
screen = pygame.display.set_mode((screen_width * screen_scale, screen_height * screen_scale))
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")
    with open(input_path) as f:
        t = f.readlines()

    x = 0
    y = 0
    for x in range(screen_width):
        for y in range(screen_height):
            # Loops over the output text file to read and display.
            # In the actual physical one this will be assembled into a byte for each line
            if(t[y][x] == "1"):
                rect = pygame.Rect(x * screen_scale, y * screen_scale, screen_scale - 1, screen_scale - 1)
                pygame.draw.rect(screen, "white", rect)
            y += 1
        x += 1           

    pygame.display.flip()

    clock.tick(15)

pygame.quit()