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

**AWS Lambda** 
- AWS Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It is an example of Function as a Service (FaaS).
- The website consists of three static files—index.html, style.css, and script.js—which are stored in the S3 bucket and served as the content distributed through Amazon CloudFront.

**Amazon API Gateway** 
- A fully managed service for creating, publishing, securing, monitoring, and managing APIs at any scale
- It manages incoming traffic, directing them to the correct services, and makes sure only authorized requests get through

## 🔍 Additional Notes

**Lambda Function**
- A self-contained block of code that performs a specific task when triggered by an event

**Runtime**
- Execution environment that provides the programming language and libraries required for a Lambda function to run

**Node.js**
- An open-source, cross-platform JavaScript runtime that enables JavaScript code to run outside of a web browser

**Architecture**
- Processor type used to execute the Lambda function

**What the code (lambdacodesource.txt) does?**
- The code sets up a Lambda function that retrieves data from a DynamoDB table
- It looks for specific user data based on a 'userId' (thru form/field submitted in the website) and returns that data that matches the 'userId'
- If there's an error, it returns an error message

**Application Programming Interface (API)**
- A set of rules that allows different software applications to communicate and share data with each other

**Relationship Between API Gateway and AWS Lambda**
- API act as front door to the lambda function (receive request & forward then to lambda functions)
- Lambda process the request & send the response thru API gateway back to user

**Representational State Transfer (REST) API**
- Architectural style for designing web services that communicate using standard HTTP methods

**Resource Path**
- A resource path is the URL endpoint that identifies a specific resource within an API

**Resource Name**
- Logical name assigned to a resource within API Gateway (to manage & reference it easily in the console)

**API Method**
- Type of operation that clients can perform on a resource
- example:
  - GET – Retrieve data
  - POST – Create new data.
  - PUT – Update existing data.
  - DELETE – Remove data.

**Lambda Proxy Integration**
- Setting that simplifies the connection between API Gateway and Lambda
- When user interact with website, request goes to API gateway (contains headers, query parameter, path parameter & body)
- API gateway then break down the request & reformat it in a way lambda function can process it 
- Once lambda return the response, API gateway need to map the response back into a format expected by the client
- With lambda proxy integration, API gateway does not need to reformat the user request (all entire request are send directly to lambda)

**What the Configured API Method Does**
- When a user sends a GET request, API Gateway invokes the Lambda function, which retrieves the requested data from DynamoDB and returns it to the client

**Lambda stage**
- Snapshot of your API at a specific point in time (version control)

**Invoke URL**
- Public endpoint used to access a deployed API
- Applications, websites, scripts, or other services send HTTP requests to this URL to invoke the API and receive response

**API Documentation**
- Document that explains how developers can interact with an API

**API Specification Types**
- Swagger (OpenAPI 2.0): An earlier specification for describing REST APIs
- OpenAPI 3.x : The current industry-standard specification for documenting REST APIs and the successor to Swagger
- Are usually export with extensions so that the additional API settings specific to the API gateway is visible

# 📜 Instructions

## Task 1: Create a Lambda Function
1. Log in to the **AWS console** as IAM admin user.
2. Enter `Lambda` in the console search bar and open it.
3. Select **Create a Function** and select **Author from Scratch**.
4. For function name, enter `RetrieveUserData` and select **Node.js** for runtime.
5. Select **Create function**.
6. Scroll down to the **Code source** panel & paste the code shown in `lambdacodesource.txt`.
7. Replace `enter your region` with your AWS region and click **Deploy**.

## Task 2: Set Up an API Gateway & API resource 
8. Search for `API Gateway` in the AWS console and open it.
9. Select **Create APi**, select **REST API** and click **Build**.
10. Under API details, select **New API** and enter `UserRequestAPI` as API name.
11. For AP endpoint type, select **Regional** and click **Create API**.
12. From the created API settings, navigate to **Resource** and select **Create Resource**.
13. Enter `users` as resource name and click **Create resource**.
14. Once resource creation completed, select the **/user** resource.

## Task 3: Set up an API method
15. In the **Methods** panel, select **Create method**.
16. Select `GET` from the **Method type** dropdown.
17. Select **Lambda Function** for the Integration type.
18. Switch on **Lambda proxy integration**.
19. For the **Lambda function**, make sure the default region selected is where you've created your function.
20. Select the created **RetrieveUserData** function.
21. Select **Create method**.

## Task 4: Deploy your API
22. Select **Deploy API**.
23. For Stage, select **New stage**.
24. For Stage name, enter `prod` and select **Deploy**.
25. On the same page, find the prod stage's **Invoke URL**.
26. Copy and access the URL in a new tab on the browser.
27. Getting a **Missing Authentication Token** error because DynamoDB table is not set up yet (Lambda function need to be connected to DynamoDB to retrieve data).

## Task 5: Write Documentation for your API in JSON [Optional]
28. In the API gateway under the selected API, navigate to **Documentation** on the left side of the panel.
29. Select **Create Documentation Part** and select **API** for documentation type.
30. Enter below line of code with below configuration:
    > replace `<invoke URL>` with the created invoke URL
    
    ```
    {
    "description": "The UserRequestAPI manages user data requests. It supports operations to get user details based on unique identifiers (i.e. userId).",
    "baseURL": "<invoke URL>"
    }
    ```

31. Click **Create documentation part** and click **Publish documentation**.
32. Select **Stage**, fill in **version** and click **Publish**.
33. From the green notification, select **Download documentation**.
34. Select **API specification type**, **format** and **extension** (export with API Gateway extensions).
35. Click **Export API**.
    
## Task 6: Delete Resources [Optional]

Delete `API` in API Gateway.

36. Navigate to the API Gateway service in the AWS Console.
37. Select the created API.
38. Select **Actions** and select **Delete API**.
39. Confirm the deletion.

Delete `Lambda function`.

40. Navigate to the Lambda service in the AWS Management Console.
41. Select the created function.
42. Select **Actions** and select **Delete**.
43. Confirm the deletion.
