#!/usr/bin/python3
"""Task 4: Display product data from JSON, CSV, or SQLite."""

import csv
import json
import sqlite3
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "products.json"
CSV_FILE = BASE_DIR / "products.csv"
DB_FILE = BASE_DIR / "products.db"


SAMPLE_PRODUCTS = [
    (1, "Laptop", "Electronics", 799.99),
    (2, "Coffee Mug", "Home Goods", 15.99)
]


def _to_int(value):
    """Convert value to int when possible."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _normalize_product(product):
    """Normalize product object keys and value types."""
    return {
        "id": _to_int(product.get("id")),
        "name": product.get("name", ""),
        "category": product.get("category", ""),
        "price": product.get("price", "")
    }


def _initialize_database():
    """Create database and seed initial rows when table is empty."""
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
            """
        )
        cursor.execute("SELECT COUNT(*) FROM Products")
        row_count = cursor.fetchone()[0]
        if row_count == 0:
            cursor.executemany(
                "INSERT INTO Products (id, name, category, price) VALUES (?, ?, ?, ?)",
                SAMPLE_PRODUCTS
            )
        connection.commit()


def read_products_from_json():
    """Read products from JSON file."""
    try:
        with JSON_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if isinstance(data, dict):
        data = data.get("products", [])

    if not isinstance(data, list):
        return []

    products = []
    for item in data:
        if isinstance(item, dict):
            products.append(_normalize_product(item))
    return products


def read_products_from_csv():
    """Read products from CSV file."""
    try:
        with CSV_FILE.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return [_normalize_product(row) for row in reader]
    except FileNotFoundError:
        return []


def read_products_from_sql():
    """Read products from SQLite database."""
    try:
        _initialize_database()
        with sqlite3.connect(DB_FILE) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                "SELECT id, name, category, price FROM Products"
            ).fetchall()
    except sqlite3.Error as error:
        return [], f"Database error: {error}"

    return [dict(row) for row in rows], None


def _filter_products(products, product_id):
    """Filter products by id query parameter."""
    wanted_id = _to_int(product_id)
    if wanted_id is None:
        return []
    return [product for product in products if product.get("id") == wanted_id]


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


@app.route("/products")
def products():
    """Render product list from selected data source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        products_list = read_products_from_json()
    elif source == "csv":
        products_list = read_products_from_csv()
    elif source == "sql":
        products_list, error = read_products_from_sql()
        if error is not None:
            return render_template("product_display.html", products=[], error=error)
    else:
        return render_template(
            "product_display.html", products=[], error="Wrong source"
        )

    if product_id is not None:
        products_list = _filter_products(products_list, product_id)
        if not products_list:
            return render_template(
                "product_display.html", products=[], error="Product not found"
            )

    return render_template("product_display.html", products=products_list, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
