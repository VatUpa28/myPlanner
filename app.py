# myPlanner Flask app

import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ensure database folder exists
if not os.path.exists("database"):
    os.makedirs("database")

# Path to database
db_path = "database/myPlanner.db"

def init_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT
        )
    ''')

    conn.commit()
    conn.close()

@app.route("/")
def dashboard():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Get all assignments
    c.execute("SELECT title, due_date FROM assignments")
    assignments = c.fetchall()

    # Get all events
    c.execute("SELECT name, date FROM events")
    events = c.fetchall()

    conn.close()

    return render_template("dashboard.html", assignments=assignments, events=events)

@app.route("/add-assignment", methods=["POST"])
def add_assignment():
    title = request.form["title"]
    due_date = request.form["due_date"]

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute(
        "INSERT INTO assignments (title, due_date) VALUES (?, ?)",
        (title, due_date)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))

@app.route("/add-event", methods=["POST"])
def add_event():
    name = request.form["name"]
    date = request.form["date"]

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute(
        "INSERT INTO events (name, date) VALUES (?, ?)",
        (name, date)
    )

    conn.commit()
    conn.close

    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
