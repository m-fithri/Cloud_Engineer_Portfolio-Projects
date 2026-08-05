# 📌 Overview

The third part of the project focuses on creating Kubernetes manifest files to define how a containerized application should be deployed and exposed.

The implementation includes creating a Deployment manifest for application deployment and a Service manifest for exposing the backend to users.

# 🎯 Objective

- Set up a Deployment manifest that tells Kubernetes how to deploy your backend.
- Set up a Service manifest that tells Kubernetes how to expose your backend to your users.

# ✏️ What I learned

## 🔍 Additional Notes

**1) Kubernetes Manifest Files** 
- The configuration files that define the desired state of resources in a Kubernetes cluster.
- Written in YAML or JSON as they tell Kubernetes what resources to create and how those resources should behave.

**2) Deployment Manifest**
- Defines how Kubernetes should deploy and manage an application.
- It specifies:
  - The container image to run
  - The number of Pod replicas
  - Labels used to identify Pods
  - Update strategy for rolling updates

**3) Service Manifest**
- Defines how applications can communicate with a set of Pods.
- It specifies:
  - Which Pods to target using labels (selectors)
  - The type of Service (such as ClusterIP, NodePort, or LoadBalancer)
  - The ports used for communication

**4) Difference Between Deployment and Service Manifest**

| Deployment Manifest | Service Manifest |
|---|---|
| Manages the deployment and lifecycle of application Pods | Provides network access to a group of Pods |
| Creates, updates, scales, and replaces Pods automatically | Routes traffic to the appropriate Pods |
| Defines the desired number of Pod replicas | Defines how users or other applications communicate with the Pods |
| Focuses on running the application | Focuses on making the application accessible |
