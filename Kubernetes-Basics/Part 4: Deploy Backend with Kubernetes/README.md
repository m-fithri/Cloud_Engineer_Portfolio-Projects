# 📌 Overview

The final part of the project focuses on deploying a containerized backend application to an Amazon EKS cluster and monitoring its deployment.

The implementation brings together the complete Kubernetes workflow, from infrastructure provisioning to a live, running backend application.

# 🎯 Objective

- Deploy the backend on a Kubernetes cluster.
- Track your Kubernetes deployment using EKS.

# ✏️ What I learned

## 🔍 Additional Notes

**1) Pod** 
- The smallest and most basic deployable unit in Kubernetes.
- A Pod represents one or more containers that run together on the same worker node and share the same network and storage resources.
- A Pod includes:
  - One or more containers (usually a single application container)
  - A shared IP address and network namespace
  - Shared storage volumes (if configured)
