#!/usr/bin/python3
"""Task 2: Dynamic template with loops and conditions."""

import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
ITEMS_FILE = BASE_DIR / "items.json"


def load_items():
    """Read items from JSON file and return a list."""
    try:
        with ITEMS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    items = data.get("items", [])
    if isinstance(items, list):
        return items
    return []


@app.route("/")
def home():
    """Render home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Render about page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Render contact page."""
    return render_template("contact.html")


@app.route("/items")
def items():
    """Render items page with dynamic content."""
    return render_template("items.html", items=load_items())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
