from lib import transitions, text_scroll, defaults

def start(screen_size, text, speed, loop):
    txt = ""
    is_looping = True
    if text == "":
        txt = defaults.SCROLLING_TEXT
        is_looping = defaults.SCROLLING_TEXT_LOOP
    else:
        txt = text
        is_looping = loop
    text_scroll.scroll(txt, speed=float(speed), loop=bool(is_looping), width=screen_size[0])
    stop(screen_size)

def stop(screen_size):
    transitions.get_rand_transition().start(screen_size)
