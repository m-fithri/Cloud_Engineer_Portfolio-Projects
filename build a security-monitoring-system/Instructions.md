# 📜 Instructions

## Task 1: Create a Secret
1. Log in to the AWS Management Console as the IAM Admin user.
2. Enter `Secrets Manager` in the search bar and open it.
3. Select **Store a new secret** to begin creating the secret.
4. Under **Choose secret type**, select **Other type of secret**.
5. In the **Key/value** tab, enter `The Secret is` as the **Key**.
6. Enter a random secret or hot take that you have as the **Value**
   > Example: I need 3 coffees a day to function

7. Keep the default **Encryption key** setting.
8. Select **Next**.
9. In the **Configure secret** page, enter `TopSecretInfo` under **Secret name**.
10. Under **Description - optional**, add a description like `Secret created for project on Building a Monitoring System`.
11. Click **Next**.
12. Click **Next** again to skip the **Configure rotation - optional** section.
13. Click **Store** at the bottom of the review page.

## Task 2: Configure CloudTrail
14. Enter `CloudTrail` in the AWS console search bar and open it.
15. From the left hand navigation panel, select **Trails**.
16. Select **Create trail** to start setting up a new trail.
17. Under **Trail name**, enter `secrets-manager-trail`.
18. In the **Storage location** section, select **Create new S3 bucket**.
19. Under **Trail log bucket and folder**, enter a unique bucket name.
20. Make sure to uncheck **Log file SSE-KMS encryption** options.
21. Keep the other default settings and click **Next**.
22. On the **Choose log events** page, ensure `Management events` is selected under **Event type**.
23. Under **API activity**, keep both `Read` and `Write` checked.
24. Check `Exclude AWS KMS events` and `Exclude Amazon RDS Data API events`.
25. Select Next and click **Create trail**.

## Task 3: Generate Secret Access Events
26. Navigate back to the `Secrets Manager` console.
27. Pick the created `TopSecretInfo` secret.
28. On the secret details page, scroll down to the **Overview** section.
29. Select **Retrieve secret value** and you should now see the secret value displayed.
30. Select **Close** to close the secret value display.
31. Secrets can also be access using AWS CLI. Open **AWS CloudShell** by clicking on the CloudShell icon in the AWS Management Console's top navigation bar.
32. In the CloudShell terminal, run the following command.
    > make sure to replace `your-region-code` at the end of the command

    ```
    aws secretsmanager get-secret-value --secret-id "TopSecretInfo" --region your-region-code
    ```

33. The command should run successfully and give you the secret's value in JSON format.
34. Head back to the `CloudTrail` console and select **Event history** from the left hand navigation panel.
35. Under **Lookup attributes**, expand the dropdown and choose **Event source**.
36. In the search bar next to **Event source**, enter `secretsmanager.amazonaws.com`.
37. The records are visible under the event called `GetSecretValue`.

## Task 4: Track Secrets Access Using CloudWatch Metrics
38. Still in your CloudTrail console, select **Trails** in the left navigation pane.
39. Select the created trail and scroll down to the CloudWatch Logs section.
40. Select **Edit** and check the `Enabled` checkbox for **CloudWatch Log**.
41. Select **New** log group and enter `secretsmanager-loggroup` for the log group name.
42. Under **IAM Role**, select `New`.
43. Under **Role name**, enter `CloudTrailRoleForCloudWatchLogs_secrets-manager-trail` and select **Save changes**.
44. Head to the CloudWatch console and expand **Logs** and select **Log management** from the left navigation pane.
45. In the Log management page, search for and select `secretsmanager-loggroup`.
46. There should be a few **Log streams**. Pick any one of them and open it.
    > Those timestamp can be expand to view the details recorded inside

47. Head back to the log group and expand `Actions` and then **Create metric filter** from the dropdown menu.
48. In the **Filter pattern** field, enter `GetSecretValue` and select Next.
49. Configure the settings to follow below configuration:
    - filter name: `GetSecretsValue`
    - metric namespace: `SecurityMetrics`
    - metric name: `Secret is accessed`
    - metric value: `1`
    - default value: `0` 

50. Select **Next** and **Create metric filter**. 

## Task 5: Create CloudWatch Alarm and SNS Topic
51. Still in your CloudWatch Alarm's page, select the **Metric filters** tab and select the created metric filter.
52. Select **Create alarm** and configure the settings to follow below configuration:
    - data source: `metrics`
    - type: `classic`
    - metric name: `Secret is accessed`
    - statistic: `Average`
    - period: `5 minutes`
    - threshold type: `static`
    - whenever secret is accessed is: `Greater/Equal`
    - than: `1`

53. Select Next and configure the alarms based on below options:
    - alarm state trigger: `in alarm`
    - Send a notification to the following SNS topic: `Create new topic`
    - topic name: `SecurityAlarms`
    - email endpoints: enter any email
   
54. Select **Create topic** and **Next**. Configure the alarm based on below options:
    - alarm name: `Secret is accessed`
    - alarm description: `This alarm goes off whenever a secret in Secrets Manager is accessed.`

55. Select **Next** and **Create alarm**.
56. Make sure to check the entered email to confirm the subscription to the SNS topic that has been created.

## Task 6: Configure direct SNS notification from CloudTrail [Optional]
57. Head back to CloudTrail console and select **Trails** in the left navigation pane.
58. Select the created trails and click **Edit**.
59. Scroll below to **SNS notification delivery** section under **additional settings**.
60. Enabled the `SNS notification delivery` and select **existing** for create a new SNS topic.
61. Select the created topic and click **Save changes**.
62. This will trigger a notification for every single event compared to CloudWatch alarm (trigger when specific events are met)
63. Navigate to 'AWS Secrets Manager' console and try to retrieve the secret value again > multiple email are received
64. Follow the same configuration steps from step 60 to disabled it. 

## Task 7: Test Email Notification
65. Head back to the Secrets Manager console and try to retrieve the secret value again.
66. Head to your `TopSecretInfo` secret and select **Retrieve secret value**.
67. Retrieving secret value this time did not trigger any notification via email.
68. Few configuration to check to determine where the issue originated from:
    - CloudTrail didn't record the GetSecretValue event.
    - CloudTrail isn't sending logs to CloudWatch.
    - CloudWatch's metric filter isn't filtering logs correctly.
    - CloudWatch's Alarm isn't triggering an action.
    - SNS isn't delivering emails to you.
   
69. Troubleshooting steps documentation can be viewed in the the `Troubleshooting.md` for reference.

## Task 8: Delete Resources
   
Delete the `CloudTrail` trail.

70. Head to the CloudTrail console and select **Trails** in the left navigation panel.
71. Select the checkbox next to the created trail and select **Delete**.
72. Select **Delete**. Confirm the deletion again.

Delete the `S3 bucket` for CloudTrail logs

73. In the S3 console, select the created bucket.
74. Select **Empty**. Confirm the deletion.
75. Select **Delete**. Confirm the deletion again.

Delete the `CloudWatch alarm` and log group

76. Head to the CloudWatch console and select **Alarms** in the left navigation pane.
77. Select the created alarms, select **Delete** and confirm the deletion.

Delete the `Secrets Manager` secret

78. Head to the Secrets Manager console and select **Secrets** in the left navigation pane.
79. Select the created secrets, expand the **Actions** dropdown and click **delete secret**.
80. For **Schedule secret deletion**, set the waiting period to `7` days and click **schedule deletion**.

Delete the `SNS topic and subscription`

81. Head to the SNS console and select **Topics** in the left navigation pane.
82. Select the created topics, click **Delete** and confirm the deletion.
