# 📌 Overview

The second part of this project focuses on building a chatbot that collects and validates user information using Amazon Lex slots.

By the end of this section, the chatbot is capable of capturing user details through custom and built-in slots, while automatically extracting slot values from the user's initial input to streamline the conversation.

# 🎯 Objective

- Define a custom slot type.
- Associate custom and built-in slots to your intent.
- Parse slot values from the initial utterance.

# ✏️ What I learned

## 🔍 Additional Notes

**1) Slots** 
- Pieces of information that Amazon Lex collects from a user to fulfill an intent.

**2) Why Include the text `{accountType}` in the Sample Utterances for the CheckBalance Intent?**
- The {accountType} placeholder tells Amazon Lex to extract the accountType slot directly from the user's input. 

**3) What Does the "Restrict to Slot Values" Setting Do?**
- This option limits a slot to a predefined list of acceptable values.
- If the user provides a value that is not in the list, Amazon Lex considers the slot unfulfilled and prompts the user to provide a valid value.

**4) Why Use "Restrict to Slot Values" for `accountType`?**
- Restricting the `accountType` slot ensures that only supported account types (such as Checking or Savings) are accepted.

**5) What Does the CheckBalance Intent Do?** 
- Enables users to request their bank account balance.

**6) Why Does the Bot Say "Intent CheckBalance Fulfilled"?** 
- An intent is considered fulfilled when Amazon Lex has successfully collected all required slot values.
- In this stage of the project, the chatbot gathers the user's information but does not yet connect to a backend service to retrieve the actual account balance (showing "Intent CheckBalance fulfilled" instead of a real account balance).

**7) What Does "Slot Capture: Failure Response" Do?**
- Defines how the chatbot responds when it cannot obtain a valid value for a required slot.

**8) Why Does `FallbackIntent` Appear?** 
- It is triggered when Amazon Lex is unable to determine the user's intent or repeatedly fails to collect valid slot values.
- In this case, the chatbot requests a date of birth multiple times and the user continues to provide invalid or unrelated responses
- Chatbot then trigger `FallbackIntent` to recover from the conversation or allow the user to switch to a different intent.
