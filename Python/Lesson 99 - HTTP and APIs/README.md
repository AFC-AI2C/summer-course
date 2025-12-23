# HTTP and APIs

This repository provides a foundational understanding of the **HyperText Transfer Protocol (HTTP)** and how **Application Programming Interfaces (APIs)** enable communication between different software systems.


## 🎯 Lesson Objectives

* Understand the core rules and structure of the **HTTP protocol**.
* Identify common **HTTP methods** and **response status codes**.
* Explore how APIs facilitate data exchange between clients and servers.


## 🌐 The HTTP Protocol

Specified in RFC 1945, HTTP is the standard protocol for transferring data over the web. It relies on a request-response model between a client (like a browser) and a server.


### Core Rules

- **Client-Initiated:** The client always starts the communication; the server listens for requests.
- **One-to-One:** Each exchange consists of exactly one request and one corresponding response.
- **Stateless:** The server does not remember previous interactions, which is why "cookies" are often used to maintain session state.


## 📩 Anatomy of a Request & Response

An HTTP exchange is composed of three main parts: a start line, headers (metadata), and an optional body (the actual data).


### Example Exchange

- **Request:** `GET /test HTTP/1.1` followed by headers like `Host: example.com`.
- **Response:** `HTTP/1.1 200 OK` followed by server info and the content body (e.g., HTML or JSON).


## 🛠️ Methods and Status Codes

### Common Request Methods

Methods indicate the desired action to be performed on a resource:

- **`GET`**: Retrieve data from the server.
- **`POST`**: Submit new data to the server.
- **`HEAD`**: Same as GET but only transfers the status line and header section (no body).


### Response Status Codes

Standardized codes that indicate the result of the request:

- **200 OK**: The request succeeded.
- **201 Created**: The request succeeded and a new resource was created.
- **301 Moved Permanently**: The resource has been assigned a new permanent URI.
- **400 Bad Request**: The server could not understand the request.
- **403 Forbidden**: The server understood but refuses to authorize the request.
- **404 Not Found**: The server cannot find the requested resource.
- **500 Internal Server Error**: The server encountered an unexpected condition.


## 🔗 APIs and Connectivity

APIs use HTTP as a transport layer to allow different applications to "talk" to one another, typically exchanging data in formats like **JSON**.
