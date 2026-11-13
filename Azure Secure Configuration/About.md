# Project overview
This project focused on securing an Azure-hosted web application by combining network segmentation, controlled administrative access, host hardening, encryption, monitoring, logging and backup measures.

The environment used an Azure Virtual Network with separate VM and Web Application Firewall subnets. An Azure Application Gateway with Web Application Firewall (WAF) was placed in front of the web server, while an Azure SQL Database was configured to accept connections only from the VM subnet, as described in the report.
### Objectives
- Separate the web application workload from the public-facing application gateway.
- Restrict network traffic through Network Security Group (NSG) rules and host-level firewall rules.
- Strengthen SSH authentication and Linux server access controls.
- Protect data in transit and at rest.
- Configure system updates, backups, logging, auditing and monitoring.
- Test whether the WAF blocked requests identified as potentially malicious.
### Outcome
- A database connection was successful from the VM, while the report shows that access was restricted to that network location.
- The web application was accessible over HTTP and HTTPS through the Application Gateway.
- WAF test requests containing potentially malicious input were blocked with HTTP 403 responses, while normal requests were allowed.
- Fail2ban logs showed 82 IP addresses banned during the observed day.
- The unattended-upgrades service was active and had performed updates.
- Backup files and their corresponding log entries were created.
- rsyslog, log rotation and auditd activity were checked through their status information and logs.
