from lib import display, transitions, text_lib
import time

loop = True
animation_speed = .1
def start(screen_size, text, speed, loop):
    loop = bool(loop)
    animation_speed = float(speed)
    screen_width = screen_size[0]
    text = text_lib.text_to_lines(text)
    frame = 0x00 * screen_width
    displayed_text_count = screen_width
    lines_to_display = len(text)
    current_line = 0

    frame = (text[:screen_width] + ([0x00] * screen_width))[:screen_width]
    while not display.stop_event.is_set():
        display.draw(frame)
        time.sleep(animation_speed * 2)
        print(lines_to_display)
        while displayed_text_count < lines_to_display:
            current_line += 1
            displayed_text_count += 1
            frame = text[current_line:current_line + screen_width]
            display.draw(frame)
            time.sleep(animation_speed)
        time.sleep(animation_speed * 2)
        current_line = 0
        displayed_text_count = screen_width

    stop(screen_size)

def stop(screen_size):
    transitions.get_rand_transition().start(screen_size)