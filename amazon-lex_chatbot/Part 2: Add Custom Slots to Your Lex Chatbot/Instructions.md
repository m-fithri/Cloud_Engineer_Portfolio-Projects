# 📜 Instructions

## Task 1: Create a custom slot for account types
1. Log in to the **AWS console** as IAM admin user.
2. In the Amazon Lex console, select **Slot types** from left hand navigation panel.
3. Expand the **Add slot type** dropdown and select **Add blank slot type**.
4. Enter `accountType` for the **Slot type name** and choose **Add**.
5. In the **Slot value resolution** panel, choose **Restrict to slot values**.
6. In the **Values** field, enter `Checking` and select **Add value**.
7. Enter `Savings` and select **Add value**.
8. Enter `Credit` and add a few synonyms in the second field. Press `;` on your keyboard after every time you add in a new one:
   - credit card
   - visa
   - mastercard
   - amex
   - american express

9. Choose **Add value** to finish up your work for **Credit** and select **Save slot type**.

## Task 2: Create the CheckBalance intent
10. In the left hand navigation panel, head back to **Intents**.
11. Expand the **Add intent** dropdown and select **Add empty intent**.
12. Enter `CheckBalance` for intent name and click **Add**.
13. Enter the following description in the **Intent description** panel:
    ```
    Intent to check the balance in the specified account type.
    ```

14. Scroll down to **Sample utterances**, switch to **Plain Text** and paste in the following utterances:
    ```
    What’s the balance in my account?
    Check my account balance
    What’s the balance in my {accountType} account?
    How much do I have in {accountType} ?
    I want to check the balance
    Can you help me with account balance?
    Balance in {accountType}
    ```

15. Scroll down to the **Slots** panel and choose **Add slot**.
16. For slot's **Name**, enter `accountType`.
17. For the **Slot type**, choose your custom slot value accountType that has been created in Part 1.
18. Enter `For which account would you like your balance?` for **Prompts** and choose **Add**.
19. Click **Add slot** again and fill in these values for the next slot:
    - Name: `dateOfBirth`
    - Slot type: `AMAZON.Date`
    - Prompts: `For verification purposes, what is your date of birth?`

20. Choose **Save intent** and choose **Build**
21. Choose **Test** and start a new conversation by entering below text in sequence:
    ```
    I want to check my balance please.
    Checking
    1/1/1993
    ```

22. Click **Inspect** near the top of the chat window.
    > Notice that the bot already filled both slots `accountType` and `dateOfBirth` with information it knows about you

23. Enter `What's the balance in my savings account?` in the conversation.
    > This time, it will only prompt you for your date of birth as it already knows that it should be checking the `Savings` account

## Task 3: Handling Errors in Responses [Optional]
24. Still in the **CheckBalance** intent, head back to the **Slots** panel.
25. Expand the **dateOfBirth** dropdown and select **Advanced options**.
26. Scroll below to **Slot prompts** and expand **bot elicits information**.
27. Expand **Variations - optional** and enter `Sorry, that wasn't clear to me. What's your date of birth?`.
    > Notice that there is an option for **play the messages in order**.
 
    > By toggling this on, it means the message slot prompts will not be selected randomly and play in order instead.

28. Add another variations.
29. Navigate to **Slot capture: failure response** section and expand **Response when slot isn't understood** dropdown.
30. Enter `It looks like the dates provided weren't right. Can you re-enter it? Just the month, day and year will do, like June 15, 1995` in the message field.
31. Expand **Variations - optional** and enter `I don't think you've entered a date. I need your birth date for verification`.
32. Add another variations.
33. Click **Update slot**, select **Save intent** and **Build**.
34. Select **Test** and enter below text in a row to trigger the `checkbalance` intent again:
    ```
    Check my Savings balance
    I want to see the balance in Checking
    Balance in Credit
    ```

35. In `CheckBalance` intent, select **Advanced options** under the `dateOfBirth` slot and scroll to **Slot capture: failure response**.
36. Expand **Set values** dropdown and look for **Next step in conversation**.
37. Default selection value is to move to another **Intent** which is `FallbackIntent`.
38. Expand **Intent** dropdown and select **Elicit a slot**.
39. Choose `dateOfBirth` under **Slot** and toggle turn on **Skip elicitation prompt** option.
40. Select **Update slot** then click **Build** and **Test**.
41. Trigger `CheckBalance` intent by entering `Balance in Credit` in the chat.
42. Enter below text in the conversation as well in sequence:
    ```
    cheese
    what's YOUR birthday?!
    I have no clue
    not today
    I dont know
    ```

    > This time, the default settings for failure response is changed to clarify that the bot is still expecting a birth date as response for verification instead of switching to `FallbackIntent`.

## Task 4: Delete Resources [Optional]
43. Navigate to Amazon Lex console.
44. Under **Bots** section, select the created bot and expand the **Actions** dropdown.
45. Select **Delete** and confirm the deletion.
