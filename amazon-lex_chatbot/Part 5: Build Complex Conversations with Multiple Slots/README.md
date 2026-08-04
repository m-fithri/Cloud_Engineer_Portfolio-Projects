# 📌 Overview

The final phase of this project demonstrates how to design, build, and deploy a complete conversational banking chatbot using Amazon Lex.

It showcases advanced conversation management through shared slot types, confirmation prompts, and visual conversation flows, while using AWS CloudFormation to automate deployment and support consistent infrastructure management.

# 🎯 Objective

- Configure multiple slots with a shared slot type.
- Implement a confirmation prompt.
- Use the conversation flow and visual builder.
- Automate bot deployment with CloudFormation.

# ✏️ What I learned

## 🔑 Key Concepts

**1) AWS CloudFormation** 
- An Infrastructure as Code (IaC) service that enables AWS resources to be defined, provisioned, and managed using code templates.

## 🔍 Additional Notes

**2) What Is the Main Benefit of Using AWS CloudFormation to Deploy an Amazon Lex Chatbot?**
- It automates the deployment of the chatbot and its supporting AWS resources from a single template for a consistent deployment.

**3) What Is the Primary Purpose of Confirmation Prompts in a Banking Chatbot?**
- Verify critical information before a transaction or sensitive operation is performed.

**4) Confirmation Prompts**
- A safety check that asks a user if their collected slot data is correct before the bot performs an action

**5) What Does the `TransferFunds` Intent Do?**
- Allow users to transfer their preferred amount from one account to another.

**6) What Does the First Change Accomplish?**
- A new `get slot value` will trigger when the transfer is complete.
- It prompts the user to indicate whether they would like to check their account balance, allowing the conversation to continue without starting a new interaction.

**7) What Was Added Using the Visual Builder?**
- A conditional branch was added to evaluate the user's response after the transfer is complete.
- If the user chooses to check their balance, the chatbot seamlessly transitions to the `CheckBalance` intent.
- Otherwise, the conversation ends gracefully.
