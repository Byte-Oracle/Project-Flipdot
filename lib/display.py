import threading
import serial

PORT, BAUD, ADDR = "/dev/serial0", 57600, 0xFF
WIDTH, HEIGHT = 28, 7

_serial = serial.Serial(PORT, BAUD)
_lock = threading.Lock()
stop_event = threading.Event()

def busy():
    return _lock.locked()

def draw(frame):
    frame = (list(frame) + [0x00] * WIDTH)[:WIDTH]
    _serial.write(bytes([0x80, 0x83, ADDR] + frame + [0x8F]))

def run(func, *args):
    if not _lock.acquire(blocking=False):
        return False

    stop_event.clear()

    def job():
        try:
            func(*args)
        finally:
            _lock.release()

    threading.Thread(target=job, daemon=True).start()
    return True

def stop():
    stop_event.set()
