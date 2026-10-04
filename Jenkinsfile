pipeline {
    agent any

    environment {
        PY = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install') {
            steps {
                bat '"%PY%" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                bat 'venv\\Scripts\\activate && flake8 app.py --max-line-length=100'
            }
        }
        stage('Test') {
            steps {
                bat 'venv\\Scripts\\activate && pytest -v'
            }
        }
    }

    post {
        success { echo 'Pipeline succeeded!' }
        failure { echo 'Pipeline failed.' }
    }
}