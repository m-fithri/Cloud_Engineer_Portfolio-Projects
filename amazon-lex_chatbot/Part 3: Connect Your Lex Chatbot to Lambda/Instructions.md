# 📜 Instructions

## Task 1: Create AWS Lambda Function
1. Log in to the **AWS console** as IAM admin user.
2. Search for `Lambda` in the AWS console and open it.
3. Select **Create a function** and choose **Author from scratch**.
4. Enter `BankingBotEnglish` for the function name and select **Python 3.14** for the runtime option.
5. Click **Create function**.
6. Scroll down to the **Function code** section and double-click on `lambda_function.py`.
7. Paste the code shown in `BankingBotEnglish.py` into the code source field and click **Deploy**.

## Task 2: Connect AWS Lambda with Amazon Lex
8. Head back to Amazon Lex console and select the created bot.
9. Select **Aliases** from the left navigation panel and choose the default `TestBotAlias`.
10. On **Languages** panel, click on **English (US)**.
11. Select **BankingBotEnglish** as source and leave `$LATEST` as the default lambda function version.
12. Click **Save**.

## Task 3: Connect CheckBalance intent with Lambda function
13. Navigate back to the `CheckBalance` intent and scroll down to **Fulfillment** section.
14. Expand **On successful fulfillment** and choose **Advanced options**.
15. Under the **Fulfillment lambda code hook** panel, make sure the **Use a lambda function for fulfillment** option is selected.
16. Click **Update options** and click **Save intent**.
17. Click **Build** and **Test**.
18. Enter `Check my balance` in the bot conversation and provide the account type.
19. Enter any date of birth for verification and it should returns a random bank balance figures.

## Task 4: Customize the Lambda function [Optional]
20. Navigate back to **Lambda** under the **Code** section.
21. Enter the code shown in **fun_twist.py** in line 65 of the code and replace `YOUR-NAME` with your name.
22. Click **Deploy**.
23. Head back to **CheckBalance** intent and select **Test**.
    > If the previous test chat window are still active, click **Refresh** icon to restart the conversation

24. Enter `Check my Savings account` in the chat and provide any date of birth for verification. It will shows up a new response.
25. Head back to **Lambda** under **Code** section.
26. In line 66 of the code, include an additional response for descriptions and click **Deploy**.
    > Example: `bank of NextWork` and `another cool location`.

27. Head back to **CheckBalance** intent and select **Test**.
28. Enter `savings` and provide any date of birth for verification. It will shows up a new response.

## Task 5: Delete Resources [Optional]

Delete Lex Bot

29. Navigate to Amazon Lex console.
30. Under **Bots** section, select the created bot and expand the **Actions** dropdown.
31. Select **Delete** and confirm the deletion.

Delete Lambda function

32. Navigate to AWS Lambda console.
33. Choose **Functions** from the left navigation panel and select the created functions.
34. Expand the **Actions** dropdown, select **Delete** and confirm the deletion.

Delete Lambda function log files

35. Navigate to CloudWatch console.
36. Select **Logs management** from the left navigation panel and select created log groups.
37. Expand the **Actions** dropdown, select **Delete** and confirm the deletion.
