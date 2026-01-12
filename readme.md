# Site Sentry - Network Monitor Tool

A lightweight Network Monitoring tool built with Python and Flask. It allows users to check the latency and uptime status of any website and maintains a history of checks in a CSV log.

## Features
- **Real-time Latency Check:** Measures response time in milliseconds.
- **Status Monitoring:** Identifies if a site is ONLINE or OFFLINE.
- **History Dashboard:** Visualizes past checks in a tabular format.
- **CSV Logging:** Automatically saves all checks to a persistent log file.

## Tech Stack
- **Backend:** Python, Flask
- **Networking:** Requests Library
- **Frontend:** HTML, Jinja2, CSS

## How to Run locally
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt