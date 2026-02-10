# Java AIOPS CI/CD Project

This project integrates a Java application with AI-driven code review and deployment risk assessment, containerized with Docker, infrastructure as code with Terraform, and deployment with Helm and Jenkins CI/CD.

## Structure

- app/: Java Maven application
- aiops/: Python scripts for AI logic
- docker/: Dockerfile for containerization
- terraform/: Infrastructure as code
- helm/: Kubernetes Helm chart
- Jenkinsfile: CI/CD pipeline

## Getting Started

1. Build the Java app: `cd app && mvn clean package`
2. Run AI scripts: `python aiops/code_review.py`
3. Build Docker image: `docker build -f docker/Dockerfile -t myapp .`
4. Deploy with Terraform: `cd terraform && terraform apply`
5. Deploy with Helm: `cd helm && helm install java-aiops .`