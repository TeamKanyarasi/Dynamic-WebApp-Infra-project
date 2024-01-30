# Dynamic-WebApp-Infra-project

Developed a system that automatically manages the lifecycle of a web application hosted on  EC2 instances, monitors its health, and reacts to changes in traffic by scaling resources.Furthermore, administrators receive notifications regarding the infrastructure's health and scaling events.

## 1. Web Application Deployment: 

 - Using `boto3`: 
    - Created an S3 bucket to store web application's static files. 
    - Launched an EC2 instance and configured it as a web server (ex: Nginx).
    - Deployed the web application onto the EC2 instance. 

## 2. Load Balancing with ELB: 

 - Deployed an Application Load Balancer (ALB) using `boto3`. 
 - Registered the EC2 instance(s) as a `target group` with the ALB. 

## 3. Auto Scaling Group (ASG) Configuration: 

 - Using `boto3`, created an ASG with the deployed EC2 instance as a template. 
 - Configured scaling policies to scale in/out based on metrics like `CPU utilization`, `network traffic`. 

## 4. Lambda-based Health Checks & Management: 

 - Developed a Lambda function to periodically check the health of the web application through the ALB with the below implementations. 
 - If the health check fails consistently, the Lambda function should: 
    - Capture a snapshot of the failing instance for debugging purposes.
    - Terminate the problematic instance, allowing the ASG to replace it.
    - Send a notification through SNS to the administrators. 

## 5. S3 Logging & Monitoring: 

 - Configured the ALB to send access logs to the S3 bucket. 
 - Created a Lambda function that triggers when a new log is added to the S3 bucket. This function can analyze the log for suspicious activities (like potential DDoS attacks) or just high traffic. 
 - If any predefined criteria are met during the log analysis, the Lambda function sends a notification via SNS. 

## 6. SNS Notifications: 

 - Set up different SNS topics for different alerts (e.g., health issues, scaling events, high traffic). 
 - Integrated SNS with Lambda so that administrators can receive SMS or email notifications. 

## 7. Infrastructure Automation: 

 - Created a single script using `boto3` that: 
     - Deploys the entire infrastructure. 
     - Updates any component as required. 
     - Tears down everything when the application is no longer needed. 
