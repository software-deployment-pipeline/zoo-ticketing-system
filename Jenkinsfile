pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {

                // Cloning the GitHub repository
                git branch: 'development-felix',
                    credentialsId: 'github-ssh-key',
                    url: 'git@github.com:software-deployment-pipeline/zoo-ticketing-system.git'
               
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    dockerImage = docker.build("felixjoshua/zoo_ticketing")
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
                echo 'Merging into main..'
                script {
                    sh 'git config --global user.email "jenkins@test.com"'
                    sh 'git config --global user.name "Jenkins CI"'
                    sh 'git checkout main'
                    sh 'git merge origin/development-felix'                
                    sh 'git push origin main'
                }
                echo 'Code successfully merge..'
            }
        }

        stage('Push to Docker Hub') {
                steps {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                            dockerImage.push('latest')
                        }
                    }
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    // SSH into EC2 instance and deploy
                    sshagent(credentials: ['ec2-ssh-key']) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no ec2-user@3.106.213.115 << EOF
                                # Stop existing application
                                docker stop zoo-ticketing || true
                                docker rm zoo-ticketing || true

                                # Pull new Docker image
                                docker pull felixjoshua/zoo-ticketing:latest

                                # Run the new Docker image
                                docker run -d -p 80:8080 --name zoo-ticketing your-docker-repo/zoo-ticketing:latest

                                echo "Deployment completed"
                            EOF
                        '''
                    }
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
