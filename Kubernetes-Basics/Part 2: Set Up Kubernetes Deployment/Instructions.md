# 📜 Instructions

## Task 1: Set up EC2 and EKS [Optional - Only do these steps if the previous resources are deleted]
1. Log in to the **AWS console** as IAM admin user.
2. Search for `EC2` in the AWS console and open it.
3. Select **Instance** from the left navigation panel and click **Launch instance**.
4. Configure the instance based on below options:
   - **name**: `eks-instance`
   - **OS image**: `Amazon Linux 2023 kernel-6.18 AMI`
   - **instance type**: `t3.micro`
   - **key pair login**: `proceed without key pair`

5. Keep the default settings for **Networking** and **Storage** section.
6. Click **Launch instances** and select the created instance.
7. Click **Connect**.
8. Select **In web browser** tab and **EC2 instance connect**.
9. Click **Connect** and you should be connected to the EC2 instance using terminal.
10. Navigate to AWS console, search for `IAM` and select **Roles** from the left navigation panel.
11. Click **Create role** and configure the following options:
    - **trusted entity type**: AWS service
    - **use case**: EC2

12. Click **Next** and select the `AdministratorAccess` permission policy.
13. Click **Next**.
14. Enter `my-eks-instance-role` for role name and provide the description.
15. Select **Create role**.
16. Head back to EC2 console and select **Instances** from the left panel.
17. Select the created instance, expand the **Actions** dropdown and select **Security**.
18. Click **Modify IAM role**.
19. Under **IAM role**, select the `my-eks-instance-role` and click **Update IAM role**.
20. Open the `eks-instance` terminal page and enter the command shown in `cluster_create-2.txt`.
    > The EKS cluster set up should be successfully running in the terminal now

## Task 2: Pull the Code for your Backend
21. Head to EC2 console while waiting for the cluster creation.
22. Select the created instance `my-eks-instance-role` and click **Connect**.
23. Select **In web browser** tab and **EC2 instance connect**.
24. Click **Connect** and you should be connected to the EC2 instance using terminal.
25. Open the GitHub repository (https://github.com/nextwork-projects/nextwork-flask-backend.git) in a browser and select **Code**.
26. Copy the **HTTPS URL** and enter below command in the terminal
    ```
    git clone https://github.com/nextwork-projects/nextwork-flask-backend.git
    ```
	
27. Getting the `git command not found` error because git is not installed yet in the EC2.
28. Run below command to install git from the terminal:
    ```
    sudo dnf update
    sudo dnf install git -y
    ```

29. After installation complete, run `git --version` in the terminal to validate git installation.
30. To clone the repository, enter:
    ```
    run 'git clone https://github.com/nextwork-projects/nextwork-flask-backend.git'
    ```

## Task 3: Build a Container Image for Your Backend
31. From the same terminal, install **Docker** by entering `sudo yum install -y docker`.
32. Enter `sudo service docker start` to start docker.
33. Navigate to the folder directory that contains **Dockerfile** by using `cd` command.
34. Enter below command to build a container image:
    ```
    docker build -t nextwork-flask-backend .`

## Task 4: Push Your Container Image to Amazon ECR
35. Proceed to create new ECR repository by entering below command:
    ```
    aws ecr create-repository \
      --repository-name nextwork-flask-backend \
      --image-scanning-configuration scanOnPush=true \
    ```

36. In the new browser page, search for `ECR` in AWS console and open it.
    > The created repository should be visible as `nextwork-flask-backend`

37. Select the created repository and click **View push command**.
38. There should be a new small window pop up. Under the **macOS/Linux** tab, copy the first command and run it in EC2 Instance Connect window.
39. Copy the last 2 command (number 3 & 4) and run it in the EC2 Instance Connect window as well.
40. Close the **push command** window and select the created repository.
41. Check the **Images** tab and the container images should be visible there.

## Task 5: Delete Resources [Optional]

Delete EKS cluster

42. Delete the EKS cluster using EC2 Instance Connect by entering below command:
    ```
    eksctl delete cluster --name my-eks-cluster --region <region-name>
    ```

    > Replace `<region-name>` with the current actual region name

43. This delete the EKS cluster and all associated resources but it may takes a bit of time so proceed with the next steps to delete other resources.

Delete EC2 instance

44. Head to EC2 console and select the `eks-instance` that are manually created earlier.
45. Expand the **Instance state** dropdown and select **Terminate (delete) instance**.
46. Navigate to **Elastic IPs** from the left navigation panel.
47. Select the elastic IP address, expand **Actions** dropdown and select **Release elastic IP addresses**.

Delete ECR repository

48. Head to the ECR console and select the created repository.
49. Click **Delete** and confirm the deletion.
