pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/newdelthis/ml-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Test Model') {
            steps {
                sh 'python test.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'model.pkl', fingerprint: true
            }
        }
    }
}
