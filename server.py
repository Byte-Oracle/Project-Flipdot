from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Cool Stuff Coming</p>"
