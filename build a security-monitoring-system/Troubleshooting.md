# ❓ Troubleshooting

## Troubleshoot 1: CloudTrail didn't record the GetSecretValue event

1. Head to the CloudTrail console and select **Event history** from the left navigation pane.
2. Under **Lookup attributes**, select the dropdown and choose **Event source**.
3. In the search bar next to Event source, enter `secretsmanager.amazonaws.com`.
4. At least one `GetSecretValue` event will shows up at the top of the list which matches the time you viewed your secret.
5. This means that CloudTrail did capture the event.

## Troubleshoot 2: CloudTrail isn't sending logs to CloudWatch
6. Still in the CloudTrail console, select **Trails** from the left navigation pane.
7. Select the created trails and check the Last log file delivered timestamp (it should be recent if logs are being delivered properly)
8. Scroll down to the **CloudWatch Logs** section and make sure it shows the correct log group name.
9. This means that CloudTrail is sending logs over to CloudWatch.

## Troubleshoot 3: CloudWatch's metric filter isn't filtering logs correctly
10. Head to the CloudWatch console and select **Log management** from the left navigation pane.
11. Select the created log groups and navigate to **metric filters** tab.
12. Select the created metric filters and click **Edit**.
13. Enter the text shown in `log event patter test.txt` into **log event messages** panel and click **test pattern**.
14. The results shows list of event records under `GetSecretValue`.
15. This means that the metric filter does correctly filter for events where the secret is accessed.

## Troubleshoot 4: CloudWatch's Alarm isn't triggering an action
16. Open AWS CloudShell and enter below command to trigger the alarm manually:
    ```
    aws cloudwatch set-alarm-state \
        --alarm-name "Secret is accessed" \
        --state-value ALARM \
        --state-reason "Manually triggered for testing"
    ```

17. Check the email inbox. There should be a notification email that the alarm is **in alarm**, and Manually triggered for testing as the reason.
18. Head back to the CloudWatch console and select **All alarms** from the left navigation pan.
19. Select the created alarms, expand the **Actions** dropdown and click **Edit**.
20. In metric, change the statistic to `sum` & period to `1 minute`.
21. Make sure the configuration below is still the same:
    - threshold type: `static`
    - whenever secret is accessed is: `Greater/Equal`
    - than: `1`

22. Select **Skip to Preview and create** and select **Update alarm**.

## Troubleshoot 5: SNS isn't delivering emails to you
23. Head to the SNS console and select **Topics** from the left navigation pane.
24. Select the created topics and select **Publish message**.
25. Add a message **Subject** like `Testing`.
26. In the **message body**, enter a quick message like `Wassup`.
27. Select **Publish message**
28. Message received via email so this means that SNS is set up properly.

---

29. After all above troubleshooting steps are done, head back to the Secrets Manager console and try to retrieve the secret value again.
30. Head back to the CloudWatch console and refresh the **Secret is accessed** alarm.
31. It should be in the **In alarm** state.
32. Head back to your email inbox and look for an email from **AWS Notifications** with the subject `ALARM: "SecretIsAccessedAlarm"`.
33. This confirms that the monitoring system is working.
