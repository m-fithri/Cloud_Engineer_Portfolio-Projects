# 📌 Overview

The first part of the Kubernetes project focuses on deploying a Kubernetes cluster on AWS using Amazon EKS.

The implementation includes EC2 instance provisioning, EKS cluster creation, infrastructure monitoring and IAM-based cluster access.

# 🎯 Objective

- Launch and connect to an EC2 instance.
- Create your very own Kubernetes cluster.
- Monitor cluster creation with CloudFormation.
- Access your cluster using an IAM access entry.
- Test the resilience of your Kubernetes cluster.

# ✏️ What I learned

## 🔑 Key Concepts

**1) Amazon Elastic Kubernetes Service (EKS)** 
- A fully managed AWS service for running Kubernetes without managing the Kubernetes control plane.

**2) Amazon EC2**
- A scalable computing capacity in the AWS Cloud so you can develop and deploy applications without hardware constraints

**3) AWS CloudFormation**
- An Infrastructure as Code (IaC) service that enables AWS resources to be defined, provisioned, and managed using code templates.

**4) AWS IAM**
- A web service that helps you securely control access to AWS resources.

**5) Kubernetes**
- An open-source container orchestration platform that automates the deployment and provisioning of containerized applications.

## 🔍 Additional Notes

**6) Amazon Machine Image (AMI)**
- A pre-configured template used to launch EC2 instances.

**7) Key Pair**
- A set of security credentials used to securely access an EC2 instance.

**8) EC2 Instance Connect**
- A feature that lets you securely connect to an EC2 instance directly from the AWS Management Console or AWS CLI.

**9) Why use EC2 Instance Connect?**
- It simplifies the connection process by avoiding many traditional SSH setup steps, such as:
  - Generating and managing SSH key pairs.
  - Storing private keys on your local machine.
  - Configuring an SSH client.
  - Manually running SSH commands with a private key.

**10) eksctl**
- A command-line tool for creating and managing Amazon EKS clusters.

**11) Difference of a cluster and a node group?**
| Cluster | Node Group |
|---|---|
| The entire environment that Kubernetes manages for your containerized app | A collection of worker nodes (EC2 instances) that run your containerized applications |

**12) How Kubernetes and EC2 instance related?**
- Kubernetes manages your containerized applications.
- The worker nodes that run those containers are EC2 instances.
- Kubernetes schedules Pods onto these EC2 instances based on available resources.

**13) Desired size, minimum size and maximum size**
| Desired size | Minimum size | Maximum size |
|---|---|---|
| number of nodes you want running in your node group | minimum number of nodes your group need to have at all times | maximum size: maximum number of nodes that you will allow inside this group |
