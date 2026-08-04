# 📜 Instructions

## Task 1: Create the new `TransferFunds` intent
1. Log in to the **AWS console** as IAM admin user.
2. Navigate to Amazon Lex intents page, click **Add intent** and **Add empty intent**.
3. Enter `TransferFunds` as intent name and `Help user transfer funds between bank accounts` as its description.
4. Scroll below to **Sample utterances** and enter:
   ```
   Can I make a transfer?
   I want to transfer funds
   I'd like to transfer {transferAmount} from {sourceAccountType} to {targetAccountType}
   Can I transfer {transferAmount} to my {targetAccountType}
   Would you be able to help me with a transfer?
   Need to make a transfer
   ```

5. Navigate to **Slots - optional** and select **Add slot**.
6. Configure the slots based on below options:
   - **name**: `sourceAccountType`
   - **type**: `accountType`
   - **prompts**: `Which account would you like to transfer from?`

7. Add a new slot and configure it based on below options:
   - **name**: `targetAccountType`
   - **type**: `accountType`
   - **prompts**: `Which account are you transferring to?`

8. Add another new slot and configure it based on below options:
   - **name**: `transferAmount`
   - **type**: `AMAZON.Number`
   - **prompts**: `How much money would you like to transfer?`

9. Scroll to **Confirmation** section and expand **Prompts to confirm the intent**.
10. In **Confirmation prompt** panel, enter the following:
    ```
    Got it. So we are transferring {transferAmount} from {sourceAccountType} to {targetAccountType}. Can I go ahead	with the transfer?
    ```

11. In **Decline response**, enter `The transfer has been cancelled.`.
12. Scroll to **Closing response** and enter the following:
    ```
    The transfer is complete. {transferAmount} should now be available in your {targetAccountType} account.
    ```

13. Click **Save intent**, then click **Build** and **Test**.
14. Enter below text in sequence for the new conversation:
    ```
    I'd like to transfer money.
    checking
    savings
    4000
    yes
    ```
    
15. Enter `transfer 5000 from amex to savings` for second conversation and the transfer should be complete in much shorter conversation.
    > The values for `transferAmount` and `targetAccountType` has been included in the utterance

## Task 2: Explore Cool features in Amazon Lex
16. Scroll to the very top of the intents page and head to **Conversation flow** panel. 
17. Expand the **Conversational flow** dropdown and select **Visual builder** in the bottom bar of the screen.
18. Explore the visual representation of the the intent that has been built for references.

## Task 3: Using the Visual Builder [Optional]

In this task, we will set up the bot to automatically ask user whether they would like to check an account balance after a transfer

First changes:

19. Drag the **End conversation** card to the far right end.
20. From the visual builder top menu bar, drag the **Get slot value** card and put it right next to the **Closing response** card.
21. Drag the **Condition** option from the top menu bar to sit right next to **Get slot value**.
22. Drag the **Go to intent** option from the top menu bar and place it underneath the **Condition** card.
23. Select the pencil icon to edit, navigate to **Get slot value** and configure below options:
    - **name**: `GoToCheckBalance`
    - **description**: `Checks whether the user wants to check account balance`
    - **slot type name**: `AMAZON.Confirmation`
    - make sure **Required for this intent** option is selected
    - **slot prompt**: `Would you also like to check an account balance?`
    - **success response**: `Thanks for letting me know`
    - **error response**: `Sorry, was that a yes or a no?`

24. For the blue **Closing response** card, select the arrow pointing out from **The transfer is complete** message and press `backspace` or `delete` on your keyboard.
25. Click and hold the empty circle next to **The transfer is complete** message then drag it to **Get slot value** card.
26. Drag the arrow from **Success** outcome in **Get slot value** card. Conversation should move towards the **Condition** card if it was a success.
27. For **Failure**, move the conversation back to the `FallbackIntent`. 

---

Second changes:

28. Select the pencil icon on the top right of the **Condition** card. Click **Add conditional branch** and configure below options:
    - **branch name**: `Yes`
    - **condition**: `if user response matches yes in AMAZON.Confirmation: {GoToCheckBalance} = "Yes"`

29. Complete the **Condition** by configuring below:
    - Drag arrow from **Default** branch to **End conversation**.
    - Drag arrow from **Yes** branch to new **Go to intent** card.

