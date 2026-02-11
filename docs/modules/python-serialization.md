# Module: python-serialization

## 1. Executive Summary

This is the capstone module of the curriculum, integrating OOP, file I/O, and data interchange into **multi-format serialization** and **network communication**. Students implement serialization using JSON, Pickle, CSV, and XML formats, and transmit serialized data over TCP sockets. This module directly prepares students for REST API development, data pipeline construction, and microservice architecture — the core responsibilities of backend engineers.

---

## 2. Deep Concept Breakdown

### 2.1 JSON Serialization

**Formal definition:** JSON serialization converts Python objects to a platform-independent text format for storage or transmission.

```python
import json

def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, 'r') as f:
        return json.load(f)
```

**Strengths:** Human-readable, universally supported, language-agnostic.
**Weaknesses:** Cannot represent all Python types (datetime, set, custom objects), no type preservation for tuples.

### 2.2 Pickle Serialization

**Formal definition:** Pickle is Python's native binary serialization protocol. It can serialize almost any Python object, including custom classes.

```python
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
```

**Strengths:** Preserves Python type information, handles complex object graphs, supports custom serialization via `__getstate__`/`__setstate__`.
**Weaknesses:** Python-specific (not interoperable), **security risk** (arbitrary code execution on `pickle.load()`), version-sensitive.

**⚠️ Security warning:** Never unpickle data from untrusted sources. `pickle.load()` can execute arbitrary code, making it a vector for remote code execution attacks.

### 2.3 CSV Serialization

**Formal definition:** CSV (Comma-Separated Values) is a tabular data format where each line represents a record and fields are separated by delimiters.

```python
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        with open("data.json", 'w') as json_file:
            json.dump(data, json_file)
        return True
    except FileNotFoundError:
        return False
```

**`csv.DictReader`:** Automatically uses the first row as field names, returning each row as a dictionary.

### 2.4 XML Serialization

**Formal definition:** XML (eXtensible Markup Language) is a hierarchical data format using tags for structure.

```python
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
```

**Limitation:** All values become strings during XML serialization — type information is lost. In production, XML Schema (XSD) or explicit type attributes would be used to preserve types.

**Security consideration:** `xml.etree.ElementTree` is vulnerable to XML bomb attacks (billion laughs). Use `defusedxml` for untrusted input.

### 2.5 Network Serialization with Sockets

**Formal definition:** TCP sockets provide reliable, ordered byte-stream communication between processes. Combined with JSON serialization, they enable structured data exchange over networks.

```python
import socket
import json

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    data = conn.recv(1024).decode('utf-8')
    received_data = json.loads(data)
    conn.close()
    server_socket.close()
    return received_data

def send_data(data, host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    json_data = json.dumps(data)
    client_socket.sendall(json_data.encode('utf-8'))
    client_socket.close()
```

**Limitations in this implementation:**
- Single-connection server (not concurrent)
- No error handling for connection failures
- Fixed buffer size (1024 bytes) — large payloads may be truncated
- No message framing — multiple messages may be merged or split

---

## 3. Task-Level Static Analysis

### Task: task_00_basic_serialization.py

- **Problem statement:** JSON serialization/deserialization for Python dictionaries.
- **Design approach:** Two utility functions using `json.dump()` and `json.load()` with context managers.
- **OOP principles:** None — utility functions.
- **Control flow:** Linear — open, write/read, close.
- **Edge-case coverage:** No error handling for missing files or invalid JSON.
- **Time complexity:** O(n) where n = data size.
- **Real-world analogy:** REST API response caching — save JSON responses to disk for offline use.

### Task: task_01_pickle.py

- **Problem statement:** Custom object serialization using Pickle.
- **Design approach:** `CustomObject` class with `serialize()` instance method and `deserialize()` class method.
- **OOP principles:** Self-serialization, class methods for deserialization (factory pattern).
- **Edge-case coverage:** Both methods catch broad `Exception` and return `None` on failure.
- **Time complexity:** O(n) for serialization.
- **Potential improvements:** Bare `except Exception` silences errors. Should catch specific exceptions or log the error.
- **Security concerns:** `pickle.load()` can execute arbitrary code from tampered files.
- **Real-world analogy:** Saving/loading machine learning model weights (scikit-learn uses pickle).

### Task: task_02_csv.py

- **Problem statement:** Convert CSV files to JSON format.
- **Design approach:** `csv.DictReader` to parse CSV, `json.dump()` to write JSON.
- **Control flow:** Read CSV → convert to list of dicts → write JSON.
- **Edge-case coverage:** Catches `FileNotFoundError`, returns boolean success.
- **Time complexity:** O(n) where n = number of rows.
- **Potential improvements:** Hard-coded output filename `"data.json"` limits flexibility.
- **Real-world analogy:** ETL pipeline step — transforming CSV data exports into JSON for API consumption.

### Task: task_03_xml.py

