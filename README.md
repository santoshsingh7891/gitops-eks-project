# 🚀 AWS EKS GitOps Project with ArgoCD, Istio, Prometheus & Grafana

## 📌 Project Overview

This project demonstrates a Production-Grade GitOps CI/CD Platform on AWS using:

- AWS EKS
- Docker
- Kubernetes
- Helm
- ArgoCD
- GitHub Actions
- Istio
- Prometheus
- Grafana
- Amazon ECR

---

# 🏗️ Architecture Diagram

![Architecture](screenshots/architecture-diagram.png)

---

# ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| AWS EKS | Kubernetes Cluster |
| Docker | Containerization |
| Amazon ECR | Docker Registry |
| GitHub Actions | CI/CD Pipeline |
| ArgoCD | GitOps Deployment |
| Helm | Kubernetes Package Manager |
| Istio | Service Mesh |
| Prometheus | Monitoring |
| Grafana | Visualization |

---

# 📂 Project Structure

```bash
.
├── .github/workflows/
├── gitops-chart/
├── k8s/
├── screenshots/
├── Dockerfile
├── app.py
├── requirements.txt
└── README.md
```

---

# 🚀 CI/CD Workflow

1. Developer pushes code to GitHub
2. GitHub Actions builds Docker image
3. Docker image pushed to Amazon ECR
4. ArgoCD monitors Git repository
5. Kubernetes deployment updated automatically
6. Application deployed into EKS cluster

---

# 📸 Project Screenshots

## ArgoCD Dashboard

![ArgoCD](screenshots/argocd-dashboard.png)

---

## Grafana Dashboard

![Grafana](screenshots/grafana-dashboard.png)

---

## GitHub Actions Pipeline

![GitHub Actions](screenshots/github-actions-success.png)

---

## Running Application

![Application](screenshots/application-running.png)

---

## Amazon EKS Cluster

![EKS](screenshots/eks-cluster.png)

---

## Amazon ECR Docker Push

![ECR](screenshots/ecr-image-push.png)

---

# 📊 Monitoring Stack

## Prometheus
Collects Kubernetes and application metrics.

## Grafana
Visualizes:
- CPU usage
- Memory usage
- Pod metrics
- Cluster health

---

# 🌐 Istio Service Mesh

Istio provides:
- Traffic Management
- Security
- Observability
- Service Discovery

---

# 🔧 Deployment Commands

## Create EKS Cluster

```bash
eksctl create cluster \
--name gitops-cluster \
--region ap-south-1 \
--nodegroup-name workers \
--node-type t3.medium \
--nodes 2
```

---

## Install ArgoCD

```bash
kubectl create namespace argocd

kubectl apply -n argocd \
-f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

---

## Install Monitoring Stack

```bash
helm repo add prometheus-community \
https://prometheus-community.github.io/helm-charts

helm install monitoring \
prometheus-community/kube-prometheus-stack
```

---

# 📈 Auto Scaling

```bash
kubectl autoscale deployment gitops-app \
--cpu-percent=70 \
--min=2 \
--max=10
```

---

# ✅ Features

- GitOps-based deployment
- Automated CI/CD pipeline
- Kubernetes orchestration
- Docker containerization
- Helm package deployment
- Monitoring with Prometheus & Grafana
- Service mesh using Istio
- Horizontal Pod Autoscaling
- AWS ECR integration

---

# 👨‍💻 Author

Santosh Singh

GitHub:
https://github.com/santoshsingh7891
