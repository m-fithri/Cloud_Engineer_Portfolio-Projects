# 📜 Instructions

## Task 1: S3 Set up and Upload Files to the bucket
1. Log in to the **AWS console** as IAM admin user.
2. Enter `S3` in the console search bar and open it.
3. Select **create bucket** and enter a unique bucket name.
4. Leave all other settings as default and select **create bucket**.
5. Download and save the following website files:
   - `index.html`
   - `style.css`
   - `script.js`

6. Verify the files by opening it from a browser or downloaded software in your computer.
7. Once verified, select your created S3 bucket and click **Upload**.
8. Select **Add files** and select those three website files from your computer. Select **Upload**.

## Task 2: Set up CloudFront distribution
9. Enter `CloudFront` in the **AWS Console** search bar and open it.
10. In **CloudFront** console, select **Create a CloudFront distribution**.
11. In the Distribution options panel, enter a name to match the created S3 bucket in the **Distribution name**.
12. For **Distribution type**, select the **Single website or app** option.
13. Select **Next**.
14. In the **Origin** panel, select the **Browse S3** button.
15. Select the created bucket name and click **Choose**.
16. Keep the default in the Settings panel and select **Next** at the bottom.
17. For **Web Application Firewall (WAF)**, select **Do not enable security protections**.
18. Review the configuration. Select **Create distribution** if everything looks good.

## Task 3: Verify and Update CloudFront distribution
19. After distribution creation is completed, verify whether it is working by copying the distribution domain name and open it from another browser page.
20. Getting the **Site can't be reached** error.
21. Head back to CloudFront console.
22. In **General** menu bar, select **Edit**.
23. Look for **Default root object - optional** and enter `index.html`.
24. Click **Save Changes**.
25. Refresh the distribution domain name tab page again and it should be accessible now.

## Task 4: Enable S3 Static Website Hosting **[Optional]**
26. From S3 console, select the created bucket name and choose **Properties**.
27. Scroll below to the **static website hosting** and click **Edit**.
28. Select **Enable** for static website hosting.
29. Enter `index.html` for index document and select **Save Changes**
30. Click on the bucket website endpoint redirect link to open it
    > the link should be visible in this type of format: http://my-three-tier-bucket-789.s3-website-ap-southeast-1.amazonaws.com/

31. Getting the **403 access forbidden** error because S3 static website hosting are enabled without making the objects publicly available.

## Task 5: Troubleshoot S3 Static Website Hosting Error **[Optional]**
32. From bucket **permission** settings, look for **block public access** under bucket settings and click **Edit**.
33. Unselect the **block all public access"' options and click **Save Changes**
34. Validate whether the steps are working by refreshing the error page but it will still be inaccessible since S3 bucket files are still configured as private.
35. Edit the S3 bucket policy by including the command below: 
    > include `,` for multiple statement
    
	> replace `<S3 bucket ARN name>` with the actual bucket ARN name

    ```
    {
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "<S3 bucket ARN name>/*"
	}
    ```

36. Click **Save Changes**.
37. Refresh the error page and it should be accessible again now.

## Task 6: Delete Resources **[Optional]**

Delete `CloudFront distribution` resources.

38. In CloudFront console, select the created distribution.
39. Select **Disable**.
40. Wait for the distribution status to change to **Disabled**.
41. Select **Delete**.

Delete `S3 bucket` resources.

42. In the S3 console, select the created bucket.
43. Select **Empty**. Confirm the deletion.
44. Select **Delete**. Confirm the deletion again.
