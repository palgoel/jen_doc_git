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
   stage('Deploy') {
       echo "${currentBuild.result} is the result ${env.BUILD_URL}."
   }
}
