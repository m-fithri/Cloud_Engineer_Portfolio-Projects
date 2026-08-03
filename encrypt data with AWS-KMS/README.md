# Data Encryption with AWS Key Management Service (KMS)

## 📌 Overview

Protecting sensitive data is a fundamental responsibility in modern cloud environments, as unauthorized access can lead to data breaches, financial loss, and reputational damage.

One of the most effective ways to safeguard data is through encryption, which converts readable information into an unreadable format that can only be accessed by authorized users with the appropriate encryption keys.

This project demonstrates how encryption is used in AWS to protect sensitive data both at rest and in transit while ensuring that only authorized users and services can access it.

By completing this project, you'll gain a practical understanding of encryption concepts, key management, and AWS security best practices for protecting data in production environments.

---

The goals of this project are to:
- Create and manage encryption keys using AWS Key Management Service (AWS KMS).
- Encrypt an Amazon DynamoDB table with a customer-managed KMS key.
- Add and retrieve data from the encrypted DynamoDB table to verify successful encryption and access.
- Observe how AWS KMS protects data by preventing unauthorized access without the appropriate permissions.
- Grant an IAM user permission to use the KMS key and access the encrypted data securely.

## 🛠️ Technologies & Tools

`AWS KMS` `Amazon DynamoDB` `AWS IAM`

## 🏗️ Architecture

```

                           ──────────────────────────────────
                          │                                  │
                          │     🗝                           │
                          │   [ KMS Encryption Key ]         │ ✅ ◀ ══════════   [ IAM Admin User ]
   [ KMS ]  ══════════ ➤ │                                  │
                          │                                  │
                          │                [ DynamoDB ]      │ ❌ ◀ ══════════   [ Test User ]
                          │                                  │
                          │                                  │
                           ──────────────────────────────────

```

## ✏️ What I learned

### 🔑 Key Concepts

**1) AWS Key Management Service (KMS)**
- A managed service that lets you create and control the cryptographic keys used to protect your data.

**2) Amazon DynamoDB**
- A fast, fully managed, serverless NoSQL database service under AWS.
- Stands out as a fast and flexible way to store data.
- Is schemaless, meaning you can add attributes as you need, and every item in your database can have a different set of attributes.

**3) AWS IAM**
- A web service that helps you securely control access to AWS resources.

### 🔍 Additional Notes

**4) Encryption**
- A process that uses algorithms to convert data into a secure format called ciphertext.
- Only authorized users can decrypt and restore the data to its original, readable state.

**5) Encryption Keys**
- Tells the algorithm exactly how it would transform plain text into the jumbled up format called cipher text.

**6) AWS Managed Keys vs Customer Managed Keys**

| AWS managed keys | Customer managed keys |
|---|---|
| Automatically created and managed by AWS to encrypt data in the services you used | Gives you full control on how it encrypts data & who can access the key |

**7) Symmetric Encryption vs Asymmetric Encryption**

| Symmetric Encryption | Asymmetric Encryption |
|---|---|
| Use a single encryption key to both lock (encrypt) and unlock (decrypt) the data | Use pair of keys: public key to encrypt & private key to decrypt |

**8) Key Lifecycle**
- Stages an encryption key goes through, from creation to deletion.

**9) Partition Key**
- Filter/ways DynamoDB use to sort data.

**10) Why Create a User without KMS access?**
- To validate whether a user without access to the KMS key can view the data in DynamoDB.

**11) Why Test User Access is Denied?**
- The test user does not have the permission to decrypt the data (created DynamoDB table is encrypted with a specific AWS KMS key).

**12) Waiting Period**
- The time between you scheduling the deletion of a key and the key actually getting deleted.
