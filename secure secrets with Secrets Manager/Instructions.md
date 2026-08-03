# 📜 Instructions

## Task 1: Examine and Set Up the Code
1. Open a browser page and navigate to the GitHub repository (https://github.com/NatNextWork1/nextwork-security-secretsmanager).
2. Select `app.py` and find the lines that start with `import`. These lines are **import statements**.
   > `read_index` function defines what happen when you visit the web app main page
   
   > `list_s3_buckets` is responsible for retrieving and displaying S3 buckets. It uses `config.AWS_ACCESS_KEY_ID`, `config.AWS_SECRET_ACCESS_KEY` and `config.AWS_REGION` to connect to AWS
   
   > exposing the credentials publicly is a major security risk since anyone who gets the credentials can access your AWS account

3. Open Command Prompt and navigate to Documents folder by entering `cd Documents`.
4. Clone the GitHub repository by entering `git clone [HTTPS-URL]`.
   > replace the [HTTPS-URL] with the GitHub repository URL 

5. Open `config.py` with a text editor and replace the placeholder value with below dummy credentials:
   ```
   AWS_ACCESS_KEY_ID = "AKIAW3MEFRAFTQM5FHKE"
   AWS_SECRET_ACCESS_KEY = "F0b8s5m+pOZsttvBCirr1BOutuvCpqXMW2Y1qAxY"
   AWS_REGION = "us-east-2"
   ```
   
6. Save the changes.

## Task 2: Run the Web App with your own AWS Credentials [Optional]
7. Still in the Documents folder directory from the terminal, enter `python -m venv venv` to create a new virtual environment.
8. Activate the virtual environment by entering `venv\Scripts\activate`.
9. Enter `python app.py` to run the app file but getting an error for boto3 and fastapi module.
10. Install those 2 packages or install all required packages listed in `requirement.txt` simultaneously by entering `pip install -r requirements.txt` in the terminal.
11. Run the app again by entering `python app.py` then copy the shown URL into the browser page.
12. In the web app page, click **View my S3 buckets** to retrieve S3 buckets list but getting an error saying AWS Access Key ID does not exist.
    > This because the hard-coded credentials earlier are a fake one for testing

13. In the new browser page, log in to the AWS Management Console as the IAM Admin user.
14. If there are no existing S3 bucket created, head to **S3** console to create a new bucket.
15. Once S3 bucket creation is completed, search for `IAM` in the AWS console and open it/
16. Select **IAM users** from the left navigation panel and select the **Users**.
17. Navigate to **Security Credentials** tab and click **create access key**.
18. Select **local code** for use case and tick the confirmation acknowledgement.
19. Click **Next**, fill in description field and click **create access key**.
20. Head back to terminal window, stop the running app by pressing `Ctrl` and `C` key.
21. Replace the **Access Key ID** and **Secret Key** shown in `config.py` file with the newly created access key value and save the changes.
22. Run the app again by entering `python app.py` in the terminal window.
23. Click **View my S3 buckets** from the web app page and it should be listing any existing S3 buckets under AWS account.
   
## Task 3: Make Your Code Public
24. Fork the GitHub repository `https://github.com/NatNextWork1/nextwork-security-secretsmanager` to your GitHub.
25. Connect local repository (click `edited code`) to the forked repository on GitHub by running `git remote add origin <your-forked-repo-url>`.
    > make sure to replace the `<your-forked-repo-url>` with the actual GitHub repository URL
    
26. Getting a **remote origin already exists** error because Git automatically set up a remote named `origin` to point to the original repository when cloning it earlier.
27. Enter `git remote set-url origin <your-forked-repo-url>` to change existing remote `origin` to the new forked repository.
28. Enter `git remote -v` to verify the remote origin set up.
29. Stage all the changes by entering `git add .`.
30. Commit the changes by entering `git commit -m "Updated config.py with hardcoded credentials"`.
31. Push the local commit to the forked repository by entering `git push -u origin main`.
32. Commit succeeded but GitHub sends a notification email regarding the uploaded secrets (secret scanning not fully covered for personal GitHub account).
    > Secrets Manager can be used to manage secrets securely and retrieve them from the app without hardcoding directly in `config.py` file

## Task 4: Create Secret in Secrets Manager
33. Search for `Secrets Manager` in the AWS console and open it.
34. Select **Secrets** from the left navigation panel and select **Store a new secret**.
35. Select **Other type of secret** for secret type and enter `AWS_ACCESS_KEY_ID` in the key field.
36. Click **Add row** and enter `AWS_SECRET_ACCESS_KEY` in the new key field.
37. Enter the value for both key field (refer `config.py` file) and click **Next**.
38. Enter `aws-access-key` for secret name and `Created to replace hard-coded access key credentials in config.py` for the description.
39. Skip the **Tags - optional**, **Resource permissions - optional**, **Replicate secret - optional** and **Configure rotation** section.
40. Click **Next** and **Store**.

## Task 5: Update config.py
41. From the **created secret banner**, click **see sample code** and navigate to `python3` under **caching clients** tab.
42. Copy the shown line of code from line 6 onward.
43. Open `config.py` file using code editor and paste the copied line of code earlier.
44. Add the block of code shown in `get_secret.py` to the `config.py` as well.
45. Enter `import json` under the `import botocore.session` line of code and click **Save**.

## Task 6: Push Changes
46. In the terminal window, enter `git add .` to save all the changes.
47. Enter `git commit -m "Updated config.py with Secrets Manager credentials"` to save the snapshot of the changes.
48. Enter `git push -u origin main` to push the local commit to the forked repository.
49. Push succeeded but noticed that the hardcoded access key from step 5 is still exist in the **commit history**.
50. To remove this commit history, get the commit ID and enter `git rebase -i --root`.
51. Look for the list of commit ID in the list, navigate to the commit line (before the `pick` command) and press `D` key to drop the commit.
52. Enter `:wq` to close the editor but getting a merge conflicts.
53. To solve the merge conflicts, open the `config.py` again using the code editor.
    > `<<<<<<< HEAD` marks the beginning of your current version
    
    > `=======` separates the 2 conflicting versions
    
    > `>>>>>>> feature-branch` marks the end of the incoming changes

54. Delete the command below and save the changes.
    > the entire code between `<<<<<<< HEAD` and `=======`
    
    > the `=======` marker
    
    > the entire `>>>>>>> feature-branch` line

55. Enter below command in the terminal:
    ```
    git add config.py
    git commit -m "Resolved merge conflicts"
    ```

56. Enter `git rebase --continue` and `git push -f origin main` to push the changes.
57. Head back to the `config.py` file in the repository and it should be showing a clean line of code without any hardcoded credentials.

## Task 7: Delete Resources

Delete the forked GitHub repository

58. Go to the forked repository and click **Settings**.
59. Scroll below and click **delete this repository** and confirm the deletion.

Delete the Secrets Manager secret.

60. Navigate to Secrets Manager console and click **Secrets** from the left navigation panel.
61. Select the created secret, expand the **Actions** dropdown and select `delete secret`.
62. Enter `7` days for waiting period and click `schedule deletion`.
63. Navigate to IAM console & select **IAM users** from the left navigation panel.
64. Look for the **access key** section, expand the **Actions** dropdown & click **delete**.
65. Proceed to **deactivate** the key and click **delete** to confirm deletion.

Delete the local repository.

66. In the terminal, enter `deactivate` to exit the virtual environment (for optional Task 2).
67. Enter `cd ..` to navigate to the parent folder.
68. Enter `rmdir /s /q <folder_path>` to delete the repository.
    > `<folder_path>` refers to the folder path in which you store the local repository
