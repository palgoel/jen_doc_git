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
        bat '''if %currentBuild.result% == null OR %currentBuild.result% == SUCCESS echo "The build passed"
     '''
   }
}
