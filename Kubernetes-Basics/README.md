# Kubernetes Basics

## 📌 Overview

Kubernetes has become the industry standard for deploying, scaling, and managing containerized applications in modern cloud environments.

This project demonstrates how to build and deploy a containerized application on Kubernetes using Amazon EKS and AWS services, providing hands-on experience with container orchestration and cloud-native deployment.

By the end of the project, a scalable Kubernetes environment is established with hands-on experience in cluster management, container deployment, and workload orchestration.

---

The project is structured into four parts, each covering a specific set of objectives as outlined below:

**Part 1: Launch a Kubernetes Cluster**
- Launch and connect to an EC2 instance.
- Create your very own Kubernetes cluster.
- Monitor cluster creation with CloudFormation.
- Access your cluster using an IAM access entry.
- Test the resilience of your Kubernetes cluster.

**Part 2: Set Up Kubernetes Deployment**
- Clone a backend application from GitHub.
- Build a Docker image of the backend.
- Push your image to an Amazon ECR repository.
- Troubleshoot installation and configuration errors

**Part 3: Create Kubernetes Manifests**
- Set up a Deployment manifest that tells Kubernetes how to deploy your backend.
- Set up a Service manifest that tells Kubernetes how to expose your backend to your users.

**Part 4: Deploy Backend with Kubernetes**
- Set up the backend of an app for deployment.
- Install kubectl.
- Deploy the backend on a Kubernetes cluster.
- Track your Kubernetes deployment using EKS.

## 🛠️ Technologies & Tools

`Amazon EKS`  `Amazon ECR`  `Amazon EC2`  `AWS CloudFormation`  `AWS IAM` `Kubernetes` `Git & GitHub`

 ## 🏗️ Architecture

```
Part 1: Create a Kubernetes cluster

                                          ══════════════ ➤  [eksctl]      ════ ➤      [CloudFormation]    ════════════════ 
                                          |                                                                                 |
                                          |                                                                                 |
Part 2: Push a Docker                     |                                                                                 |
image of your app backend                 |                                                                                 |
                                          |                                                                                 |
                                          |                                                                                 ▼
                                                              
      [GitHub]   ◀ ════════   [EC2 instance]  ══════ ➤    [Docker Container   ══════ ➤  [ECR (Elastic    ◀ ════════    [EKS (Elastic 
                                                                  Image]               Compute Registry]             Kubernetes Service]
                                          |                                                                                 ▲   |
                                          |                                                                                 |   |
Part 3: Deploy your app backend           |                                                                                 |   |
                                          |                                                                                 |   |
                                          |                                                                                 |   |
                                          ══════════════ ➤   [Manifest files]   ════════ ➤     [kubectl]      ═════════════    ══════════ ➤    [Deployed backend]

```


