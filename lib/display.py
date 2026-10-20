import threading
import serial

PORT, BAUD, ADDR = "/dev/serial0", 57600, 0xFF
WIDTH, HEIGHT = 28, 7

_serial = serial.Serial(PORT, BAUD)
_write_lock = threading.Lock()
_switch_lock = threading.Lock()
_current = None
stop_event = threading.Event()

def busy():
    return _current is not None and _current.is_alive()

def draw(frame):
    frame = (list(frame) + [0x00] * WIDTH)[:WIDTH]
    with _write_lock:
        _serial.write(bytes([0x80, 0x83, ADDR] + frame + [0x8F]))

def run(func, *args):
    # Only one job owns the display: stop the current one, wait for it
    # (including its exit transition), then start the new one.
    global _current
    with _switch_lock:
        stop()
        if _current is not None:
            _current.join()
        stop_event.clear()
        _current = threading.Thread(target=func, args=args, daemon=True)
        _current.start()

def stop():
    stop_event.set()
