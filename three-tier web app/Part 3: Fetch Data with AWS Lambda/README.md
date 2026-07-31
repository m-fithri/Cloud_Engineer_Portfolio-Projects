# 📌 Overview

The third part of this project focuses on storing and managing application data using Amazon DynamoDB. This phase demonstrates how the Data Tier of the 3-tier web application architecture stores and retrieves information efficiently. 

You will also learn how AWS Lambda interacts with DynamoDB to query application data and return the requested information to users through the API.

# 🎯 Objective

- Create a database table to store user data.
- Create a serverless function to retrieve user data.
- Write tests to validate if your function can fetch data from DynamoDB.
- Secure your serverless function with proper permissions.
- Secure your database with an inline policy

# ✏️ What I learned

## 🔑 Key Concepts

**1) Amazon DynamoDB** 
- A fully managed, serverless NoSQL database service that delivers high performance and low latency at any scale.
- It provides a fast and flexible way to store and retrieve application data without managing database servers.
- DynamoDB uses a flexible schema, allowing items within the same table to contain different attributes, making it ideal for applications with evolving data requirements.

## 🔍 Additional Notes

**2) Partition Key**
- A primary attribute that DynamoDB uses to determine the partition where an item is stored.
- Every item in a table must have a partition key value, and each value must be unique if the table uses only a partition key as its primary key.

**3) What the code (lambdacodesource1.txt) does**
- The first section of the code uses the AWS SDK for JavaScript to communicate with Amazon DynamoDB.
- It accepts a `userId` provided by the client, queries the `UserData` table for the matching record, and returns the retrieved data as the API response.
- The second section implements error handling to catch exceptions, such as invalid requests or database access failures, and returns an appropriate error message.

**4) AWS SDK**
- A collection of libraries and tools that enable developers to interact with AWS services programmatically.

**5) Why Use an Inline IAM Policy Instead of the Managed Policy (AmazonDynamoDBReadOnlyAccess)?**
- An inline IAM policy provides fine-grained permissions tailored to a specific Lambda function.
- In this project, the Lambda function only needs read access to the UserData table, so an inline policy grants permission exclusively to that resource (Principle of Least Privilege).

