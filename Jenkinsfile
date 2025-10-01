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
                // Make sure Python is installed on Jenkins node
                bat 'cd /d C:\Users\shivendra.shrivastav\PycharmProjects\PythonProject'
                // Activate venv (important step)
                bat .venv\Scripts\activate
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest test_InstantIssue.py --alluredir=allure-results'
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}




