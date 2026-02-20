pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/AdieeeP/studentportal.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Migrations') {
            steps {
                bat 'venv\\Scripts\\python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                set DJANGO_SETTINGS_MODULE=StudentPortal.settings
                venv\\Scripts\\python manage.py test
                '''
            }
        }
    }
}