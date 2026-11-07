# parses SSH auth logs to count failed login attempts by IP
failed_attempts = {}
with open("sample-auth.log", "r") as file:
    for line in file:
        # the if statement makes sure it only checks lines that have Failed password
        if "Failed password" in line:
            ip = line.split()[-3]
            failed_attempts[ip] = failed_attempts.get(ip,0) + 1
for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"ALERT: Suspicious activity from {ip} ({count} failed attempts)")

