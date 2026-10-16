pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { echo 'Fetching the code' }
        }
        stage('Test') {
            steps { sh 'echo "running tests"; exit 1' }
        }
        stage('Build') {
            steps { echo 'Building the app' }
        }
    }
}
