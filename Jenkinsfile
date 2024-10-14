pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the GitHub repository
                git url: 'https://github.com/software-deployment-pipeline/zoo-ticketing-system', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building the application...'
                // Building a Docker image
                script {
                    dockerImage = docker.build("zoo-ticketing")
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running some tests...'
                // Uncomment the following lines if you have tests inside the container
                // Ensure you have Python and the right libraries installed in the Dockerfile
                script {
                    dockerImage.inside {
                        sh 'python3 -m unittest discover -s tests'
                    }
                }
            }
        }

        // Optional Deployment Stage
        // stage('Deploy to Production') {
        //     steps {
        //         echo 'Deploying to production...'
        //         script {
        //             docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
        //                 dockerImage.push('your-dockerhub-repo/your-image-name')
        //             }
        //         }
        //     }
        // }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Clean up workspace
            cleanWs()
        }
    }
}
