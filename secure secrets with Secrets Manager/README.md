# Secure Secrets with Secrets Manager

## 📌 Overview

Modern applications rely on sensitive credentials, such as API keys, database passwords, and access tokens, to securely communicate with backend services

Hard-coding these secrets into application code can lead to serious security risks if the code is exposed, potentially allowing unauthorized access to critical systems and data,

This project demonstrates how to use AWS Secrets Manager to securely store, manage, and retrieve application secrets instead of embedding them directly in source code. 

By completing this project, we will learn secure credential management best practices and understand how production applications protect sensitive information when connecting to AWS services and databases.

---

The goals of this project are to:
- Identify how a web application can insecurely store sensitive credentials.
- Explore how GitHub Secret Scanning helps detect and prevent secrets from being committed to a repository.
- Update the web application to securely store and retrieve credentials using AWS Secrets Manager.
- Verify that the application's source code can be safely shared or made public without exposing sensitive credentials.

## 🛠️ Technologies & Tools

`AWS Secrets Manager` `AWS IAM` `Github`

## 🏗️ Architecture

```

                                                                                            [Secret]
                                                                                                
                                                                                                │
                                    Web App Code                                                │
                                    ─────────────────────────────────────────────────────────   │ ───────────────
                                   │                                                            ▼                │
        GitHub                     │                                                                             │
 [Original Repository]   ══════════════ ➤   [Cloned code]  ⟹  [Hardcode credentials]  ⟹  [Secure code]       │
                                   │                                                                             │
          │                        │                                 │                        │                  │
          │                        │                                 │                        │                  │
          │                        │                                 ▼                        ▼                  │
          │                        │                                                                             │
          │                        │                             [denied]                  [allowed]             │
          │                        │                                                                             │
          │                         ──────────────────────────────  │   ─────────────────────  │   ────────────── 
          │                                                         │                          │
          │                                                         │                          │
          │                                                         ─ ── ── ── ── ── ── ── ── ──
          │                                                                        │
          │                                                                        │
          │                                                                        │
          │                                                                        ▼
          │                                                                        
           ── ── ── ── ── ── ── ── ── ── ── ── ── ── ── ── ── ── ── ── ── ──    GitHub
                                                                               [Forked]


```

## ✏️ What I learned

### 🔑 Key Concepts

**1) AWS Secrets Manager**
- A service that helps you securely store, retrieve and audit sensitive information like passwords, API keys and credentials.

**2) AWS IAM**
- A service that helps you securely control access to AWS resources.

**3 GitHub**
- A platform where developers share and collaborate on code.

**4 AWS Key Management Service (KMS)**
- A managed service that lets you create and control the cryptographic keys used to protect your data.

---

### 🔍 Additional Notes

**5) `app.py`**
- A main file containing the logic of the web app (how the app will respond to user request & interact with AWS services).

**6) How is `app.py` built?**
- Built using FastAPI, a web framework for building APIs with Python.

**7) Import Statements**
- A command used to reuse code from external files, libraries, or modules.

**8) `config.py`**
- A file that contains the configuration settings for the web app.

**9) Dockerfile**
- A plain-text script containing ordered instructions used to automate the creation of a Docker image.

**10) `requirements.txt`**
- A list of python libraries required by the app to run.

**11) Forking in GitHub**
- Making a personal copy of an existing repository, and editing and storing that copy in your own GitHub account.

**12) Forking vs Cloning in GitHub**

| Forking | Cloning |
|---|---|
| Creates a copy of the repository on your GitHub account (cloud) | Cloning downloads a copy of the repository to your local computer |

**13) Why running the app in virtual environment?**
- It keeps all the packages we need to run this web app.
- When it is deleted, all packages installed are removed too (computer clean of unused packages).

**14) Secret Rotation**
- Process of automatically changing your secrets on a regular schedule (best for high-risk credentials like database passwords, privileged API keys, and service account credentials).

**15) What does the new code in `config.py` do with the retrieved secret?**-
- Code are added in the `config.py` to extract the values of the secret that we stored in Secrets Manager.
- It uses the function suggested by the code sample and splits up the secret value to store the access key ID & secret access key in the same variable that `app.py` continue to use.

**16) Merge conflicts**
- Happen when the same line of code has been changed in different commit
