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

