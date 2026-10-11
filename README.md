# Network Scanner

A Python-based TCP port scanner built to explore network security, socket programming, and basic service identification.

This project is a hands-on learning tool designed to help me understand how network services expose themselves through TCP ports and how to perform basic checks on systems I own or have permission to assess.

## Features

- **IP address validation** using Python's `ipaddress` module.
- **Custom port ranges** so users can choose which TCP ports to scan.
- **TCP port scanning** using Python's `socket` module.
- **Connection result handling** to distinguish open ports, refused connections, and other errors.
- **Basic service detection** through a separate `service_detection.py` module.
- **HTTP response inspection** to identify HTTP responses and display a response banner.
- **Resource cleanup** using `try/finally` to close sockets.
- **Git version control** with generated files and the virtual environment excluded through `.gitignore`.

## Technologies

- Python
- TCP/IP networking
- Python sockets
- Git and GitHub
- Kali Linux / Linux terminal

## Project Structure

```text
network-scanner/
├── scanner.py
├── service_detection.py
├── assessment.py
├── README.md
├── .gitignore
└── .venv/                 # Local virtual environment (ignored by Git)
```

## Requirements

- Python 3
- A terminal
- Permission to scan the target system

The scanner uses Python's standard library, so no third-party packages are currently required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/innostan/network-scanner.git
cd network-scanner
```

### 2. Run the scanner

```bash
python3 scanner.py
```

### 3. Enter a target and port range

When prompted, enter an IP address, followed by the starting and ending TCP port numbers.

For example, to test a local HTTP server listening on port 8000:

```text
Enter an IP address (or q to quit): 127.0.0.1
enter a starting port number : 8000
enter ending port number. 8000
```

The scanner should report port 8000 as open when the test server is running.

To exit, enter `q` at the IP address prompt.

## Testing Locally

You can create a local HTTP service for testing without scanning another machine.

In a second terminal, run:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Keep the server running, then start the scanner in your project terminal and scan `127.0.0.1` on port `8000`.

Stop the test server with `Ctrl + C` when finished.

## Current Limitations

- The scanner performs TCP connection checks; it is not a full network vulnerability scanner.
- Service identification is basic and currently relies on an HTTP probe rather than protocol-specific detection for every service.
- Open ports do not automatically mean a vulnerability exists.
- Results may vary depending on network conditions, firewall rules, and service configuration.
- The tool does not yet generate structured assessment reports.

## Planned Improvements

- Add protocol-aware service detection.
- Improve socket error handling and scan reliability.
- Add timestamps and structured scan results.
- Introduce basic risk classification with clear explanations.
- Export results to a report file.
- Improve command-line usability and documentation.

## Responsible Use

Use this tool only against systems you own or have explicit permission to assess. Start with localhost or a controlled lab environment. Do not use it to scan third-party systems without authorization.

## Learning Objective

This project is part of my practical journey into network security and defensive security engineering. The goal is to build a clear understanding of how services are exposed on networks and develop useful tools for authorized security assessments.
