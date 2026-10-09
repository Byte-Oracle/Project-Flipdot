import time
from lib import display

anim_speed = 0.025

def start(screen_size):
    t_rows = screen_size[0]
    t_col = screen_size[1]
    frame = [0x00] * t_rows
    for row in range(t_rows + t_col):
        for col in range(t_rows):
            if col < row:
                frame[col] = ((frame[col] << 1 | 1)) & 0x7F
        display.draw(frame)
        time.sleep(anim_speed)

    for row in range(t_rows + t_col):
        for col in range(t_rows):
            if col < row:
                frame[col] = ((frame[col] << 1 | 0)) & 0x7F
        display.draw(frame)
        time.sleep(anim_speed)
