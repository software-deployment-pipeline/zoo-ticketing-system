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
                    dockerImage = docker.build('zoo-ticketing')
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                script {
                    dockerImage.inside {
                        // Run the tests in the 'tests' folder
                        sh 'pytest tests/test_sample.py'
                    }
                }
            }
        }
    }

    post {
        always {
            // Archive test results or any other necessary cleanup
            junit '**/tests/*.xml' // Comment out if you don't generate XML reports
        }
    }
}
