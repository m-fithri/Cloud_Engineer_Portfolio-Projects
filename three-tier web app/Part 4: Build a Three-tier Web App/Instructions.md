# 📜 Instructions

## Task 1: Integrate the Tiers
1. Log in to the **AWS console** as IAM admin user.
2. Search for `API Gateway` in the AWS console and open it.
3. Copy the prod stage API's **Invoke URL**.
4. Append `/users?userId=1` to the end of the URL you've copied & run it in the web browser.
5. Find the distributed site's URL in the CloudFront console again and open it to another web browser page.
6. Try entering `1` in the `userId` field and selecting **Get User Data**.
7. Nothing happens.
8. To troubleshoot, open the browser's developer tools by pressing **F12** on the keyboard and select the **Console** tab.
9. Refresh the page, enter `1` in the `userId` field and select **Get User Data** again.
10. Noticed the referencing URL error on `https://[YOUR-PROD-API-URL]/users?userId=1` which originated from the uploaded `script.js` file earlier.
11. Open the `script.js` file directly using a code editor.
12. The line 9 is directly references `[YOUR-PROD-API-URL]` so this need to be replaced with the correct value.
13. Head to `API Gateway` console and copy the prod stage API's **Invoke URL**. 
14. Paste this in **script.js**, making sure you're replacing `[YOUR-PROD-API-URL]` in the script and save the changes.
15. Head back to the S3 console and select **Upload**.
16. Select **Add files**, select the updated `script.js` and proceed to **upload** it to the S3 bucket.

## Task 2: Validate a Fully Functioning Web App
17. Access the website through the CloudFront URL again for testing but getting error related to **CORS** because the API Gateway is not configured to allow requests from the CloudFront URL.
18. API Gateway is only allowing requests directly from its **Invoke URL** so to resolve this, CORS on the API Gateway need to be enabled so that it can accept requests from the domain where the frontend is hosted.
19. Head back to the `Amazon API Gateway` console and navigate to the **Resources** tab.
20. Select the `/users` resource and select **Enable CORS**.
21. In the CORS configuration, check both `GET` and `OPTIONS` under **Access-Control-Allow-Methods**.
22. Enter the **CloudFront distribution domain name** as the **Access-Control-Allow-Origin** value. This will allow requests from the CloudFront domain to the API.
23. Select **Save**.
24. Select **Deploy API**, choose the deployment stage and click **Deploy** to update the stage.
25. Update the Lambda function code with the code shown in `lambdasourcecode2.txt` with below configuration:
    > replace `YOUR_REGION` with the actual region name
    
    > replace `*` for the `'Access-Control-Allow-Origin value'` with the CloudFront domain name

26. Select **Deploy** to deploy your updated function.
27. Head back to CloudFront site again and refresh the page.
28. Click **Get User Data** and the data fetched from DynamoDB should be visible on the website.

## Task 3: Delete Resources

Delete `CloudFront distribution` resources.

29. In CloudFront console, select the created distribution.
30. Select **Disable**.
31. Wait for the distribution status to change to **Disabled**.
32. Select **Delete**.

Delete `S3 bucket` resources.

33. In the S3 console, select the created bucket.
34. Select **Empty**. Confirm the deletion.
35. Select **Delete**. Confirm the deletion again.

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

Delete `DynamoDB` table.

44. Head to the `DynamoDB` service.
45. From the left hand navigation bar, select **Tables**.
46. Select the `UserData` table.
47. Select **Delete**.

