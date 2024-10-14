pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the GitHub repository
                git url: 'https://github.com/software-deployment-pipeline/zoo-ticketing-system', branch: 'development-felix'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building the application...'
                // Building a Docker image
                script {
                    dockerImage = docker.build("zoo_ticketing")
                }
            }
        }

         stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                script {
                    dockerImage.inside {
                        sh 'python -m unittest discover -s tests/unit'
                    }
                }
            }
        }

        stage('Run Integration Tests') {
            steps {
                echo 'Running integration tests...'
                script {
                        sh 'python zoo-ticketing.py > output.txt'  // Run the console app and save output
                        sh 'python -m unittest discover -s tests/integration'  // Run integration tests
                }
            }
        }

        // stage('Deploy to Production') {
        //     steps {
        //         // Deploying the Docker container to a production server
        //         script {
        //             dockerImage.push('your-dockerhub-repo/your-image-name')
        //         }
        //     }
        // }
    }

    post {
        always {
            // Clean up after build
            cleanWs()
        }
    }
}
