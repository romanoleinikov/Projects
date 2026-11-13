import re
from collections import defaultdict
from config import AUTH_LOG, LOGIN_THRESHOLD

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

def detect_failed_logins(mal_ip): 
    ip_attempts = defaultdict(int)
    findings = []

    with open(AUTH_LOG, "r", encoding="utf-8") as auth_file:
        for line in auth_file:
            if "failed password" in line.lower():
                match = pattern.search(line)
                if match:
                    ip = match.group()
                    ip_attempts[ip] += 1

    for ip, count in ip_attempts.items():
        if count > LOGIN_THRESHOLD:
            if ip in mal_ip:  
                findings.append(f"[Auth - CRITICAL] Brute-force from KNOWN MALICIOUS IP {ip} ({count} failed attempts)")
            else:
                findings.append(f"[Auth] Possible brute-force from IP {ip} ({count} failed attempts)")

    return findings