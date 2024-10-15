pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/software-deployment-pipeline/zoo-ticketing-system', branch: 'test-axel'
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
}
