pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Add GitHub's SSH key to known_hosts
                sh 'ssh-keyscan github.com >> ~/.ssh/known_hosts'
                // Cloning the GitHub repository
                
                git branch: 'development-felix', url: 'git@github.com:software-deployment-pipeline/zoo-ticketing-system.git'

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
                    dockerImage.inside {
                        sh 'python -m unittest discover -s tests/integration'  // Run integration tests
                    }
                }
            }
        }

        stage('Merge into main') {
            steps {
                echo 'Merging into main...'
                script {
                    sh 'git config --global user.email "jenkins@example.com"'
                    sh 'git config --global user.name "Jenkins CI"'
                    sh 'git checkout main'
                    sh 'git merge origin/development-felix'                
                    sh 'git push origin main'
                    
                }
            }
        }

        // push to main branch?

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
