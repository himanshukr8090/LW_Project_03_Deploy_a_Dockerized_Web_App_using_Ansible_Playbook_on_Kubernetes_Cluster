# 🚀 Project 3: Deploy a Dockerized Web App using Ansible on EKS ☁️🐳☸️

This project demonstrates how to deploy a **Dockerized Flask Web App** on an **Amazon EKS (Elastic Kubernetes Service)** cluster using **Ansible** for automation. The entire process was done manually, focusing on infrastructure understanding and automation with IaC tools.

---

## ✅ Steps I Followed:

## 1. 🐳 Created & Dockerized a Flask Web App
```bash
# Simple app.py with routes
# Dockerfile to containerize the app
docker build -t himanshu8090/flask-app .
docker push himanshu8090/flask-app
```

## 2. ☸️ Created a Kubernetes EKS Cluster (using `eksctl`)
```bash
eksctl create cluster --name flask-cluster --region ap-south-1 --node-type t3.medium --nodes 2 --managed
```

## 3. 🔄 Transferred `kubeconfig` to Ubuntu (Ansible Master Node)

### 📤 From Windows (Host Machine)
```bash
scp -i "LW-Projects.pem" "C:\Users\hp\.kube\config" ubuntu@<ansible-ec2-ip>:/home/ubuntu/config
```

### 📥 On Ubuntu (Ansible Master Node)
```bash
mkdir -p ~/.kube
mv ~/config ~/.kube/config
chmod 600 ~/.kube/config
export KUBECONFIG=~/.kube/config
```

## 4. ⚙️ Installed AWS CLI & kubectl on Ansible EC2
```bash
# Install kubectl
curl -LO https://dl.k8s.io/release/v1.30.1/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Configure AWS credentials
aws configure  # (Access Key, Secret Key, Region, Output Format)
```

## 5. 🧾 Wrote Kubernetes YAML Manifests

- **`deployment.yaml`** – Defines the Deployment of the Flask app.
- **`service.yaml`** – Exposes the app using a `LoadBalancer`.

## 6. 🤖 Wrote and Ran Ansible Playbook
```bash
ansible-playbook -i inventory.ini ansible-deploy-eks.yml
```

### 🧾 Playbook Tasks

- 📄 Copy manifest files (`deployment.yaml`, `service.yaml`)
- ☸️ Use `kubectl apply` to deploy them to the EKS cluster


## 7. 🌐 Accessed the Web App
```bash
kubectl get svc
# Retrieved LoadBalancer URL from flask-service
# Accessed app using external URL
```

## 🧰 Tech Stack
- **Flask** (Python)
- **Docker**
- **Ansible**
- **Kubernetes**
- **Amazon EKS**
- **AWS CLI**
- **eksctl**
- **Ubuntu EC2**

## 📌 Learning Highlights
- Manual EKS cluster setup & configuration  
- Docker image creation and push to Docker Hub  
- Real-world Ansible automation of Kubernetes tasks  
- AWS CLI & IAM integration with Kubernetes auth  
- Clean CI-free deployment to cloud

---

## 🔗 Connect
Feel free to connect with me on [LinkedIn](www.linkedin.com/in/himanshukrsingh0) or check out more on [Docker Hub](https://hub.docker.com/u/himanshu8090).

