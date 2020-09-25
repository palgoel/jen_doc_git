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
       if (currentBuild.result == null || currentBuild.result == 'SUCCESS') { 
            bat 'echo "This works Fine"'
        }
   }
}