- **Problem statement:** XML serialization/deserialization for dictionaries.
- **Design approach:** `ElementTree` for building and parsing XML trees.
- **Edge-case coverage:** ⚠️ No error handling for file I/O or malformed XML.
- **Time complexity:** O(n) where n = dictionary size.
- **Potential improvements:** Add type preservation, error handling, and use `defusedxml` for security.
- **Real-world analogy:** SOAP API request/response handling, configuration file management.

### Task: task_04_net.py

- **Problem statement:** Client-server communication with JSON serialization over TCP sockets.
- **Design approach:** Server binds/listens/accepts/receives; Client connects/sends.
- **Control flow:** Server blocks on `accept()`, client connects, sends JSON, both close.
- **Edge-case coverage:** ⚠️ No error handling for connection failures, timeouts, or partial receives.
- **Time complexity:** O(n) for data serialization + network latency.
- **Potential improvements:** Add timeouts, error handling, message framing, multi-client support.
- **Security concerns:** No input validation on received data; no size limits on received messages.
- **Real-world analogy:** Simplified HTTP request/response cycle — JSON payload over TCP.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Encapsulation | ✅ | `task_01_pickle.py` — `CustomObject` with serialize/deserialize |
| Factory Method | ✅ | `task_01_pickle.py` — `@classmethod deserialize()` |
| Self-Serialization | ✅ | `task_01_pickle.py` — objects serialize themselves |
| Strategy Pattern (implicit) | ✅ | Multiple serialization formats for the same data |
| Client-Server | ✅ | `task_04_net.py` — socket communication |
| ETL Pipeline | ✅ | `task_02_csv.py` — Extract (CSV) → Transform → Load (JSON) |
| Defensive Programming | ⚠️ | Present in `task_01_pickle.py` and `task_02_csv.py`; absent in `task_03_xml.py` and `task_04_net.py` |

---

## 5. Built-ins & Keywords Deep Dive

### `json` module

```python
import json

# Serialization
json.dumps(obj)                    # Object → JSON string
json.dumps(obj, indent=4)         # Pretty-printed
json.dump(obj, file)               # Object → JSON file

# Deserialization
json.loads(json_string)            # JSON string → Object
json.load(file)                    # JSON file → Object

# Custom encoder for unsupported types
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

json.dumps(data, cls=CustomEncoder)
```

### `pickle` module

```python
import pickle

# Serialization
pickle.dumps(obj)                  # Object → bytes
pickle.dump(obj, file)             # Object → binary file

# Deserialization
pickle.loads(bytes_data)           # bytes → Object
pickle.load(file)                  # binary file → Object
```

### `csv` module

```python
import csv

# Reading
with open("data.csv") as f:
    reader = csv.DictReader(f)      # First row = headers
    for row in reader:
        print(row["name"])          # Access by column name

# Writing
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})
```

### `xml.etree.ElementTree`

```python
import xml.etree.ElementTree as ET

# Building XML
root = ET.Element("root")
child = ET.SubElement(root, "child")
child.text = "value"
child.set("attribute", "attr_value")

# Writing
tree = ET.ElementTree(root)
tree.write("output.xml")

# Parsing
tree = ET.parse("data.xml")
root = tree.getroot()
for child in root:
    print(child.tag, child.text)
```

### `socket` module

```python
import socket

# Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(5)
conn, addr = server.accept()
data = conn.recv(1024)
conn.sendall(b"Response")
conn.close()

# Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))
client.sendall(b"Request")
response = client.recv(1024)
client.close()
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. Compare JSON, Pickle, CSV, and XML serialization formats. When would you use each?
2. Why is `pickle.load()` a security risk? What alternatives exist for untrusted data?
3. What is the difference between `json.dump()` and `json.dumps()`?
4. Explain TCP vs UDP sockets. Why does this module use TCP?
5. What is message framing in network programming? Why is it needed when using TCP sockets?

### Practical Coding Questions

1. Write a custom JSON encoder that handles `datetime`, `Decimal`, `set`, and `bytes` types.
2. Implement a thread-safe TCP server that handles multiple concurrent clients, each sending JSON messages.
3. Create a data pipeline that reads CSV, transforms the data, and outputs both JSON and XML.
4. Write a function that deep-compares two JSON files and returns a diff object describing all changes.
5. Implement a simple key-value store server using sockets — supporting `GET key`, `SET key value`, and `DELETE key` commands.

### Debugging Scenarios

1. A client sends a large JSON payload (10MB) over a socket, but the server only receives 1024 bytes. The parsed JSON is invalid. Explain the issue and fix it with message framing.
2. A developer pickles an object from module `app.models.User`, then tries to unpickle it in a script where the module is `models.User`. `ModuleNotFoundError` is raised. Explain why and how to fix it.

### System Design Question

1. Design a data synchronization system between a mobile app and a backend server. Requirements: (a) the mobile app stores data locally as JSON files, (b) changes are sent to the server as JSON over HTTP/sockets, (c) the server stores data in a database, (d) conflicts must be detected and resolved. What serialization format would you use at each layer? How would you handle schema evolution? What error handling and retry logic would you implement?
