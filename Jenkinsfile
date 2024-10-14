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
                echo 'Running unit tests...'
                script {
                    // Mount workspace to container using Docker on Windows
                    dockerImage.inside("-v /c/Users/LENOVO/Jenkins:/workspace") {
                        // Use 'bat' if this is a Windows-based container; otherwise 'sh' for Linux
                        bat 'cd /workspace && python -m unittest discover -s tests'
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                script {
                    dockerImage.run('-d -p 8081:8080')
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs() // Optional, remove if you want to keep the workspace for future reference
        }
    }
}
