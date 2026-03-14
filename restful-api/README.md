# RESTful API

## Task 0: Basics of HTTP/HTTPS

---

### 1. Differences Between HTTP and HTTPS

| Feature | HTTP | HTTPS |
|---|---|---|
| Full Name | HyperText Transfer Protocol | HyperText Transfer Protocol Secure |
| Encryption | None — data is sent in plain text | Encrypted via SSL/TLS |
| Port | 80 | 443 |
| Security | Vulnerable to eavesdropping and man-in-the-middle attacks | Protected against interception and tampering |
| Certificate | Not required | Requires an SSL/TLS certificate from a Certificate Authority |
| Data Integrity | Not guaranteed | Guaranteed — data cannot be altered in transit |
| Use Case | Non-sensitive public content | Banking, login pages, e-commerce, any sensitive data |

**Summary:** HTTP transfers data in plain text, making it readable by anyone who intercepts the traffic. HTTPS wraps the same HTTP protocol inside an SSL/TLS encryption layer, ensuring confidentiality, data integrity, and server authentication. The "S" stands for **Secure**.

---

### 2. Structure of an HTTP Request and Response

#### HTTP Request

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Accept-Language: en-US
Connection: keep-alive
```

| Part | Description |
|---|---|
| **Request Line** | Method + Path + HTTP version (e.g., `GET /index.html HTTP/1.1`) |
| **Headers** | Key-value metadata (Host, User-Agent, Accept, etc.) |
| **Blank Line** | Separates headers from the body |
| **Body** (optional) | Data sent with the request (used in POST, PUT, PATCH) |

#### HTTP Response

```
HTTP/1.1 200 OK
Date: Sat, 14 Mar 2026 10:00:00 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 1024
Connection: keep-alive

<html>
  <body>Hello, World!</body>
</html>
```

| Part | Description |
|---|---|
| **Status Line** | HTTP version + status code + reason phrase (e.g., `HTTP/1.1 200 OK`) |
| **Headers** | Metadata about the response (Content-Type, Content-Length, etc.) |
| **Blank Line** | Separates headers from the body |
| **Body** | The actual content returned (HTML, JSON, image data, etc.) |

---

### 3. Common HTTP Methods

| Method | Description | Use Case |
|---|---|---|
| **GET** | Retrieves data from the server without modifying it | Fetching a web page or requesting data from an API |
| **POST** | Sends data to the server to create a new resource | Submitting a registration form or creating a new user |
| **PUT** | Replaces an existing resource entirely with new data | Updating a user's full profile |
| **PATCH** | Partially updates an existing resource | Changing only a user's email address |
| **DELETE** | Removes a specified resource from the server | Deleting a blog post or a user account |
| **HEAD** | Same as GET but returns only headers, no body | Checking if a resource exists or was modified |
| **OPTIONS** | Describes the communication options for the target resource | CORS preflight requests to check allowed methods |

---

### 4. Common HTTP Status Codes

| Status Code | Name | Description | Scenario |
|---|---|---|---|
| **200** | OK | The request succeeded | Successfully fetching a web page or API data |
| **201** | Created | A new resource was successfully created | After a POST request creates a new user |
| **301** | Moved Permanently | The resource has been permanently moved to a new URL | A website migrating from HTTP to HTTPS |
| **400** | Bad Request | The server could not understand the request due to invalid syntax | Sending malformed JSON to an API endpoint |
| **401** | Unauthorized | Authentication is required and has failed or not been provided | Accessing a protected API route without a token |
| **403** | Forbidden | The server understood the request but refuses to authorize it | A regular user trying to access an admin-only page |
| **404** | Not Found | The requested resource could not be found on the server | Visiting a page that has been deleted or never existed |
| **500** | Internal Server Error | The server encountered an unexpected condition | A bug in the server-side code causing a crash |
