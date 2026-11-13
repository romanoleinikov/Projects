import re
from config import IOC_FILE, ACCESS_LOG

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

def load_iocs():
    mal_ip, mal_path = [], []
    with open(IOC_FILE, "r", encoding="utf-8") as ioc:
        for line in ioc:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if "/" in line:
                mal_path.append(line)
            elif pattern.search(line):
                mal_ip.append(line)
    return mal_ip, mal_path

def detect_ioc_matches(mal_ip, mal_path):
    findings = []
    with open(ACCESS_LOG, "r", encoding="utf-8") as access_file:
        for line in access_file:
            for ip in mal_ip:
                if ip in line:
                    findings.append(f"[IOC] Malicious IP detected: {line.strip()}")
            for path in mal_path:
                if path in line:
                    findings.append(f"[IOC] Malicious path detected: {line.strip()}")
    return findings