# Build A Security Monitoring System

## 📌 Overview

This project demonstrates how to build a monitoring and alerting solution in AWS using AWS CloudTrail, Amazon CloudWatch, and Amazon Simple Notification Service (SNS).

The goal is to understand how AWS security and monitoring services work together to detect events, analyze activity, and automatically notify administrators when specific actions occur.

The solution consists of the following components:

- **AWS CloudTrail** records API activity and management events, then stores the logs in an Amazon S3 bucket for auditing and analysis.
- **Amazon CloudWatch** monitors CloudTrail events, evaluates them against configured rules, and triggers alerts when predefined conditions are met.
- **Amazon Simple Notification Service (SNS)** delivers alert notifications to subscribed users through supported communication channels, such as email.

---

The project is divided into two stages:

Stage 1: Configure Secret & Logging
- **Task 1** - Create the secret that will be monitored
- **Task 2** - Configure AWS CloudTrail to capture API activity
- **Task 3** - Testing the CloudTrail set up

Stage 2: Configure Monitoring and Alerts
- **Task 4** - Create CloudWatch rules to monitor CloudTrail events
- **Task 5** - Configure CloudWatch Alarm and Amazon SNS to receive alert events
- **Task 6** - Verify the end-to-end workflow by generating an event and confirming that a notification is successfully delivered

## 🛠️ Technologies & Tools

`AWS Secrets Manager` `AWS CloudTrail` `Amazon CloudWatch` `Amazon SNS` `Amazon S3` `AWS CLI`

## 🏗️ Architecture

```

                                        CloudWatch
[Secrets Manager] ⟸ [CloudTrail] ⟹ [Log group + Filter + Alarm] ⟹ [Amazon SNS] ⟹ Email

                          │ 
                          ▼

                      [S3 Bucket]

```

## ✏️ What I learned

### 🔑 Key Concepts

**1) AWS Secret Manager**
- A fully managed service that securely stores, retrieves, and manages sensitive information such as database credentials, API keys, tokens, and passwords.

**2) AWS CloudTrail**
- A governance, compliance, and auditing service that records API activity and management events across your AWS account.

**3) AWS CloudWatch**
- A monitoring service that collects metrics, logs, and events from AWS resources and applications.

**4) Amazon SNS**
- A fully managed messaging service that sends notifications to subscribers when an event occurs.

**5) Amazon S3**
- A highly durable, scalable object storage service used to store and retrieve data.

**6) AWS CLI**
- A tool that allows you to manage AWS services using terminal commands instead of the AWS Management Console.

### 🔍 Additional Notes

**7) Encryption**
- Process of scrambling readable data into an unreadable code ensuring only someone with the right key can unscramble & read it.

**8) Resource Permissions**
- Determine which IAM users, roles, or AWS services are allowed to access a specific AWS resource.
- For Secrets Manager, these permissions control who can read, modify, or delete a secret.

**9) Secret Replication**
- Secret replication copies a secret to one or more AWS Regions.
- This improves availability and reduces cross-region requests by allowing applications to retrieve secrets from a region closer to where they are running.

**10) Configure Rotation**
- Secret rotation automatically updates a secret at scheduled intervals without requiring manual intervention (reducing the risk of credential compromise).

**11) Trail**
- A CloudTrail configuration that specifies which events should be recorded and where the resulting log files should be delivered.

**12) Why Use Amazon S3 for CloudTrail Logs?**
- Amazon S3 provides highly durable, scalable, and cost-effective storage for audit logs.
- It allows CloudTrail logs to be retained for long-term analysis while charging only for the storage consumed.

**13) Why Exclude AWS KMS and Amazon RDS Data API Events?**
- It can generate a large volume of routine management events.
- Excluding these events reduces unnecessary log noise, making it easier to identify activities related to Secrets Manager while also reducing storage and monitoring costs.

**14) What Does "Retrieve Secret Value" Do?**
- It fetches the decrypted contents of a secret using an API call, CLI command, or the console.

**15) AWS CloudShell**
- A browser-based terminal that enables you to run AWS CLI commands without installing or configuring software on your local machine.

**16) Log Group**
- A collection of logs from a specific application or service.

**17) Why Create an IAM Role for CloudWatch Logs?**
- Instead of granting CloudTrail broad permissions, an IAM role allows CloudTrail to write logs only to the designated CloudWatch Log Group (Principle of Least Privilege)

**18) CloudTrail Event History vs. CloudWatch Logs**

| CloudTrail Event History | CloudWatch Logs |
|---|---|
| Provides a recent history of management events for your AWS account | Stores logs for customizable retention periods, including indefinite retention if required |
| Retains events for up to 90 days at no additional cost | Supports searching, filtering, metric extraction, alarms, dashboards, and automated responses |
| Best suited for auditing and investigating AWS API activity | Best suited for real-time monitoring, operational visibility, and alerting |

**19) CloudWatch Metric Filters**
- Scan incoming log data for specific terms, phrases, or patterns, translating text logs into numerical metrics.

**20) Metric Namespace**
- Help you organize your metrics and prevent naming conflicts with metrics from other AWS services (like a folder).

**21) Metric Value and Default Value**

| Metric Value | Default Value |
|---|---|
| What gets recorded when our filter spots a match in the logs | What gets recorded when our filter doesn't find any matches during a given time period |

**22) Statistic and Period**

| Statistic | Period |
|---|---|
| Tells CloudWatch how to analyze the CloudWatch metric | How often CloudWatch checks in on your metric |

**23) Alarm Threshold**
- Metric value that must be reached before a CloudWatch alarm changes state.
