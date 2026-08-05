# 📜 Instructions

## Task 1: Launch and connect to an EC2 instance
1. Log in to the **AWS console** as IAM admin user.
2. Search for `EC2` in the AWS console and open it.
3. Select **Instance from the left navigation panel and click **Launch instances**.
4. Configure the instance based on below options:
   - **name**: `eks-instance`
   - **OS image**: `Amazon Linux 2023 kernel-6.18 AMI`
   - **instance type**: `t3.micro`
   - **key pair login**: `proceed without key pair`

5. Keep the default settings for **Networking** and **Storage** section.
6. Click **Launch instances** and select the created instance.
7. Click **Connect**.
8. Select **In web browser** tab and **EC2 instance connect**
9. Click **Connect** and you should be connected to the EC2 instance using terminal.

## Task 2: Launch an EKS cluster (and get an error)
10. In the `eks-instance` terminal, enter the command shown in `cluster_create.txt`.
11. Getting an error `eksctl: command not found` because eksctl has not been installed yet.
12. Run below command in the terminal to install eksctl:
    ```
    curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
    sudo mv -v /tmp/eksctl /usr/local/bin
    ```

13. After installation completed, enter `eksctl version` to validate the installation.

## Task 3: Launch an EKS cluster (for real this time)
14. Enter the command shown in `cluster_create-2.txt` and replace the `<your-region-code>` with the current actual region.
15. Getting `checking AWS STS access` error because the EC2 instance doesn't have the permission to create EKS cluster yet (need IAM role).
16. Navigate to AWS console, search for `IAM` and select **Roles** from the left navigation panel.
17. Click **Create role** and configure the following options:
    - **trusted entity type**: AWS service
    - **use case**: EC2

18. Click **Next** and select the `AdministratorAccess` permission policy.
19. Click **Next**.
20. Enter `my-eks-instance-role` for role name and provide the description.
21. Select **Create role**.
22. Head back to EC2 console and select **Instances** from the left panel.
23. Select the created instance, expand the **Actions** dropdown and select **Security**.
24. Click **Modify IAM role**.
25. Under **IAM role**, select the `my-eks-instance-role` and click **Update IAM role**.
26. Open the `eks-instance` terminal page and re-enter the command shown in `cluster_create-2.txt` again.
    > Make sure to replace the `<your-region-code>` with the current actual region
    
    > The EKS cluster set up should be successfully running in the terminal now

## Task 4: Track how AWS creates your EKS cluster
27. To track cluster creation, head to `CloudFormation` console.
28. In the **Stacks** page, select the created stacks and select **Events** tab.
    > It shows the timeline of each action CloudFormation is taking to set up the resources
    
29. Select the **Resources** tab to view the list of created resources.
30. A new stack should also be visible (around 10-12 minutes after running the `create cluster` command) which is created specifically for the node group.
    > EKS cluster and node group stack are separated to manage/troubleshoot easier
    
31. Wait for the first cluster status shows **CREATE_COMPLETE**.
    > We can proceed with the next step without waiting for the second stack creation to complete

## Task 5: Access EKS from the Management Console
32. Search for `EKS` in AWS console and open it.
33. Select the created cluster and navigate to **Compute** tab.
    > Notice that the node groups are created in the **Node groups** panel
    
34. In the cluster details page, there is a blue banner saying `Your current IAM principal doesn’t have access to Kubernetes objects on this cluster`.
    > Even with `AdministratorAccess` role assigned, Kubernetes has its own way of managing access within a cluster
    
35. Navigate back to **Clusters**, select the **Access** tab and select **Create** in IAM **Access entries**.
36. Retrieve the IAM principal ARN by navigating to below path:
    > IAM → IAM users → IAM admin user

37. Once the IAM principal ARN are copied, paste the IAM principal ARN and select **Standard** for type.
38. Click **Next**.
39. Click **Add policy** and enter `AmazonEKSClusterAdminPolicy` for the policy name.
40. Keep the default options for **Access scope**.
41. Click **Next** and **Create**.
42. From the clusters page, there should be a **3 nodes** visible now in **Compute** tab.

## Task 6: Delete nodes (and watch them regenerate) [Optional]
43. Head back to EC2 console and notice that there are **3 new EC2** listed which is a part of the EKS cluster node group.
44. For testing purpose, select all 3 nodes.
45. Expand the **Instance state** dropdown and select **Terminate (delete instance)**.
46. Confirm the deletion by clicking **Terminate (delete)**.
47. In EKS console under **Nodes** from the **Compute** section, notice that all 3 nodes are not visible anymore.
48. After a few minutes, notice that the nodes are automatically generate back.
49. Navigate back to the EC2 console and noticed 3 new EC2 instance are automatically created as well.

## Task 7: Delete Resources [Optional]

Delete EKS cluster

50. Head to CloudFormation console, select the first stack from the list and click **Delete stack**.
51. Click **Edit termination protection**, select **Deactivated** and click **Save**.
52. Click **Delete stack** and confirm the deletion.
53. Select the second stack and follow the same step to delete it.
54. Make sure the stack status shows **DELETE_COMPLETE** before starting with the next steps.

Terminate EC2 instance

55. Head to EC2 console and select the `eks-instance` that are manually created earlier.
56. Expand the **Instance state** dropdown and select **Terminate (delete) instance**.
57. Navigate to **Elastic IPs** from the left navigation panel.
58. Select the elastic IP address, expand **Actions** dropdown and select **Release elastic IP addresses**.
