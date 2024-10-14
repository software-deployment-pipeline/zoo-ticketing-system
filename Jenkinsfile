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
