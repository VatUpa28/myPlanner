# myPlanner Flask app

import os
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# Ensure database folder exists
if not os.path.exists("database"):
    os.makedirs("database")

# Path to database
db_path = "database/myPlanner.db"

# Create database and tables if they don't exist
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Create assignments table
c.execute('''
    CREATE TABLE IF NOT EXISTS assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        due_date TEXT
    )
''')

# Create events table
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

if __name__ == "__main__":
    app.run(debug=True)
