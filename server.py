from flask import Flask, render_template, redirect, url_for, request
from features import flip_clock_feature as flip_clock, text_scroll_feature, mc_server_status_feature
from lib import display, transitions

app = Flask(__name__)
screen_size = (display.WIDTH, display.HEIGHT)

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/clock")
def clock():
    display.run(flip_clock.start, screen_size)
    return redirect(url_for("index"))

@app.post("/scrolling_text")
def scrolling_text():
    speed = request.form.get("animation_speed")
    loop = request.form.get("loop_toggle")
    text = request.form.get("input_text")
    display.run(text_scroll_feature.start, screen_size, text, speed, loop)
    return redirect(url_for("index"))

@app.post("/mc_server_status")
def mc_server_status():
    address = request.form.get("server_address")
    speed = float(request.form.get("animation_speed", 0.1))
    wait = int(request.form.get("wait", 30))
    display.run(mc_server_status_feature.start, screen_size, address, speed, wait)
    return redirect(url_for("index"))

@app.post("/transition")
def transition():
    display.run(transitions.get_rand_transition().start, screen_size)
    return redirect(url_for("index"))

@app.post("/stop")
def stop():
    display.stop()
    return redirect(url_for("index"))



display.run(transitions.get_rand_transition().start, screen_size)
