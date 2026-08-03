# 📜 Instructions

## Task 1: Install Terraform
1. Navigate to Terraform download page `https://developer.hashicorp.com/terraform/install` and download the package.
2. Unzip the package in local computer **Downloads** folder and copy the Terraform binary (.exe file).
3. Open C drive via File Explorer and navigate to `C:\Program Files` folder.
4. Create a new folder named `Terraform`, navigate to the created folder and paste the Terraform binary file.
5. Copy the current directory folder path `C:\Program Files\Terraform`.
6. Search for `Edit the system environment variables` in the windows search bar.
7. Navigate to **Environment Variables** and select **Path** from the system variables list.
8. Click **Edit** and select **New**.
9. Paste the folder path earlier and click **OK** for all the shown properties window.
10. Open the terminal and enter 'terraform version' to validate Terraform installation.

## Task 2: Set up Terraform project
11. From the terminal, navigate to Desktop folder and enter `mkdir Terraform_Projects` to create a directory.
12. Navigate to the created directory and create a new file by entering `mkdir main.tf`.
13. As alternative, these steps can also be done using **File Explorer**.

## Task 3: Define main.tf
14. Open the created `main.tf` earlier with a text or code editor (using `vim` / `nano` or using Notepad / VS Code) and enter the code shown in `terraform_setup.txt`.
    > replace `your-region-code` with the actual region and adjust the bucket name to make it unique

15. Save the changes.
16. To further customize the configuration, include the tags for S3 bucket (refer Terraform registry documentation).

## Task 4: Run Terraform configuration
17. In the terminal, enter `terraform init` to set up the backend.
18. Enter `terraform plan` to create the execution plan.
19. Receives an error **No valid credentials sources found** because both Terraform and terminal does not have the credential access to AWS account yet.

## Task 5: Set up AWS Credentials
20. Install AWS CLI in the terminal by entering below command:
    ```
    Invoke-WebRequest -Uri "https://awscli.amazonaws.com/AWSCLIV2.msi" -OutFile "AWSCLIV2.msi"
    Start-Process msiexec.exe -ArgumentList "/i AWSCLIV2.msi" -Wait
    ```

21. Once AWS CLI installation completed, reopen a new terminal page and enter `aws --version` to validate the AWS CLI installation.
22. Log in to the AWS Management Console as the IAM Admin user.
23. Enter `IAM` in the search bar and open it.
24. Select **IAM users** from the left navigation panel and select **Users**.
25. Navigate to **Security Credentials** tab and click **Create access keys**.
26. Select **Command Line Interface (CLI)** for use case and tick the confirmation acknowledgement below.
27. Click **Next** and enter the description and click **Create access keys**.
28. Head back to the terminal window and enter `aws configure`. 
29. Enter the **AWS Access Key ID** & **AWS Secret Access Key** value from your **access keys** page in IAM console
30. Fill in your region and enter `json` for output format.
31. Still in the Terraform folder directory, enter `terraform init` and `terraform plan` again.

## Task 6: Launch an S3 Bucket with Terraform
32. In the terminal, enter `terraform apply` and `yes` to apply the changes.
33. If there is an error received regarding the bucket name, edit the bucket name in the `main.tf` file and save the changes.
34. Run `terraform plan`, `terraform apply` and `yes` to proceed.
35. To validate whether the bucket creation is successful, search for `S3` in AWS console and open it.
36. The newly created bucket should be visible under **General purpose bucket** section.

## Task 7: Upload an S3 object with Terraform [Optional]
37. Download or use any existing image on the computer and renamed it as `images.png`.
38. Moved the `images.png` to the `Terraform_Projects` folder.
39. Edit the `main.tf` file and enter below block of code:
    ```
    resource "aws_s3_object" "image" {
		  bucket = aws_s3_bucket.my_bucket.id # reference the bucket ID
		  key = "images.png" # path in the bucket
		  source = "images.png" # local file path (rename if images are in different folder path)
    }
    ```

40. Head back to the terminal window, enter `terraform plan`, `terraform apply` and `yes` to proceed with the changes.
41. The `images.png` file should be visible now in the S3 console as S3 bucket objects.

## Task 8: Delete Resources

Delete S3 bucket

42. To delete the resources, enter `terraform destroy` in the terminal window.
43. Enter `yes` to proceed.
44. Navigate to S3 console to validate the resource deletion.

Delete IAM access keys

45. Head back to IAM console, select `IAM users` from the left navigation panel and select **Users**.
46. Navigate to **Security Credentials** tab and expand the **Actions** dropdown under access keys section.
47. Click **Delete**, **Deactivate** and confirm the deletion.
48. Delete the downloaded credentials `.csv` file from the computer as well (if you downloaded the file in step 27).
