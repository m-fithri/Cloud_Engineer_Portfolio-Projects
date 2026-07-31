# Three-tier Web App

## Overview

A three tier web application is a software architecture that separates an application into three independent layers: which is **Presentation Tier**, **Application/Logic Tier** and **Database Tier**.

This separation improves scalability, security and performance by allowing each layer to operate independently.

- **Presentation Tier (Frontend)** - The user interface where users interact with the application thru a web browser. It handles user requests and display data.

- **Logic Tier (Backend)** - Processes business logic, handles client requests and communicates between the user interface and the database.

- **Database Tier** - Stores and manages application data, ensuring reliable data retrieval, updates, and security.

---

The project is structured into four parts, each covering a specific set of objectives as outlined below:

**Part 1: Website Delivery with CloudFront**
- Create a storage space in S3 for your website's files.
- Set up CloudFront to distribute your website globally.
- Manage permissions for both S3 and CloudFront.

**Part 2: APIs with lambda + API gateway**
- Develop a serverless Lambda function.
- Configure an API with API Gateway.
- Connect Lambda with API Gateway.
- Write JSON documentation for your API.

**Part 3: Fetch Data with AWS Lambda**
- Create a database table to store user data.
- Create a serverless function to retrieve user data.
- Write tests to validate if your function can fetch data from DynamoDB.
- Secure your serverless function with proper permissions.
- Secure your database with an inline policy

**Part 4: Build a Three-tier Web App**
- Connect all these services together seamlessly for your three-tier architecture.

## Technologies & Tools

`Amazon S3`  `CloudFront`  `AWS Lambda`  `Amazon API Gateway`  `Amazon DynamoDB`

## Architecture

```
Users

  │
  ▼

Presentation Tier
[script.js + index.html + style.css] → [S3 bucket] → [CloudFront distribution] → [Distributed website]

  │
  ▼

Logic Tier
[API Gateway] → [Lambda function]

  │
  ▼

Data Tier
[DynamoDB database]

```
