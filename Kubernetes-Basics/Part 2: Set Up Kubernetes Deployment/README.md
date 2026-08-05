# 📌 Overview

The second part of the project demonstrates how to package a backend application into a portable container image for Kubernetes.

The implementation includes building a Docker image from the backend application and storing it in Amazon ECR, making the application ready for deployment on Amazon EKS.

# 🎯 Objective

- Clone a backend application from GitHub.
- Build a Docker image of the backend.
- Push your image to an Amazon ECR repository.
- Troubleshoot installation and configuration errors

# ✏️ What I learned

## 🔑 Key Concepts

**1) Amazon Elastic Container Registry (ECR)** 
- A fully managed AWS service for storing, managing, and sharing container images.

**2) Git and GitHub**

| Git | GitHub |
|---|---|
| A version control tool that tracks changes to source code locally | A cloud-based platform that hosts Git repositories online |

**3) Amazon EC2**
- A scalable computing capacity in the AWS Cloud so you can develop and deploy applications without hardware constraints.

**4) Backend**
- The server-side part of an application that processes requests, performs business logic, and manages data.

**5) Cloning**
- The process of creating a complete local copy of a remote Git repository.

## 🔍 Additional Notes

**6) Why does the repository name say `flask`?**
- The backend application is built using Flask, a lightweight Python web framework
- A framework provides a foundation for building applications by offering pre-built tools and libraries, allowing developers to focus on application logic rather than common setup tasks.

**7) Container Image**
- A packaged, read-only template that contains everything needed to run an application.
- Includes:
  - Application source code
  - Runtime
  - Libraries and dependencies
  - Configuration files
  - Operating system components (when required)

**8) What does Building an Image means?**
- Process of creating a container image from a Dockerfile.
- Docker reads the Dockerfile line by line and packages the application with all required dependencies into a reusable image.

**9) Docker**
- An open-source platform for building, packaging, and running applications inside containers.

**10) Why are we using Docker and ECR?**

| Docker | ECR |
|---|---|
| Packages the application, libraries, and configuration into a container image | Stores container images securely in AWS |
| Ensures the application behaves consistently regardless of where it runs | Makes images available for deployment by services like EKS and ECS |

**11) What the output of create ECR repository means?**

| Output | Meaning |
|---|---|
| repositoryArn | ARN for your ECR repository |
| repositoryUri | Repository's address used to push and pull container images |
| repositoryName | User-defined name of the repository |
| imageTagMutability | Determines whether image tags can be changed |
| imageScanningConfiguration | Specifies whether images are automatically scanned for known software vulnerabilities when pushed to the repository |
| encryptionConfiguration | Indicates how container images are encrypted while stored in Amazon ECR |

**12) Push command**
- A Docker command that uploads a locally built container image to a container registry such as Amazon ECR.

**13) What is the advantage of using a container registry**
- Container registry like ECR is great for Kubernetes deployment because we get to store tagged images from a single source.
- When any other user pull the container image, they can do it without any manual downloading required.
