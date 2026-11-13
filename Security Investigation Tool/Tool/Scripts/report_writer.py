def write_report(report_filename, curdate, ioc_findings, auth_findings, ps_findings):
    with open(report_filename, "w", encoding="utf-8") as report:
        report.write("SECURITY INVESTIGATION REPORT\n")
        report.write(f"Generated: {curdate}\n")
        report.write("=" * 50 + "\n\n")

        report.write(f"Total IOC matches:           {len(ioc_findings)}\n")
        report.write(f"Total Auth alerts:           {len(auth_findings)}\n")
        report.write(f"Total PowerShell alerts:     {len(ps_findings)}\n")
        report.write(f"Total findings:              {len(ioc_findings + auth_findings + ps_findings)}\n")

        report.write("--- IOC Matches ---\n")
        for line in ioc_findings:
            report.write(line + "\n")

        report.write("\n--- Authentication Failures ---\n")
        for line in auth_findings:
            report.write(line + "\n")

        report.write("\n--- PowerShell Activity ---\n")
        for line in ps_findings:
            report.write(line + "\n")

        report.write("\n" + "=" * 50 + "\n")
        report.write("END OF REPORT\n")

    print(f"\n[+] Report saved to: {report_filename}")