# Project Description 
Project involved designing and implementing an AWS environment for WinLocal's web application and competition-entry database. The architecture was intended to provide controlled network access, separate public-facing components from private resources, and support availability and recovery as application demand changes.
### Objectives 
- Build a segmented AWS network for the web application and its database.
- Restrict administrative access to the web server through a bastion host.
- Make the website available through an Application Load Balancer.
- Provide database storage for competition entries, including user names and addresses.
- Support scaling and instance recovery through reusable machine images and an Auto Scaling Group.
- Monitor defined conditions using CloudWatch alarms
### Outcome
The report demonstrates a working website accessed through the Application Load Balancer, connectivity to the MySQL database, and administrative access to the web server through the bastion host. It also documents the AMI and Auto Scaling setup and tests of CloudWatch alarm behaviour.
