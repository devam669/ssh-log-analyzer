# SSH Brute-Force Log Analyzer

A python script that analyzes linux SSH authentication logs to detect brute-force login attempts.

## How It Works
- **Log Parsing:** Reads server authentication logs line by line.
- **Threat Filtering:** Isolates `"Failed password"` entries while ignoring normal, successful user logins.
- **IP Extraction & Tracking:** Extracts source IP addresses and uses a Python dictionary to tally failed attempts per IP.
- **Automated Alerting:** Flags any IP address that reaches 3 or more failed login attempts.

## Example Output
```text
ALERT: Suspicious activity from 192.168.1.45 (3 failed attempts)
```

## How to Run
1. Ensure **Python 3** is installed on your machine.
2. Download or clone this repository.
3. Run the script in your terminal:
   ```bash
   python analyzer.py
   ```
