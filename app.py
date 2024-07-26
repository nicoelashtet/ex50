from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    greeting = "World"
    return f'Hello, {greeting}!'

# Run the Flask application if this script is executed
if __name__ == "__main__":
    app.run()
