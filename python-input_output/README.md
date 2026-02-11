# Python - Input/Output

This project covers file handling and JSON serialization/deserialization in Python.

## Learning Objectives

- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON
- What is serialization and deserialization
- How to convert Python data structures to/from JSON
- How to access command line parameters in a Python script

## Requirements

- Python 3.8.5
- pycodestyle 2.7.*
- All files must be executable
- All files must end with a new line

## Files

| File | Description |
|------|-------------|
| `0-read_file.py` | Function that reads a text file and prints to stdout |
| `1-write_file.py` | Function that writes a string to a text file |
| `2-append_write.py` | Function that appends a string to a text file |

## Usage

```python
# Reading a file
read_file = __import__('0-read_file').read_file
read_file("my_file.txt")

# Writing to a file
write_file = __import__('1-write_file').write_file
nb_characters = write_file("my_file.txt", "Hello World!\n")

# Appending to a file
append_write = __import__('2-append_write').append_write
nb_characters_added = append_write("my_file.txt", "More text\n")
```

## Author

Holberton School
