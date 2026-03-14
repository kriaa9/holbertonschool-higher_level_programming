# Task 1: Consume Data from an API Using Command Line Tools (curl)

## Overview

This task demonstrates how to use `curl` to interact with RESTful APIs from the command line. curl is a powerful tool for testing, debugging, and prototyping API requests.

---

## Part 1: Installing and Basic Interaction with curl

### Verify curl Installation

```bash
curl --version
```

**Output:**

```
curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd
```

**Result:** ✅ curl is installed and available with support for multiple protocols including HTTP/HTTPS.

---

### Fetch Content from a Webpage

```bash
curl http://example.com
```

**Output:**

```html
<!doctype html><html lang="en"><head><title>Example Domain</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}
h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style></head>
<body><div><h1>Example Domain</h1>
<p>This domain is for use in documentation examples without needing permission.
Avoid use in operations.</p>
<p><a href="https://iana.org/domains/example">Learn more</a></p></div></body></html>
```

**Result:** ✅ Successfully retrieved the HTML content of a webpage.

---

## Part 2: Fetching Data from an API

### Retrieve Posts from JSONPlaceholder

```bash
curl https://jsonplaceholder.typicode.com/posts
```

**Output (first 10 posts):**

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis"
  },
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur"
  },
  ...
]
```

**Data Structure of Each Post:**

- `userId`: The ID of the user who wrote the post (integer)
- `id`: The unique identifier of the post (integer)
- `title`: The title of the post (string)
- `body`: The content/body of the post (string)

**Result:** ✅ Successfully retrieved JSON array of 100 posts from the API. Each post contains userId, id, title, and body attributes.

---

## Part 3: Using Headers and Other curl Options

### Fetch Only Response Headers

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

**Output:**

```
HTTP/2 200
date: Sat, 14 Mar 2026 07:17:19 GMT
content-type: application/json; charset=utf-8
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
server: cloudflare
vary: Origin, Accept-Encoding
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1773262958
cf-cache-status: HIT
alt-svc: h3=":443"; ma=86400
```

**Key Headers Explained:**

| Header | Value | Meaning |
|--------|-------|---------|
| `HTTP/2 200` | Status Code | Request succeeded |
| `content-type` | `application/json; charset=utf-8` | Response is JSON format |
| `cache-control` | `max-age=43200` | Cache for 12 hours (43200 seconds) |
| `x-ratelimit-limit` | 1000 | API allows 1000 requests per period |
| `x-ratelimit-remaining` | 999 | 999 requests remaining before rate limit |

**Result:** ✅ Successfully retrieved headers without the body. Useful for checking status codes, content types, and caching policies.

---

### Make a POST Request

```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

**Output:**

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

**Explanation:**

- `-X POST`: Specifies HTTP method as POST (create/submit data)
- `-d "title=foo&body=bar&userId=1"`: Sends form-encoded data in the request body
  - `title=foo`: Title of the new post
  - `body=bar`: Content of the new post
  - `userId=1`: User ID who is creating the post

**Result:** ✅ Successfully created a new post. The server responded with the created post including an auto-generated `id` of 101. (Note: JSONPlaceholder doesn't actually store the data; it's a mock API for testing.)

---

## Key curl Flags and Options

| Flag | Purpose | Example |
|------|---------|---------|
| `-I` / `--head` | Fetch only headers, no response body | `curl -I https://api.example.com/data` |
| `-X` / `--request` | Specify HTTP method (GET, POST, PUT, DELETE, etc.) | `curl -X DELETE https://api.example.com/posts/1` |
| `-d` / `--data` | Send data in request body (for POST/PUT) | `curl -d "param=value" https://api.example.com/posts` |
| `-H` / `--header` | Set custom header | `curl -H "Authorization: Bearer token" https://api.example.com` |
| `-v` / `--verbose` | Show detailed request/response info | `curl -v https://api.example.com` |
| `-o` / `--output` | Save response to a file | `curl -o response.json https://api.example.com` |
| `-L` / `--location` | Follow redirects | `curl -L https://api.example.com` |

---

## Learning Outcomes

✅ **Installed and verified curl** — Version 8.5.0 with multiple protocol support
✅ **Fetched webpage content** — Successfully retrieved HTML from example.com
✅ **Consumed API data** — Retrieved JSON array of 100 posts from JSONPlaceholder
✅ **Inspected HTTP headers** — Viewed response metadata including content-type, caching, and rate limits
✅ **Made POST requests** — Successfully created a new resource and received auto-generated ID

---

## Summary

`curl` is a versatile command-line tool for interacting with web services and APIs. The key takeaways:

1. **GET requests** (default) retrieve data without modifying anything
2. **POST requests** (with `-X POST`) submit new data to create resources
3. **Headers** can be inspected independently to understand server behavior
4. **Status codes** and metadata help diagnose API issues
5. **JSON output** can be formatted with tools like `jq` for better readability

This foundation enables developers to quickly prototype and test APIs before integrating them into their applications.
