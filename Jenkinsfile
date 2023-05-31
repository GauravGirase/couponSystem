pipeline {
  agent any
  stages{
      stage ("Hello"){
        steps{
          println "Branch Name: " + env.BRANCH_NAME
          println "Change ID: " + env.CHANGE_ID
          println "GITHUB_PAYLOAD: " + env.GITHUB_PAYLOAD
          println "Hello World"
          def url = "https://api.github.com/repos/GauravGirase/couponSystem/pulls/5"
          def head_sha = sh (returnStdout: true, script: "curl -s ${url} | jq -r .head.sha").trim()
          println "Head sha: " + head_sha
          
        }         
      }
  }
}
