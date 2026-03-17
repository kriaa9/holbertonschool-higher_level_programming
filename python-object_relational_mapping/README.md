# Python - Object-relational mapping

This project links two great worlds: Databases and Python! It uses the `MySQLdb` module to connect to a MySQL database and perform queries using Python scripts, and later introduces `SQLAlchemy`, an Object-Relational Mapper (ORM).

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements

- Python 3.8+
- MySQLdb module (`pip install mysqlclient`)
- SQLAlchemy module (`pip install SQLAlchemy`)
- MySQL 8.0
- All scripts are executable
- All scripts use `if __name__ == "__main__":` guard

## Files

| File | Description |
|------|-------------|
| `0-select_states.py` | Lists all states from the database `hbtn_0e_0_usa` |
