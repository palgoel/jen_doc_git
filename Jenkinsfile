#!groovy
node {
    stage('Checkout') {
        checkout scm
    }	
    stage('Build') {
        bat '''pip install -r requirements.txt' 
		behave''' 
        archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true 
    }	
}
