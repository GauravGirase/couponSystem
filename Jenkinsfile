pipeline {
  agent any
  stages{
      stage ("Hello"){
        steps{
          println "Branch Name: " + env.BRANCH_NAME
          println "Change ID: " + env.CHANGE_ID
          println "GITHUB_PAYLOAD: " + env.GITHUB_PAYLOAD
          println "Pull request: " + pullRequest.addLabel("Build Failed")
          println "Hello World"
        }         
      }
  }
}
