# 📜 Instructions

## Task 1: Set Up Your App for Deployment
1. Run the following command to create a new directory from the instance root called `manifests`:
   ```
   cd ..
   mkdir manifests
   cd manifests
   ```

2. Create a file named `flask-deployment.yaml` by entering below command from the terminal:
   ```
   touch flask-deployment.yaml
   ```
  
3. Open the `flask-deployment.yaml` with any text editor and paste the command shown in `flask-deployment.txt`.
   > make sure to replace `<your-ecr-image-url>` with URL of the docker image you have pushed to ECR
 
4. To get the ECR URL, navigate to below path from the ECR console:
   > you can get the ECR URL by navigating to the ECR console → private registry → repositories → created repositories → pushed image

5. Exit the editor and save the changes.

## Task 2: Create your Service Manifest
6. Create another file named `flask-service.yaml` by entering below command from the terminal:
   ```
   touch flask-service.yaml
   ```

8. Open the `flask-service.yaml` with any text editor and paste the command shown in `flask-service.txt`.
9. Exit the editor and save the changes.

## Task 3: Delete Resources [Optional]

Delete EKS cluster

9. Delete the EKS cluster using EC2 Instance Connect by entering below command:
    ```
    eksctl delete cluster --name my-eks-cluster --region <region-name>
    ```

    > Replace `<region-name>` with the current actual region name

10. This delete the EKS cluster and all associated resources but it may takes a bit of time so proceed with the next steps to delete other resources.

Delete EC2 instance

11. Head to EC2 console and select the `eks-instance` that are manually created earlier.
12. Expand the **Instance state** dropdown and select **Terminate (delete) instance**.
13. Navigate to **Elastic IPs** from the left navigation panel.
14. Select the elastic IP address, expand **Actions** dropdown and select **Release elastic IP addresses**.

Delete ECR repository

15. Head to the ECR console and select the created repository.
16. Click **Delete** and confirm the deletion.
