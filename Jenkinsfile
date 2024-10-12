pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the GitHub repository
                git url: 'https://github.com/your-username/your-repo-name.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Building a Docker image
                script {
                    dockerImage = docker.build("your-image-name")
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Running tests inside the Docker container
                script {
                    dockerImage.inside {
                        sh 'python -m unittest discover -s tests'
                    }
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                // Deploying the Docker container to a production server
                script {
                    dockerImage.push('your-dockerhub-repo/your-image-name')
                }
            }
        }
    }

    post {
        always {
            // Clean up after build
            cleanWs()
        }
    }
}
