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
       echo "${env.BRANCH_NAME} is the branch name."
       echo "${env.JENKINS_HOME} is the Jenkins home name."
   }
}
