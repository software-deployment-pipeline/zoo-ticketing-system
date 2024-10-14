pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/software-deployment-pipeline/zoo-ticketing-system', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    dockerImage = docker.build('zoo-ticketing')
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                script {
                    // Use Docker for Windows-style paths with correct format
                    dockerImage.inside("-v /c/Users/LENOVO/AppData/Local/Jenkins/.jenkins/workspace/jenkins_pipeline:/app -w /app") {
                        // Run pytest in the /app directory
                        sh 'pytest tests/test_sample.py'
                    }
                }
            }
        }
    }

    post {
        always {
            // Archive test results if available
            junit '**/tests/*.xml' // If you generate test result XMLs
        }
    }
}
