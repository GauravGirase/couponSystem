pipeline {
  agent any
  stages{
      stage ("Hello"){
        steps{
          script{
              println "Branch Name: " + env.BRANCH_NAME
              println "Change ID: " + env.CHANGE_ID
              println "GITHUB_PAYLOAD: " + env.GITHUB_PAYLOAD
              println "Hello World2"
         
            if(env.CHANGE_ID){
              println "PR=1: " + pullRequest.title
              println "PR=Body: " + pullRequest.body 
               def url = "https://api.github.com/repos/GauravGirase/couponSystem/pulls/${env.CHANGE_ID}"
//               def head_sha = sh (returnStdout: true, script: "curl -s ${url} | jq -r .head.sha").trim()
              def curl_response = sh (returnStdout: true, script: "curl -s ${url}")
              println "curl_response: " + curl_response
            }
          }
        }         
      }
  }
}
