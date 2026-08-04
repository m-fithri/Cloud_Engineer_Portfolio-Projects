# Three-tier Web App

## 📌 Overview

Conversational AI is transforming how businesses interact with customers by providing fast, personalized, and automated support.

This project demonstrates how to build an AI-powered banking chatbot using **Amazon Lex** and AWS services to simulate a real-world customer support solution.

By the end of the project, the chatbot can understand natural language, recognize banking-specific requests, retrieve account information through backend logic, and maintain conversational context to deliver a seamless user experience.

---

The project is structured into five parts, each covering a specific set of objectives as outlined below:

**Part 1: Build Your First Chatbot with Amazon Lex**
- Set up a basic intent (WelcomeIntent).
- Create lists of utterances.
- Handle failures with **FallbackIntent**
- Define a **MessageGroup** to send variations in your bot's responses.
- Build and test your bot using text and speech.

**Part 2: Add Custom Slots to Your Lex Chatbot**
- Define a custom slot type.
- Associate custom and built-in slots to your intent.
- Parse slot values from the initial utterance.

**Part 3: Connect Your Lex Chatbot to Lambda**
- Set up a Lambda function.
- Integrate the Lambda function with your chatbot's alias.
- Use code hooks to perform the final fulfillment step of the intent.

**Part 4: Save User Info with Your Lex Chatbot**
- Set up context carryover of slot values from one intent to the next.

**Part 5: Build Complex Conversations with Multiple Slots**
- Configure multiple slots with a shared slot type.
- Implement a confirmation prompt.
- Use the conversation flow and visual builder.
- Automate bot deployment with **CloudFormation**.

## 🛠️ Technologies & Tools

`AI`  `AI Chatbots`  `Amazon Lex`  `AWS Lambda`  `AWS CloudFormation`
