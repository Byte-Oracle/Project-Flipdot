import threading
from flask import Flask, render_template, redirect, url_for
from features import test as test_feature

display_lock = threading.Lock()
stop_event = threading.Event()
app = Flask(__name__)

def run_feature(func):
    # Only start the feature if nothing else is using the display
    if not display_lock.acquire(blocking=False):
        return

    stop_event.clear()

    def job():
        try:
            func(stop_event)
        finally:
            display_lock.release()

    threading.Thread(target=job).start()

def stop_feature():
    # Ask the running feature to stop; it has to check stop_event to notice
    stop_event.set()

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/test")
def test():
    run_feature(test_feature.run)
    return redirect(url_for("index"))

@app.post("/stop")
def stop():
    stop_feature()
    return redirect(url_for("index"))
