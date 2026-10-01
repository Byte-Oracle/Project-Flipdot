import os
import threading
import pygame
import flip_clock

# Resolve input.txt relative to this script, not the current working directory
input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

screen_scale = 50
screen_width = 28
screen_height = 7
pygame.init()
screen = pygame.display.set_mode((screen_width * screen_scale, screen_height * screen_scale))
clock = pygame.time.Clock()
running = True

f_clock = flip_clock
clock_thread = threading.Thread(target=f_clock.start, args=((screen_width, screen_height),), daemon=True)
clock_thread.start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f_clock.stop()
            running = False
    
    screen.fill("black")
    with open(input_path) as f:
        t = f.readlines()

    x = 0
 
    for x in range(screen_width):
        y = 0
        l = int(t[x], 16)
        for y in range(screen_height):
                if (l >> y) & 1:
                    rect = pygame.Rect(x * screen_scale, y * screen_scale, screen_scale - 1, screen_scale - 1)
                    pygame.draw.rect(screen, "white", rect)         

    pygame.display.flip()

    clock.tick(15)

pygame.quit()