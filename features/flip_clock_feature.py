from datetime import datetime
from lib import display, text_lib, transitions

padding = 0
def start(screen_size):
    while not display.stop_event.is_set():
        current_time = datetime.now()
        formatted = str(current_time.strftime("%I:%M %p"))
        dot = ((0x00 << 1 | int(formatted.endswith("PM"))))& 0x7F
        display.draw([0x0] * padding + text_lib.text_to_lines(formatted[:5]) + [dot])
        display.stop_event.wait(.25)
    stop(screen_size)

def stop(screen_size):
    transitions.get_rand_transition().start(screen_size)
