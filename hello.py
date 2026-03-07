from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index Page</p>"


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

