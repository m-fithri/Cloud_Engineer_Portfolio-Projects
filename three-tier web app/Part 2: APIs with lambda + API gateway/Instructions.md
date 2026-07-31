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
