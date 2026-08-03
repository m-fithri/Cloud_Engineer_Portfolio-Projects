# Create S3 Buckets with Terraform

## 📌 Overview

In modern cloud environments, automation plays a vital role in how you develop and deploy code. 

Automation can helps improved the software development process by eliminating repetitive manual task, reduce the risk of human error and ensure resources are deployed consistently across different environments. 

This project demonstrates how to use Terraform to provision an Amazon S3 bucket using Infrastructure as Code (IaC).

By completing this project, we will learn how to install and configure Terraform, initialize a Terraform project, troubleshoot common issues, and successfully apply a Terraform configuration to create and manage an S3 bucket on AWS.

---

The goals of this project are to:
- Install and configure Terraform for Infrastructure as Code (IaC).
- Configure AWS credentials to enable Terraform to authenticate with your AWS account.
- Provision and manage Amazon S3 buckets using Terraform.
- Upload and manage files in an Amazon S3 bucket using Terraform.

## 🛠️ Technologies & Tools

`Terraform` `Amazon S3` `AWS CLI` `AWS IAM`

## 🏗️ Architecture

```

      Setup                                                                                            Troubleshooting
    ───────────────────────────────────                                                              ─────────────────────────────────
   │                                   │                                                            │                                 │
   │       [Install Terraform]         │                                                            │                                 │
   │                                   │                                                            │        [Install AWS CLI]        │
   │                │                  │                                                            │                                 │
   │                ▼                  │                                                            │                │                │
   │                                   │                          Plan                              │                ▼                │
   │    [Set up a Terraform project]   │   ══════════════ ➤    Terraform     ══════════════ ➤     │                                 │
   │                                   │                      Configuration                         │     [Set up AWS Access Keys]    │
   │                │                  │                                                            │                                 │
   │                ▼                  │                                                            │                                 │
   │                                   │                                                             ─────────────────────────────────
   │         [Create main.tf]          │                                                                              │
   │                                   │                                                                              │
    ───────────────────────────────────                                                                               │
                                               Output                                                                 │
                                 ─────────────────────────────                               Apply                    │
                                |                             │     ◀ ══════════════       Terraform       ◀ ═════════
                                │    [Launch an S3 bucket]    │                           Configuration
                                │                             │ 
                                 ─────────────────────────────                                   

```

## ✏️ What I learned

### 🔑 Key Concepts

**1) Terraform**
- A tool that helps you build and manage your cloud infrastructure using code.

**2) Amazon S3**
- Act as a storage space in the cloud where you can store your files.

**3) AWS CLI**
- Unified tool that allows you to manage and control Amazon Web Services directly from your local terminal.

**4) AWS IAM**
- Service that helps you securely control access to AWS resources.

### 🔍 Additional Notes

**5) Infrastructure as Code (IaC)**
- Ability to provision and support your computing infrastructure using code instead of manual processes and settings.

**6) main.tf**
- A central file in a Terraform project.

**7) What do the three blocks of code in the main.tf file describe?**
- first block indicates we are using AWS as the provider of this infrastructure
- second block provisions a S3 bucket & gives it a unique name
- third block manages the bucket permissions which control its access

**8) Terraform Registry**
- A central hub to find, share, and download infrastructure code, specifically offering providers, modules, and policy libraries

**9) What Terraform init do?**
- Prepare your local environment before you can run execution commands

