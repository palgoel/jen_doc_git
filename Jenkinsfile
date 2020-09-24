#!groovy
node {
    stage('Build') {
        bat '''pip install -r requirement.txt' 
		behave''' 
        archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true 
    }
}
