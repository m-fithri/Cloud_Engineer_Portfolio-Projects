# 📌 Overview

The third part of this project demonstrates how Amazon Lex integrates with AWS Lambda to build a functional conversational application.

By the end of this section, the chatbot is capable of executing backend logic through code hooks, allowing it to process user requests and generate dynamic, data-driven responses.

# 🎯 Objective

- Set up a Lambda function
- Integrate the Lambda function with your chatbot's alias.
- Use code hooks to perform the final fulfillment step of the intent.

# ✏️ What I learned

## 🔑 Key Concepts

**1) AWS Lambda** 
- A serverless compute service that allows code to run without provisioning or managing servers - Function as a Service (FaaS).

## 🔍 Additional Notes

**2) What Is the Primary Purpose of Code Hooks in Amazon Lex?**
- Enable an Amazon Lex chatbot to invoke an AWS Lambda function during a conversation.

**3) What Does Amazon Lex Use to Collect Information Required to Fulfill an Intent?**
- Slots

**4) Which Intent Is Triggered When Amazon Lex Cannot Understand a User's Request?**
- FallbackIntent

**5) What Are Aliases in Amazon Lex?**
- A pointer to a specific version of an Amazon Lex bot to simplify updates & connections with other AWS services.

**6) What Does the Lambda Function Do in This Project?**
- It generates and returns a simulated bank account balance when a user submits a balance inquiry.

**7) TestBotAlias**
- The default alias created for testing and development purposes.

**8) What Does $LATEST Mean?**
- Refers to the most recent unpublished version of a Lambda function.

**9) What Does Fulfillment Mean in Amazon Lex?**
- Final stage of an intent after all required slot values have been collected.

**10) Code Hooks**
- Integration points that allow Amazon Lex to invoke AWS Lambda functions during different stages of a conversation.
