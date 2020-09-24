#!groovy
node {
    stage('Build') {
        bat '''pip install -r requirements.txt' 
		behave''' 
        archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true 
    }
}
