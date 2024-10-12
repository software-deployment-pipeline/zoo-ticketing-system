pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the GitHub repository
                git url: 'https://github.com/software-deployment-pipeline/zoo-ticketing-system.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Building the Docker image
                script {
                    dockerImage = docker.build("zoo-tiketing")
                }
            }
        }

        // stage('Run Tests') {
        //     steps {
        //         // Running tests inside the Docker container
        //         script {
        //             dockerImage.inside {
        //                 // Adjust the test directory path if necessary
        //                 sh 'python -m unittest discover -s tests'
        //             }
        //         }
        //     }
        // }

        // stage('Deploy to Production') {
        //     steps {
        //         // Pushing the Docker image to Docker Hub
        //         script {
        //             docker.withRegistry('https://registry.hub.docker.com', 'd600d408-6549-40bf-a256-c41d517d8121') {
        //                 dockerImage.push('miad560/zoo-tiketing')
        //             }
        //         }
        //     }
        // }
    }

    post {
        always {
            // Stopping and removing containers, then cleaning up the workspace
            script {
                dockerImage.inside {
                    sh 'docker stop $(docker ps -q --filter ancestor=zoo-tiketing) || true'
                    sh 'docker rm $(docker ps -a -q --filter ancestor=zoo-tiketing) || true'
                }
                cleanWs()
            }
        }
    }
}

