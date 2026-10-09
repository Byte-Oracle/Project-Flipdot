from datetime import datetime
from lib import display, text_lib, transitions

padding = 2
def start(screen_size):
    while not display.stop_event.is_set():
        current_time = str(datetime.now().time())
        display.draw([0x0] * padding + text_lib.text_to_lines(current_time[:5]))
        display.stop_event.wait(.25)
    stop(screen_size)

def stop(screen_size):
    transitions.get_rand_transition().start(screen_size)
