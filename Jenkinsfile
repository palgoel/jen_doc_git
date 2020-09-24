#!groovy
node {
    stage('Checkout') {
        checkout scm
    }	
    stage('Build') {
        bat 'pip install -r requirements.txt' 
    }	
   stage('Test') {
        bat 'behave' 
    }	
}
