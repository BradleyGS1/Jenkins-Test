pipeline {
    agent { label 'agent1' }

    stages {
        stage('Set Up Python') {
            steps {
                // Install Python packages using pip
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Lint Code') {
            steps {
                // Lint the code using flake8
                sh './venv/bin/pip install flake8'
                sh './venv/bin/flake8 src/'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh './venv/bin/pip install pytest'
                sh './venv/bin/pytest tests/'
            }
        }

        stage('Clean Up') {
            steps {
                // Clean up environment
                sh 'rm -rf venv'
            }
        }
    }
}
