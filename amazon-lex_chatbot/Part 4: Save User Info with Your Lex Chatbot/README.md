# 📌 Overview

The fourth part of this project demonstrates how Amazon Lex uses context carryover to retain slot values between intents.

This enables the chatbot to maintain conversation state and reuse previously collected information to provide a more seamless and natural conversational experience.

# 🎯 Objective

- Set up context carryover of slot values from one intent to the next.

# ✏️ What I learned

## 🔍 Additional Notes

**1) What Does a Slot Type Define in Amazon Lex?** 
- Defines the kind of data that a slot can contain.

**2) What Is the Primary Purpose of an Output Context in Amazon Lex?**
- Stores information after an intent has been fulfilled so it can be used by subsequent intents.

**3) Context Tags (Contexts)**
- Refers to the conversation state variables that allow Amazon Lex to share information across multiple intents.

  | Output context | Input context |
  |---|---|
  | Stores selected information that can be accessed by other intents later in the conversation | Ensures that an intent is only available when the required conversational context already exists |

**4) What Does #contextCheckBalance.dateOfBirth Mean?**
- #contextCheckBalance.dateOfBirth references the dateOfBirth value stored within the contextCheckBalance output context.
- It allows another intent to reuse the previously collected dateOfBirth without prompting the user to enter it again.

**5) How Is FollowupCheckBalance Triggered?** 
- First, the CheckBalance intent is triggered, allowing the chatbot to collect the required information and return a simulated account balance.
- After the CheckBalance intent completes, the contextCheckBalance output context becomes active.
- A follow-up request then triggers the FollowupCheckBalance intent, which reuses the stored context instead of requesting the same information again.

**6) Context Expiry** 
- Determines how long an active context remains available during a conversation.

**7) Why Is Context Expiry Useful?**

| Short context expiry | Longer context expiry |
|---|---|
| Useful for sensitive information handling | Useful for extended conversation |
| Limits how long user data remains available during conversation and reduce potential security risks | Allow chatbot to retain relevant information across multiple intents to provide a seamless conversation and minimizing repeated prompts | 

