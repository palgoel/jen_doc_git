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
       try{
        bat 'behave'
        currentBuild.result = 'SUCCESS'
     }
     catch (e) {
        currentBuild.result = 'FAILURE'
     }
       echo "${currentBuild.result} is the result ${env.BUILD_URL}."
       bat '''dir>sample.txt
       echo "This is some text">sample.txt'''
   }
}
