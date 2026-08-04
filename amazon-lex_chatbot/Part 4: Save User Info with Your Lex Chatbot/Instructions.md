# 📜 Instructions

## Task 1: Remember information stored in `CheckBalance`
1. Log in to the **AWS console** as IAM admin user.
2. Search for Amazon Lex in the console and open it.
3. In Amazon Lex console on **CheckBalance** intent page, scroll down to **Contexts** panel.
4. Expand **Output contexts** dropdown and choose **New context tag**.
5. Enter `contextCheckBalance` for the context tag name and set up the timeout for **5 turns**, or **90 seconds**.
6. Choose **Add** and **Save intent**.
7. Click **Build** and **Test**.
8. Enter some message to make sure the bot still operates the same as usual without receiving any error.

## Task 2: Create the `FollowupCheckBalance` intent
9. Navigate to amazon lex **intent list** from the left navigation panel
10. Expand **Add intent** dropdown and select **Add empty intent**.
11. Enter `FollowupCheckBalance` as the intent name and `Intent to allow a follow-up balance check request without authentication.` as its description.
12. Scroll below to the **Context** section and select `contextCheckBalance` as input context.
13. For **Sample utterances** section, switch to **Plain text** and enter below message:
    ```
    How about my {accountType} account?
    What about {accountType} ?
    And in {accountType} ?
    ```

14. Under **Slots - optional** section, click **Add slot** and configure with below options:
    - **Name**: `accountType`
    - **Prompt**: `For which account would you like your balance?`
    - **Slot type**: **accountType**
  
15. Add another slot and configure with below options:
    - **Name**: `dateOfBirth`
    - **Prompt**: `For verification purposes, what is your date of birth?`
    - **Slot type**: **AMAZON.Date**

16. Click **Save intent**.

## Task 3: Finishing Touches for `FollowupCheckBalance`
17. Still in the **FollowupCheckBalance** intent page, expand the **dateOfBirth** slot and select **Advanced options**.
18. Scroll all the way down to the **Default values - optional** section and expand it.
19. Enter `#contextCheckBalance.dateOfBirth` as the default value and click **Add default value**.
20. Choose **Update slot**.
21. Navigate to **Fulfillment** section and expand **On successful fulfillment**.
22. Select **Advanced options**.
23. Head to the **Fulfillment Lambda code hook** section and make sure **Use a Lambda function for fulfillment** option is enabled.
24. Click **Update options** and **Save intent**.
25. Select **Build** and **Test**.
26. For the first test, try to trigger the `FollowupCheckBalance` intent without triggering `CheckBalance` first.
    > Enter `What about checking?`

27. Received an error response since the `FollowupCheckBalance` intent input context isn't available yet.
28. Refresh the chat. For the second test, ask for balance in your account.
    > Activate the `CheckBalance` intent first

29. Then, the context for date of birth will be carried over to the `FollowupCheckBalance` intent.

## Task 4: Context Expiry [Optional]
30. Head to `CheckBalance` intent and scroll below to the **Context - optional** section.
31. Notice that the output context has been already set up to **5 turns or 90 seconds** from the previous steps.
32. Proceed to **Test** to start a conversation with the bot.
33. Enter `check my savings account balance` and `19th January 1993` for birth date.
34. Click **Inspect**.
    > Notice that `contextCheckBalance` is active and it says there are **5 turns or 90 seconds** left

35. Enter `what about checking?` to trigger `FollowupCheckBalance`.
    > Notice that the `contextCheckBalance` is updated to **4 turns and a bit less time** left

36. Try asking `what about credit?` after time passed and it returns a `FallbackIntent` response.
37. To customize the context expiry, navigate to the **CheckBalance** intent under **Context - optional** section.
38. Click the gear icon to customized it and make it shorter.
    > Change it to **2 turns or 10 seconds**
  
39. Click **Save** and **Save intent**.
40. Select **Build** and **Test**.
41. Enter `check my savings account balance` and `19th January 1993` as birth date.
42. Click **Inspect**.
    > `contextCheckBalance` is active and it says there are 2 turns or 10s left

43. Activate `FollowupCheckBalance` by entering `what about checking?` and it should returns a `FallbackIntent` response.

## Task 5: Delete Resources [Optional]

Delete Lex Bot

44. Navigate to Amazon Lex console.
45. Under **Bots** section, select the created bot and expand the **Actions** dropdown.
46. Select **Delete** and confirm the deletion.

Delete Lambda function

47. Navigate to AWS Lambda console.
48. Choose **Functions** from the left navigation panel and select the created functions.
49. Expand the **Actions** dropdown, select **Delete** and confirm the deletion.

Delete Lambda function log files

50. Navigate to CloudWatch console.
51. Select **Logs management** from the left navigation panel and select created log groups.
52. Expand the **Actions** dropdown, select **Delete** and confirm the deletion.
