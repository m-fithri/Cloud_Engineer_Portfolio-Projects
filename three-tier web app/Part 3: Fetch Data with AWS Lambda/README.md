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

**Amazon DynamoDB** 
- A fully managed, serverless NoSQL database service that delivers high performance and low latency at any scale.
- It provides a fast and flexible way to store and retrieve application data without managing database servers.
- DynamoDB uses a flexible schema, allowing items within the same table to contain different attributes, making it ideal for applications with evolving data requirements.

## 🔍 Additional Notes

**Partition Key**
- A primary attribute that DynamoDB uses to determine the partition where an item is stored.
- Every item in a table must have a partition key value, and each value must be unique if the table uses only a partition key as its primary key.

**What the code (lambdacodesource1.txt) does**
- The first section of the code uses the AWS SDK for JavaScript to communicate with Amazon DynamoDB.
- It accepts a `userId` provided by the client, queries the `UserData` table for the matching record, and returns the retrieved data as the API response.
- The second section implements error handling to catch exceptions, such as invalid requests or database access failures, and returns an appropriate error message.

**AWS SDK**
- A collection of libraries and tools that enable developers to interact with AWS services programmatically.

**Why Use an Inline IAM Policy Instead of the Managed Policy (AmazonDynamoDBReadOnlyAccess)?**
- An inline IAM policy provides fine-grained permissions tailored to a specific Lambda function.
- In this project, the Lambda function only needs read access to the UserData table, so an inline policy grants permission exclusively to that resource (Principle of Least Privilege).

# 📜 Instructions

## Task 1: Set up DynamoDB
1. Log in to the **AWS console** as IAM admin user.
2. Search for `DynamoDB` in the AWS console and open it.
3. Select **Create table** and enter `UserData` for Table name.
4. Enter `userId` for Partition key and select `string` as the data type.
5. Leave the default settings for the rest of the options and select **Create table**.

## Task 2: Add a Table Item
6. Once the table status changes to **Active**, select the `UserData` table.
7. Select **Explore table items**.
8. At the **Items returned** panel, select **Create item**.
9. Select **Switch to JSON view** and toggle off **View DynamoDB JSON**.
10. Copy and paste below JSON code into the editor:
    ```
    {
    "userId": "1",
    "name": "Test User",
    "email": "test@example.com"
    }
    ```

11. Select **Create item**.
12. Verify that the item was created successfully. You should see it listed in the **Items returned** tab.

## Task 3: Create the Lambda Function
13. Search for `Lambda` in the AWS console and open it.
14. Select **Create function** and select **Author from scratch**.
15. Enter `RetrieveUserData` for Function name.
16. For Runtime, choose a **Node.js** runtime and select **Create function**.

## Task 4: Implement the Lambda Function Logic
17. Select the created function and navigate to **code source** under **code** section.
18. Copy and replace the code shown in the editor with the code in `lambdacodesource1.txt` (replace `enter your region` with the actual region):
19. Click **Deploy**.

## Task 5: Write a Lambda Function Test
20. Still in your Lambda function, select the **Test** tab.
21. Leave the default settings for the rest of the options and navigate to **Event JSON** panel.
22. Enter below code and click **Test**.
    ```
    {
    "userId": "1"
    }
    ```

23. Getting successful test but receive the "AccessDeniedException" error because we haven't given it explicit permission to access DynamoDB table.
24. In this context, getting a success only means that the function itself could run but error persist because DynamoDB is blocking the lambda function from reading the table.

## Task 6: Grant DynamoDB Access to Lambda
25. Switch to the **Configuration** tab in your Lambda function and select **Permissions**.
26. Select the **execution role name**
    > it will look something like RetrieveUserData-role-xxxxxxxx

27. This shortcut will take you to the IAM console, with your Lambda function readily open.
28. Navigate to **Permission policies** and click **Add permissions**.
29. Select **Attach policies** and type `DynamoDB` in the search bar.
30. In order to determine which specific policies need to be selected, check the error earlier & you will notice the `DynamoDB:GetItem` in the error message.
31. Head back to the policy set up page and expand the `AmazonDynamoDBReadOnlyAccess` policy.
32. Notice the `GetItem` policy shown in line 25 so select this `AmazonDynamoDBReadOnlyAccess` policy option and select **Add permissions**. 

## Task 7: Retest your Lambda Function
33. Head back to the **Test** tab in your Lambda function.
34. Select **Test**.
35. You should now see a successful test execution without the `AccessDeniedException` error.

## Task 8: Tighten DynamoDB Security [Optional]
36. Switch to the **Configuration** tab in your Lambda function and select **Permissions**.
37. Select the **execution role name**.
38. This shortcut will take you to the IAM console, with your Lambda function readily open.
39. Navigate to **Permission policies** and select the `AmazonDynamoDBReadOnlyAccess` policy earlier to remove it.
40. Click **Add permissions** and select **Create Inline Policies**.
41. Stick to the **visual editor** selection, expand the **Select a Service** dropdown and enter `DynamoDB` then click on it.
42. Under **Actions Allowed** section, enter `GetItem` & select it.
43. Under **Resources**, select **specific** and click **Add ARNs**.
44. In the **Specify ARNs** tab, fill in your own region in the `resource region` field.
45. For Resource Table Name, fill in your DynamoDB table name & click **Add ARNs**.
46. Click **Next** and fill in the **policy name**.
47. Click **Create policy**.
48. Head back to the **Test** tab in the lambda function.
49. Select **Test** it should be successful since it returns the queried data.

## Task 9: Delete Resources [Optional]

Delete `Lambda function`.

50. Navigate to the Lambda service in the AWS Management Console.
51. Select the created function.
52. Select **Actions** and select **Delete**.
53. Confirm the deletion.

Delete `DynamoDB` table.

54. Head to the `DynamoDB` service.
55. From the left hand navigation bar, select **Tables**.
56. Select the `UserData` table.
57. Select **Delete**.
