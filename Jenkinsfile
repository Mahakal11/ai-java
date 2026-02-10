pipeline {
  agent any

  environment {
    AWS_DEFAULT_REGION = "ap-south-1"
    IMAGE = "java-aiops:${BUILD_NUMBER}"
  }

  stages {

    stage('Checkout') {
      steps { checkout scm }
    }

    stage('AI Code Review') {
      steps {
        sh 'python3 aiops/code_review.py'
      }
    }

    stage('Build') {
      steps {
        sh 'cd app && mvn clean package'
      }
    }

    stage('Docker Build') {
      steps {
        sh '''
          docker build -t $IMAGE -f docker/Dockerfile .
        '''
      }
    }

    stage('AI Deployment Risk') {
      steps {
        sh 'python3 aiops/deploy_risk.py'
      }
    }

    stage('Deploy to EKS') {
      steps {
        sh '''
          helm upgrade --install java-aiops helm \
          --set image=$IMAGE
        '''
      }
    }
  }
}
