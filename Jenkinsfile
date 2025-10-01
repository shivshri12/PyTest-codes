pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/shivshri12/PyTest-codes.git'
            }
        }

        stage('Setup Python') {
            steps {
                // Activate venv (important step)
                bat '.venv//Scripts//activate'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest test_InstantIssue.py --alluredir=allure-results'
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    results: [[path: 'allure-results']],
                    reportBuildPolicy: 'ALWAYS',
                    tool: 'Allure'   // Jenkins me configured name
                ])
            }
        }
    }
}











