import mcstatus, time
from lib import display, text_lib, text_scroll, transitions

def start(screen_size, server_address, speed=0.1, wait=30):
    server = mcstatus.JavaServer.lookup(str(server_address), timeout=3)
    while not display.stop_event.is_set():
        try:
            status = server.status()
        except OSError:
            display.draw(text_lib.text_to_lines("OFF"))
            if display.stop_event.wait(wait):
                break
            continue

        motd = " ".join(status.motd.to_plain().split())
        prefix = text_lib.text_to_lines_small(str(status.players.online)) + [0x7F, 0x00]
        if not text_scroll.scroll(motd, speed=speed, loop=False, width=screen_size[0], prefix=prefix, small=True):
            break
        if display.stop_event.wait(wait):
            break

    stop(screen_size)

def stop(screen_size):
    transitions.get_rand_transition().start(screen_size)
