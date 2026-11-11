import json, ssl
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
from lib import display, text_lib, text_scroll, transitions, defaults

PORT = 8883
USERNAME = "bblp"

STATE_LABELS = {
    "IDLE": "IDLE",
    "PAUSE": "PAUSED",
    "FINISH": "DONE",
    "FAILED": "FAILED",
}


def start(screen_size, wait=5, speed=0.1):
    ip = defaults.BAMBU_IP
    access_code = defaults.BAMBU_ACCESS_CODE
    serial_number = defaults.BAMBU_SERIAL_NUMBER

    if not (ip and access_code and serial_number):
        show("NO CONFIG", screen_size, speed)
        display.stop_event.wait()
        stop(screen_size)
        return

    userdata = {
        "connected": False,
        "report": f"device/{serial_number}/report",
        "request": f"device/{serial_number}/request",
        "print": {},
    }

    client = mqtt.Client(CallbackAPIVersion.VERSION2, userdata=userdata)
    client.username_pw_set(USERNAME, access_code)
    client.tls_set(cert_reqs=ssl.CERT_NONE)
    client.tls_insecure_set(True)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect_async(ip, PORT, keepalive=60)
    client.loop_start()

    # TODO: Going to rewrite this to have a progress bar that moves across with the % text in the center
    try:
        show_progress = True
        while not display.stop_event.is_set():
            text = status_text(userdata, show_progress)
            show_progress = not show_progress
            if not show(text, screen_size, speed):
                break
            if display.stop_event.wait(wait):
                break
    finally:
        client.loop_stop()
        client.disconnect()

    stop(screen_size)


def stop(screen_size):
    transitions.get_rand_transition().start(screen_size)


def status_text(userdata, show_progress):
    if not userdata["connected"]:
        return "OFFLINE"

    status = dict(userdata["print"])
    state = status.get("gcode_state")
    if state is None:
        return "..."
    if state in STATE_LABELS:
        return STATE_LABELS[state]

    # RUNNING, PREPARE, etc: alternate between percent and time left.
    if show_progress:
        return f"{status.get('mc_percent', 0)}%"
    minutes = status.get("mc_remaining_time", 0)
    return f"{minutes // 60}:{minutes % 60:02d}"


def show(text, screen_size, speed):
    columns = text_lib.text_to_lines_small(text)
    if len(columns) <= screen_size[0]:
        display.draw(columns)
        return True
    return text_scroll.scroll(text, speed=speed, loop=False, width=screen_size[0], small=True)


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Bambu connect failed: {reason_code}")
        return
    userdata["connected"] = True
    client.subscribe(userdata["report"])
    # Ask for a full status dump; later reports only contain changes.
    pushall = {"pushing": {"sequence_id": "0", "command": "pushall"}}
    client.publish(userdata["request"], json.dumps(pushall))


def on_disconnect(client, userdata, flags, reason_code, properties):
    userdata["connected"] = False


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload)
    except ValueError:
        return
    userdata["print"].update(payload.get("print", {}))
