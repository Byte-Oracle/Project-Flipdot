from lib import transitions, text_scroll

def start(screen_size, text, speed, loop):
    text_scroll.scroll(text, speed=float(speed), loop=bool(loop), width=screen_size[0])
    stop(screen_size)

def stop(screen_size):
    transitions.get_rand_transition().start(screen_size)
