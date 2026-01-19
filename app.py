# myPlanner Flask app

import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

if not os.path.exists("database"):
    os.makedirs("database")

db_path = "database/myPlanner.db"

def init_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
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

    c.execute("SELECT id, name, due_date FROM assignments")
    assignments = c.fetchall()

    c.execute("SELECT id, name, date FROM events")
    events = c.fetchall()

    conn.close()

    return render_template("dashboard.html", assignments=assignments, events=events)

@app.route("/add-assignment", methods=["POST"])
def add_assignment():
    name = request.form["name"]
    due_date = request.form["due_date"]

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO assignments (name, due_date) VALUES (?, ?)", (name, due_date))
    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))

@app.route("/add-event", methods=["POST"])
def add_event():
    name = request.form["name"]
    date = request.form["date"]

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO events (name, date) VALUES (?, ?)", (name, date))
    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))

@app.route("/delete-assignments/<int:id>", methods=["POST"])
def delete_assignment(id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DELETE FROM assignments WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("dashboard"))

@app.route("/delete-events/<int:id>", methods=["POST"])
def delete_event(id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DELETE FROM events WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("dashboard"))

@app.route("/update-assignments/<int:id>", methods=["POST"])
def update_assignment(id):
    name = request.form["name"]
    due_date = request.form["due_date"]

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("UPDATE assignments SET name = ?, due_date = ? WHERE id = ?", (name, due_date, id))
    conn.commit()
    conn.close()
    return redirect(url_for("dashboard"))

@app.route("/update-events/<int:id>", methods=["POST"])
def update_event(id):
    name = request.form["name"]
    date = request.form["date"]

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("UPDATE events SET name = ?, date = ? WHERE id = ?", (name, date, id))
    conn.commit()
    conn.close()
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
