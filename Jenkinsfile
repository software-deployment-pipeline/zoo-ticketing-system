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
                    powershell '''
                    docker run --rm -v /c/Users/LENOVO/AppData/Local/Jenkins/.jenkins/workspace/jenkins_pipeline:/app -w /app zoo-ticketing python -m unittest discover -s tests
                    '''
                }
            }
        }
    }

    post {
        always {
            // Archive test results if available
            junit '**/tests/*.xml' // Remove this if no XML reports are generated
        }
    }
}
