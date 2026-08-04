# 📜 Instructions

## Task 1: Set up Lex Chatbot
1. Log in to the **AWS console** as IAM admin user.
2. Search for `Amazon Lex` in the AWS console and open it.
3. Click **Create bot** and configure the settings based on below options:
   - **Creation method**: create a blank bot
   - **Bot name**: `BankerBot`
   - **Description**: `Banker Bot to help customer check their balance and make transfers`.
   - **IAM permissions runtime role**: create a new service role with basic amazon lex permissions
   - **Bot error logging**: disabled
   - **Children online privacy protection act (COPPA)**: no
   - **Idle session timeout**: 5 minutes

4. Click **Next** and configure the bot settings based on below options:
   - **Language**: default English (US)
   - **Voice interaction**: Danielle
   - **Intent classification confidence score threshold**: default value of 0.40
  
5. Select **Done**.

## Task 2: Create the first Intent
6. When the bot is created, it will automatically display a page called **Intent: NewIntent**.
7. Under Intent details, enter `WelcomeIntent` for the **Intent name** and **Display name**.
8. Enter `Welcoming a user when they say hello.` for the intent description.
9. Scroll down to the **Sample utterances panel** and click the **Plain Text** button.
10. Copy and paste below text which represent the user inputs (called utterances) that will trigger this intent
    ```
    Hi
    Hello
    I need help
    Can you help me?
    ```

11. Scroll down to **Closing response** and expand the **Response sent to the user after the intent is fulfilled** dropdown.
12. In the **Message** field, enter `Hi! I'm BB, the Banking Bot. How can I help you today?`.
13. Choose **Save intent** and **Build** which is located at the top of the screen.
14. Click **Test** and enter any sample utterance that has been specified earlier in step 10.
15. Try using these phrases as well:
    ```
    Help me
    Hiya
    How are you
    Good morning
    ```

16. Try two of these utterances again, this time using voice to validate whether voice input is working.

## Task 3: Manage FallbackIntent
17. From left hand navigation panel, choose **FallbackIntent**.
18. Scroll down to **Closing responses** and expand the **Response sent to the user after the intent is fulfilled** dropdown.
19. Enter below text in the **Message** field:
    ```
    Sorry I am having trouble understanding. Can you describe what you'd like to do in a few words? I can help you find your account balance, transfer funds and make a payment.
    ```

20. Expand the **Variations - optional** dropdown and enter below text:
    ```
    Hmm could you try rephrasing that? I can help you find your account balance, transfer funds and make a payment.
    ```

21. Add another variation, click **Save intent** and click **Build**.
22. Click **Test** and enter two or three of the failed utterances response from the last attempt (step 16).

## Task 4: Add Initial Response [Optional]
23. Navigate to **Initial response** section and expand **Response to acknowledge the user's request** dropdown.
24. Enter `Hmmm this is interesting...` for the message value.
25. Expand **Variations - optional** dropdown, enter `One moment...` and `Hold on!`.
26. Click **Save intent** and select **Build**.
27. Start a test session with the chatbot and enter some of other phrases to trigger variations in the bot response.

## Task 5: Delete Resources [Optional]
28. Navigate to Amazon Lex console.
29. Under **Bots** section, select the created bot and expand the **Actions** dropdown.
30. Select **Delete** and confirm the deletion.
