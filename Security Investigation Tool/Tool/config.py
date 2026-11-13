# =========== File Paths ==================#
AUTH_LOG    = "auth.log"
ACCESS_LOG  = "access.log"
PS_LOG      = "powershell_log.txt"
IOC_FILE    = "ioc.txt"

# =========== Thresholds ==================#
LOGIN_THRESHOLD = 5

# =========== PowerShell Keywords ==================#
ALL_KEYWORDS = {
    "Suspicious Execution": ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-EncodedCommand'],
    "Reconnaissance":       ['whoami', 'ipconfig', 'net user'],
    "Collection":           ['Compress-Archive'],
    "Exfiltration":         ['-Upload', 'Invoke-WebRequest']
}