# 📌 Overview

The first part of this project focuses on using Amazon CloudFront to deliver a website globally. The primary goals is to demonstrate how a Content Delivery Network (CDN) enhances website performance by reducing latency and providing a better user experience. 

This phase also sets up the Presentation Tier of the three-tier web application architecture by securely distributing static web content through Amazon CloudFront.

# 🎯 Objective

- Create a storage space in S3 for your website's files.
- Set up CloudFront to distribute your website globally.
- Manage permissions for both S3 and CloudFront.

# ✏️ What I learned

## 🔑 Key Concepts

**Amazon S3** 
- Serves as cloud-based object storage for hosting and storing the static website files
- The website consists of three static files—index.html, style.css, and script.js—which are stored in the S3 bucket and served as the content distributed through Amazon CloudFront

**Amazon CloudFront**
- A Content Delivery Network (CDN) service that securely delivers content stored in an origin, such as an Amazon S3 bucket, to users around the world
- It improves the performance of both static and dynamic web content by caching frequently accessed files at edge locations, reducing latency and load times
- User requests are automatically routed to the nearest edge location, ensuring faster content delivery and a better user experience
- A **CloudFront distribution** is a configuration that defines how CloudFront retrieves, caches, secures, and delivers content from the origin to end users

## 🔍 Additional Notes

**index.html**
- The main HTML file that defines the structure and content of a web page
- It contains elements such as headings, paragraphs, images, buttons, and hyperlinks, which are rendered by a web browser

**style.css**
- A Cascading Style Sheets (CSS) file that controls the visual appearance of a website
- It defines the layout, colors, fonts, spacing, and overall design to create a consistent user interface

**script.js**
- A plain text file containing JavaScript code that adds functionality and interactivity to a website
- It handles user interactions, dynamic content updates, form validation, animations, and other client-side behaviors

**Static Website vs. Web Application**
- static website: does not require server-side processing or a database, with most logic executed in the user's browser
- web application: includes both frontend and backend components which handle business logic and user requests

**Caching**
- Process of storing copies of frequently requested content in a temporary storage location called a cache

**Cache Key**
- A unique identifier that CloudFront uses to determine whether a cached object matches an incoming request

**Origin Access Control (OAC)**
- A CloudFront security feature that restricts direct public access to an origin, such as an Amazon S3 bucket
- It allows only Amazon CloudFront to retrieve content from the origin using secure authentication, providing fine-grained access control and enhanced security

**Origin Request**
- A request that CloudFront sends to the origin server when the requested content is not available in the cache or when the cached version has expired
 
**Public Origin Access**
- A configuration where users can access content directly from the origin (such as an Amazon S3 bucket) without going through CloudFront
- This approach reduces security because it bypasses CloudFront's caching, security features, and access controls

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
