from datetime import datetime
import time
import text_lib
import os

running = True

def start(screen_size):
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    t = ""

    while(running):
        current_time = str(datetime.now().time())
        lines = text_lib.text_to_lines(current_time[:5])
        lines = (lines + ["0x00"] * screen_size[0])[:screen_size[0]]
        # Write to a temp file and swap it in so the display never reads a half-written file
        tmp_path = input_path + ".tmp"
        with open(tmp_path, "w") as f:
            f.write("\n".join(lines))
        os.replace(tmp_path, input_path)
        time.sleep(1)

def stop():
    global running
    running = False