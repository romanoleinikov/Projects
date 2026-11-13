from config import PS_LOG, ALL_KEYWORDS

def detect_mal_powershell(mal_ip, mal_path): 
    findings = []
    archive_seen = False

    with open(PS_LOG, "r", encoding="utf-8") as ps_file:
        for line in ps_file:
            for category, keywords in ALL_KEYWORDS.items():
                matched = [kw for kw in keywords if kw in line]
                if matched:
                    if category == "Collection":
                        archive_seen = True

                    if category == "Exfiltration" and archive_seen:
                        findings.append(f"[PowerShell - Exfiltration Chain Detected] Triggered by: {matched} | {line.strip()}")
                        break

                    ip_match = [ip for ip in mal_ip if ip in line]
                    if ip_match:
                        findings.append(f"[PowerShell - CRITICAL] Known malicious IP {ip_match} found | Triggered by: {matched} | {line.strip()}")
                        break

                    path_match = [path for path in mal_path if path in line]
                    if path_match:
                        findings.append(f"[PowerShell - CRITICAL] Known malicious path {path_match} found | Triggered by: {matched} | {line.strip()}")
                        break

                    findings.append(f"[PowerShell - {category}] Triggered by: {matched} | {line.strip()}")
                    break

    return findings