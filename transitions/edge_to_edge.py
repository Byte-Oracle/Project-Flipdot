import time
from lib import display

anim_speed = 0.025

def start(screen_size):
    frame = []
    full_col = (1 << screen_size[1]) - 1
    for col in range(screen_size[0]):
        frame.append(full_col)
        display.draw(frame)
        time.sleep(anim_speed)
    for col in range(screen_size[0]):
        frame[col] = 0x00
        display.draw(frame)
        time.sleep(anim_speed)
