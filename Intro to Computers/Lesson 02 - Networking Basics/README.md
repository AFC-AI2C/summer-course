# Lesson 02 - Network Basics

This repository covers the fundamental principles of networking, focusing on how data is transmitted across the internet and the standardized models that govern these communications.


## 🎯 Lesson Objectives

* Explain how **network traffic** is sent over the internet.
* Describe the **OSI Model** and its seven layers.
* Understand the **TCP/IP Model** and how it relates to the OSI Model.


## 🏗️ The OSI Model

The **Open Systems Interconnection (OSI)** model is a conceptual framework used to understand network interactions in seven distinct layers.

| Layer | Name | Function |
| --- | --- | --- |
| **7** | **Application** | Human-computer interaction layer where applications access network services. |
| **6** | **Presentation** | Ensures data is in a usable format and is where data encryption occurs. |
| **5** | **Session** | Maintains connections and controls ports and sessions. |
| **4** | **Transport** | Transmits data using protocols like TCP and UDP. |
| **3** | **Network** | Decides which physical path the data will take. |
| **2** | **Data Link** | Defines the format of data on the network. |
| **1** | **Physical** | Transmits raw bit streams over the physical medium. |


## 🌐 The TCP/IP Model

The TCP/IP model is a condensed version of the OSI model used for the actual implementation of the internet.

### Layers and Protocol Data Units (PDUs)

* **Application Layer:** Combines OSI layers 5-7; data at this layer is referred to simply as **Data**.
* **Transport Layer:** Corresponds to OSI layer 4; data is organized into **Segments**.
* **Internet Layer:** Corresponds to OSI layer 3; data is organized into **Packets**.
* **Network Access Layer:** Combines OSI layers 1-2; data is organized into **Frames**.


## 📦 Key Networking Concepts

### IP Addressing

* **IPv4:** The most common addressing scheme, consisting of four numbers (0-255) separated by periods (e.g., `192.168.1.1`).
* **IPv6:** Developed to provide more addresses; uses a 128-bit hexadecimal format (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).


### Communication Protocols

* **TCP (Transmission Control Protocol):** Connection-oriented and reliable; ensures data arrives in order.
* **UDP (User Datagram Protocol):** Connectionless and "unreliable"; faster but does not guarantee delivery (commonly used for streaming).
* **ICMP:** Used for network diagnostics, such as the `ping` command.


### Common Port Numbers

Ports allow a single IP address to host multiple services:

* **HTTP (80):** Standard web traffic.
* **HTTPS (443):** Secure web traffic.
* **SSH (22):** Secure remote console access.
* **DNS (53):** Resolves domain names to IP addresses.


## 🚦 Traffic Management

* **Unicast:** Traffic sent from one host to one specific destination.
* **Broadcast:** Traffic sent from one host to all other hosts on the network.
* **Multicast:** Traffic sent from one host to a specific group of interested hosts.