30. Select pencil icon of the **Go to intent** card.
31. For intent name, expand the dropdown and select `CheckBalance`.
32. You can auto arrange the card by clicking the **glitter icon** above the zoom in icon.
33. Click **Save intent**, then select **Build** and **Test**.
34. Trigger the `TransferFunds` intent by entering below message in the chat:
    ```
    Transfer $50.44 from checking to savings
    yes
    yes
    ```

## Task 4: Delete Resources

Delete Lex Bot

35. Navigate to Amazon Lex console.
36. Under **Bots** section, select the created bot and expand the **Actions** dropdown.
37. Select **Delete** and confirm the deletion.

Delete Lambda function

38. Navigate to AWS Lambda console.
39. Choose **Functions** from the left navigation panel and select the created functions.
40. Expand the **Actions** dropdown, select **Delete** and confirm the deletion.

Delete Lambda function log files

41. Navigate to CloudWatch console.
42. Select **Logs management** from the left navigation panel and select created log groups.
43. Expand the **Actions** dropdown, select **Delete** and confirm the deletion.

## Task 5: Deploy your bot in seconds

44. Search for **CloudFormation** in the AWS console and open it.
45. Expand **Create stack** drop down and select **With new resource (standard)**.
46. Select **Choose an existing template** for prepare template and **Upload a template file** for specify template.
47. Upload the `nextwork-banker-bot.yaml` file and select **Next**.
48. Enter `nextwork-banker-bot` for stack name and select **Next**.
49. Scroll below to the **Capabilities and transform** section and select all acknowledgement option.
50. Click **Next** and **Submit**.
51. Navigate to **Stack info** and wait until the stacks status shows **CREATE_COMPLETE**.
52. Search for **Amazon Lex** in the AWS console and open it.
53. Select the created `network-banker-bot-BankerBot` and select **Intents**.
    > Notice that a few more intents are already created

54. Connect the `TestBotAlias` with Lambda function by navigating to **Aliases** and select `TestBotAlias`.
55. Click on **English (US)** and expand **Source** dropdown to select **Lex V2**
56. Click **Save**.
57. Navigate back to **Intents** section then click **Build** and **Test**.
58. Enter below text into the conversation in sequence:
    ```
    check my balance
    checking
    1/1/98
    ```

    >  Receive an 'Invalid Bot Configuration: Access denied while invoking lambda function' error

59. Troubleshoot the error by creating a new lambda function based on below configuration:
    - **function name**: `BankingBotEnglish`
    - **runtime**: `python 3.12`

60. Select **Create function** then navigate to code section and paste the code shown in `BankingBotEnglish.py`.
61. Click **Deploy**.
62. Navigate back to Amazon Lex console, select **Bot** and select **Aliases**.
63. Click `TestBotAlias` and **English (US)**.
64. Expand **Source** dropdown to select `BankingBotEnglish` and click **Save**.
65. Navigate to **Intents** then click **Build** and **Test**.
66. Enter below text into the conversation in sequence:
    ```
    check my balance
    checking
    1/1/98
    ```

    > Receive an 'Invalid Bot Configuration: Access denied while invoking lambda function' error

67. Head back to `BankingBotEnglish` Lambda functions and select **Configuration**.
68. Select **Permission** and scroll to **Resource-based policy statements**.
69. Click **Add permission** and configure below options for **Edit policy statement** under **AWS service**:
    - **Service**: `Other`
    - **Statement ID**: `my-custom-permission-amazonlexchatbot`
    - **Principal**: `lexv2.amazonaws.com`
    - **Source name**: find the ARN from the error message (eg. arn:aws:lex:ap-southeast-2:640168412593:bot-alias/*).
    - **Action**: `lamdaInvokeFunction`
   
70. Click **Save**.
71. Navigate back to Lex console then click **Build** and **Test**.
72. Enter below text into the conversation in sequence:
    ```
    check my balance
    checking
    1/1/98
    ```

73. The conversation should be working now without any error received.

## Task 6: Delete Resources

Delete CloudFormation stack

74. Head back to CloudFormation console.
75. Search for the created stack, select **Delete stack** and confirm deletion.

Delete Lambda function log files

76. Navigate to CloudWatch console.
77. Select **Logs management** from the left navigation panel and select created log groups.
78. Expand the **Actions** dropdown, select **Delete** and confirm the deletion.
