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
10. Enter below command in the terminal to download, extract and install `eksctl`:
    ```
    curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
	sudo mv -v /tmp/eksctl /usr/local/bin
    ```

11. After installation completed, enter `eksctl version` to validate the installation.
12. Navigate to AWS console, search for `IAM` and select **Roles** from the left navigation panel.
13. Click **Create role** and configure the following options:
    - **trusted entity type**: AWS service
    - **use case**: EC2

14. Click **Next** and select the `AdministratorAccess` permission policy.
15. Click **Next**.
16. Enter `my-eks-instance-role` for role name and provide the description.
17. Select **Create role**.
18. Head back to EC2 console and select **Instances** from the left panel.
19. Select the created instance, expand the **Actions** dropdown and select **Security**.
20. Click **Modify IAM role**.
21. Under **IAM role**, select the `my-eks-instance-role` and click **Update IAM role**.
22. Open the `eks-instance` terminal page and re-enter the command shown in `cluster_create-2.txt` again.
    > Make sure to replace the `<your-region-code>` with the current actual region
	
    > The EKS cluster set up should be successfully running in the terminal now

## Task 2: Pull the Code for your Backend
23. Head to EC2 console while waiting for the cluster creation.
24. Select the created instance `my-eks-instance-role` and click **Connect**.
25. Select **In web browser** tab and **EC2 instance connect**.
26. Click **Connect** and you should be connected to the EC2 instance using terminal.
27. Open the GitHub repository (https://github.com/nextwork-projects/nextwork-flask-backend.git) in a browser and select **Code**.
28. Copy the **HTTPS URL** and enter below command in the terminal
    ```
    git clone https://github.com/nextwork-projects/nextwork-flask-backend.git
    ```
	
29. Getting the `git command not found` error because git is not installed yet in the EC2.
30. Run below command to install git from the terminal:
    ```
    sudo dnf update
    sudo dnf install git -y
    ```

31. After installation complete, run `git --version` in the terminal to validate git installation.
32. To clone the repository, enter:
    ```
    run 'git clone https://github.com/nextwork-projects/nextwork-flask-backend.git'
    ```

## Task 3: Build a Container Image for Your Backend
33. From the same terminal, install **Docker** by entering `sudo yum install -y docker`.
34. Enter `sudo service docker start` to start docker.
35. Navigate to the folder directory that contains **Dockerfile** by using `cd` command.
36. Enter below command to build a container image:
    ```
    docker build -t nextwork-flask-backend .`

## Task 4: Push Your Container Image to Amazon ECR
37. Proceed to create new ECR repository by entering below command:
    ```
    aws ecr create-repository \
      --repository-name nextwork-flask-backend \
      --image-scanning-configuration scanOnPush=true \
    ```

38. In the new browser page, search for `ECR` in AWS console and open it.
    > The created repository should be visible as `nextwork-flask-backend`

39. Select the created repository and click **View push command**.
40. There should be a new small window pop up. Under the **macOS/Linux** tab, copy the first command and run it in EC2 Instance Connect window.
41. Copy the last 2 command (number 3 & 4) and run it in the EC2 Instance Connect window as well.
42. Close the **push command** window and select the created repository.
43. Check the **Images** tab and the container images should be visible there.

## Task 5: Delete Resources [Optional]

Delete EKS cluster

44. Delete the EKS cluster using EC2 Instance Connect by entering below command:
    ```
    eksctl delete cluster --name my-eks-cluster --region <region-name>
    ```

    > Replace `<region-name>` with the current actual region name

45. This delete the EKS cluster and all associated resources but it may takes a bit of time so proceed with the next steps to delete other resources.

Delete EC2 instance

46. Head to EC2 console and select the `eks-instance` that are manually created earlier.
47. Expand the **Instance state** dropdown and select **Terminate (delete) instance**.
48. Navigate to **Elastic IPs** from the left navigation panel.
49. Select the elastic IP address, expand **Actions** dropdown and select **Release elastic IP addresses**.

Delete ECR repository

50. Head to the ECR console and select the created repository.
51. Click **Delete** and confirm the deletion.
