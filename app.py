# myPlanner Flask app

from flask import Flask

app = Flask(__name__)

@app.route("/")
def dashboard():
    return "Welcome to myPlanner"

if __name__ == "__main__":
    app.run(debug=True)
