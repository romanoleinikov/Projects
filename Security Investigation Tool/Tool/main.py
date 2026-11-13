import sys
import datetime

sys.path.append("scripts")

from ioc_detection      import load_iocs, detect_ioc_matches
from auth_detection     import detect_failed_logins
from powershell_detection import detect_mal_powershell
from report_writer      import write_report


curdate         = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_filename = f"investigation_report_{curdate}.txt"


if __name__ == "__main__":
    mal_ip, mal_path = load_iocs()

    ioc_findings  = detect_ioc_matches(mal_ip, mal_path)
    auth_findings = detect_failed_logins(mal_ip)
    ps_findings = detect_mal_powershell(mal_ip, mal_path)


    write_report(report_filename, curdate, ioc_findings, auth_findings, ps_findings)