from flask import Flask, render_template, redirect, url_for
from features import flip_clock_feature as flip_clock
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

@app.post("/transition")
def transition():
    display.run(transitions.get_rand_transition().start(screen_size))
    return redirect(url_for("index"))

@app.post("/stop")
def stop():
    display.stop()
    return redirect(url_for("index"))

display.run(transitions.get_rand_transition().start, screen_size)
