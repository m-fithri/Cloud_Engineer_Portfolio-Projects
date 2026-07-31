# 📌 Overview

The second part of this project focuses on building an API using AWS Lambda and Amazon API Gateway. This phase demonstrates how APIs enable communication between the frontend and backend while establishing the Application Tier of the 3-tier web application architecture. 

AWS Lambda serves as the application's compute layer, executing business logic, processing requests, retrieving data from the database, and returning the appropriate response to the user through the API.

# 🎯 Objective

- Develop a serverless Lambda function.
- Configure an API with API Gateway.
- Connect Lambda with API Gateway.
- Write JSON documentation for your API.

# ✏️ What I learned

## 🔑 Key Concepts

**1) AWS Lambda** 
- AWS Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It is an example of Function as a Service (FaaS).
- The website consists of three static files—index.html, style.css, and script.js—which are stored in the S3 bucket and served as the content distributed through Amazon CloudFront.

**2) Amazon API Gateway** 
- A fully managed service for creating, publishing, securing, monitoring, and managing APIs at any scale
- It manages incoming traffic, directing them to the correct services, and makes sure only authorized requests get through

## 🔍 Additional Notes

**3) Lambda Function**
- A self-contained block of code that performs a specific task when triggered by an event

**4) Runtime**
- Execution environment that provides the programming language and libraries required for a Lambda function to run

**5) Node.js**
- An open-source, cross-platform JavaScript runtime that enables JavaScript code to run outside of a web browser

**6) Architecture**
- Processor type used to execute the Lambda function

**7) What the code (lambdacodesource.txt) does?**
- The code sets up a Lambda function that retrieves data from a DynamoDB table
- It looks for specific user data based on a 'userId' (thru form/field submitted in the website) and returns that data that matches the 'userId'
- If there's an error, it returns an error message

**8) Application Programming Interface (API)**
- A set of rules that allows different software applications to communicate and share data with each other

**9) Relationship Between API Gateway and AWS Lambda**
- API act as front door to the lambda function (receive request & forward then to lambda functions)
- Lambda process the request & send the response thru API gateway back to user

**10) Representational State Transfer (REST) API**
- Architectural style for designing web services that communicate using standard HTTP methods

**11) Resource Path**
- A resource path is the URL endpoint that identifies a specific resource within an API

**12) Resource Name**
- Logical name assigned to a resource within API Gateway (to manage & reference it easily in the console)

**13) API Method**
- Type of operation that clients can perform on a resource
- example:
  - GET – Retrieve data
  - POST – Create new data.
  - PUT – Update existing data.
  - DELETE – Remove data.

**14) Lambda Proxy Integration**
- Setting that simplifies the connection between API Gateway and Lambda
- When user interact with website, request goes to API gateway (contains headers, query parameter, path parameter & body)
- API gateway then break down the request & reformat it in a way lambda function can process it 
- Once lambda return the response, API gateway need to map the response back into a format expected by the client
- With lambda proxy integration, API gateway does not need to reformat the user request (all entire request are send directly to lambda)

**15) What the Configured API Method Does**
- When a user sends a GET request, API Gateway invokes the Lambda function, which retrieves the requested data from DynamoDB and returns it to the client

**16) Lambda stage**
- Snapshot of your API at a specific point in time (version control)

**17) Invoke URL**
- Public endpoint used to access a deployed API
- Applications, websites, scripts, or other services send HTTP requests to this URL to invoke the API and receive response

**18) API Documentation**
- Document that explains how developers can interact with an API

**19) API Specification Types**
- Swagger (OpenAPI 2.0): An earlier specification for describing REST APIs
- OpenAPI 3.x : The current industry-standard specification for documenting REST APIs and the successor to Swagger
- Are usually export with extensions so that the additional API settings specific to the API gateway is visible

