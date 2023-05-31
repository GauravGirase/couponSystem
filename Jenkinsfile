pipeline {
  agent any
  stages{
      stage ("Hello"){
        steps{
          println "Branch Name: " + env.BRANCH_NAME
          println "Change ID: " + env.CHANGE_ID
          println "Hello World"
        }         
      }
  }
}
