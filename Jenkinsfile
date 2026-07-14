pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sarthakrajput19/payment.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
    }
}
