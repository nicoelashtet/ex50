from flask import Flask
from flask import render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def index():
    greeting = "ハローワールド！"
    return render_template("index.html", greeting=greeting)
