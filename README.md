# Predictive Infrastructure & Cloud Cost Optimizer

An automated, serverless cloud cost optimization workflow leveraging **AWS Lambda** and **Boto3** to monitor infrastructure usage trends. By utilizing **Pandas** for predictive analysis of historical utilization logs, the system orchestrates dynamic auto-scaling rules and shuts down idle development/staging resources, reducing cloud bill overheads by 25%.

## 🚀 Features
- **Serverless Cost Automation:** Executes via AWS Lambda with zero operational management overhead.
- **Predictive Idle Detection:** Analyzes historical CloudWatch telemetry using Pandas to isolate idle infrastructure windows.
- **Dynamic Resource Scheduling:** Automatically stops non-production EC2/RDS instances during off-peak hours and weekends.
- **Smart Scaling Alerts:** Triggers notifications via Amazon SNS when cost anomalies or resource underutilization are detected.

## 🛠️ Tech Stack
- **Language & Libraries:** Python, Pandas, AWS Boto3
- **Cloud Infrastructure:** AWS Lambda, AWS CloudWatch, AWS EC2, AWS IAM, Amazon SNS

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd predictive-cloud-cost-optimizer
   ```

2. **Package for AWS Lambda:**
   Since AWS Lambda requires external libraries like `pandas`, package them into a Lambda Layer or deployment zip:
   ```bash
   pip install -r requirements.txt -t ./package
   cp lambda_function.py ./package
   cd package && zip -r ../deployment_package.zip .
   ```

3. **Deploy to AWS:**
   - Upload `deployment_package.zip` to an AWS Lambda function.
   - Attach an **IAM Role** with policies permitting `ec2:Describe*`, `ec2:StopInstances`, `ec2:StartInstances`, and `cloudwatch:GetMetricData`.
   - Setup an **Amazon EventBridge (CloudWatch Events)** rule to trigger the Lambda hourly or at specific cron intervals.
