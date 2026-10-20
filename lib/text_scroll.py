from lib import display, text_lib

def frames(text, width=display.WIDTH, small=False):
    if(small):
        columns = text_lib.text_to_lines_small(text)
    else:
        columns = text_lib.text_to_lines(text)
    last_start = max(len(columns) - width, 0)
    for start in range(last_start + 1):
        yield (columns[start:start + width] + [0x00] * width)[:width]

def scroll(text, speed=0.1, loop=True, hold=None, width=display.WIDTH, prefix=(), small = False):
    if hold is None:
        hold = speed * 2
    prefix = list(prefix)
    text_frames = list(frames(text, width - len(prefix), small))
    last = len(text_frames) - 1
    while True:
        for i, frame in enumerate(text_frames):
            display.draw(prefix + frame)
            delay = hold if i in (0, last) else speed
            if display.stop_event.wait(delay):
                return False
        if not loop:
            return True
