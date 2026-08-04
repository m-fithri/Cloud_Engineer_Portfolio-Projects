# 📌 Overview

The first part of this project focuses on building the foundation of an AI chatbot using Amazon Lex.

By the end of this section, a basic chatbot is built and tested to recognize user greetings, respond with natural conversational flow, and gracefully handle unrecognized inputs through fallback logic.

# 🎯 Objective

- Set up a basic intent (WelcomeIntent)
- Create lists of utterances
- Handle failures with FallbackIntent
- Define a MessageGroup to send variations in your bot's responses
- Build and test your bot using text and speech 

# ✏️ What I learned

## 🔑 Key Concepts

**1) Artificial Intelligence (AI)** 
- Ability of computer systems to perform tasks that typically require human intelligence.

**2) Amazon Lex**
- An AWS service for building conversational interfaces using both voice and text,

## 🔍 Additional Notes

**3) Fallback Intent**
- A built-in Amazon Lex intent that handles user inputs which do not match any defined intent with sufficient confidence (safety mechanism).

**4) When Is FallbackIntent Triggered?**
- When Amazon Lex cannot confidently match a user's input to any configured intent (confidence score below the configured Intent Classification Confidence Score Threshold).

**5) What Does an Intent Represent?**
- Represents the user's goal or the action they want the chatbot to perform.

**6) Intent Classification Confidence Score Threshold**
- The minimum confidence score Amazon Lex requires before matching a user's input to a specific intent.
- High score = greater confidence.
- Lower score = trigger FallbackIntent.

**7) Why Define Multiple Response Variations?**
- Allow the chatbot to provide a dynamic range of responses, making the chatbot sound more conversational.

**8) Idle Session Timeout**
- Defines how long a conversation remains active when there is no user interaction.

**9) Initial Response**
- The first message sent by the chatbot when a conversation begins or when an intent is triggered.
