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
                    // Use the jenkins pipeline@tmp directory for mounting
                    dockerImage.inside('-v /c/Users/LENOVO/AppData/Local/Jenkins/.jenkins/workspace/jenkins pipeline@tmp:/workspace') {
                        // Adjust command for Windows
                        bat 'python -m unittest discover -s tests'
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
            cleanWs()
        }
    }
}
