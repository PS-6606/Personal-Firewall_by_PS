# Building a Personal Firewall

## Overview

Personal Firewall is a Python-based cybersecurity project which simulates a simple Firewall. It also provides the ability to see which connections are being received by the port, to setup predefined security rules, log blocked traffic, and create security reports.

The project illustrates the concepts of packet filtering, access control, logging and security monitoring and also shows the basic concepts of firewalling.

---

## Objectives

* To be familiar with firewall rule management.
* Simulate network traffic filtering with respect to port numbers.
* Log any suspicious or blocked connection attempts.
* Track firewall statistics.
* Create security reports based on collected logs.
* Know fundamental cybersecurity monitoring skills.

---

## Features

### Port Filtering

The firewall checks if the port is:

* Allowed
* Blocked
* Not covered by any rule

### Rule Management

Firewall rules are saved in a JSON configuration file (`rules.json`), and are not hardcoded in the source code, allowing for editing without modifying the source.

### Security Logging

All blocked connection attempts are recorded in `logs.txt` with:

* Timestamp
* Port number
* Action taken

### Statistics Tracking

The firewall stores persistent statistics in `stats.json`:

* Total connections
* Allowed connections
* Blocked connections
* No-rule connections

### Security Reporting

Generate reports showing:

* Connection statistics
* Number of blocked attempts
* Most targeted port
* Recent blocked connections

### Service Identification

Common network ports are associated with service names like:

* HTTP
* HTTPS
* SSH
* FTP
* DNS
* MySQL
* RDP

---

## Project Structure

```text
Building-a-Personal-Firewall/
│
├── main.py
├── firewall.py
├── report.py
├── rules.json
├── stats.json
├── logs.txt
└── README.md
```

---

## Technologies Used

* Python 3
* JSON
* File Handling
* Datetime Module
* Collections Module

---

## How It Works

### 1. Check Port

A port number is entered by the user.

Example:

```text
Enter Port Number: 23

Port 23 (Telnet): BLOCKED
```

The firewall matches the port with the rules that are specified and acts accordingly.

---

### 2. View Firewall Rules

Lists all the ports that are allowed and denied and the services attached to them.

Example:

```text
Allowed Ports:
80 (HTTP)
443 (HTTPS)

Blocked Ports:
21 (FTP)
23 (Telnet)
22 (SSH)
```

---

### 3. Generate Security Report

Displays security statistics and recent activity.

Example:

```text
========== SECURITY REPORT ==========

Total Connections: 15
Allowed Connections: 6
Blocked Connections: 7
No Rule Connections: 2

Blocked Attempts Logged: 7

Most Targeted Port: 23

Recent Blocked Connections:
2026-06-03 15:10:20 | Port 23 | BLOCKED
```

---

## Installation

Clone this repository
Navigate to the project folder: cd Building_a_Personal_Firewall
Run the application: python main.py

## Skills Demonstrated

### Cybersecurity

* Firewall Concepts
* Access Control
* Security Monitoring
* Security Logging
* Network Services Awareness

### Programming

* Python Programming
* Modular Design
* JSON Configuration Management
* File Processing
* Exception Handling

### Networking

* Common Network Ports
* TCP/IP Services
* Port Filtering
* Service Identification

---

## Future Improvements

* Allows creating and removing rules dynamically.
* IP address filtering
* Real packet inspection
* Graphical User Interface (GUI)
* Traffic visualization dashboard
* Intrusion detection capabilities

---

## Learning Outcomes

The following ideas were highlighted through this project:

* Firewall architecture
* Network security fundamentals
* Logging and monitoring
* Security reporting
* Configuration management
* Python application development

---