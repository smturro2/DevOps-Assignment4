

// pipeline {
//     agent any

//     stages {
//         stage('Hello') {
//             steps {
//                 echo 'Hello World'
//             }
//         }
//     }
// }


// Docs:
// - https://www.jenkins.io/doc/book/pipeline/docker/
// - youtube tutorial: https://www.youtube.com/watch?v=ZPD_PzGOvFM
pipeline {
    agent any
    stages {
        stage("Verify Tooling") {
            steps {
                sh 'docker version'
                sh 'docker info'
                sh 'docker compose version'
            }
        }
        // stage("Static Testing") {
        //     steps {
        //       withSonarQubeEnv('SonarQube') {
        //         sh 'mvn clean package sonar:sonar'
        //       }
        //     }
        // }
        
        stage("build") {
            steps {
                sh 'docker compose up -d --build'
            }
        }
        // stage("integreation test") {
        //     steps {
        //         sh 'docker compose exec web pytest tests --html=reports/report.html --self-contained-html --capture=tee-sys --log-cli-level=INFO'
        //     }
        // }

        stage("Load Testing") {
            steps {
                // Run k6 in a docker container
                sh '''
                docker run --rm -i \
                --network host \
                -v ${WORKSPACE}/k6-load-tests.js:/k6-load-tests.js \
                loadimpact/k6 run /k6-load-tests.js
                '''
            }
        }
    }

    post {
        // always {
        //     sh 'docker compose down'
        // }
        success {
            slackSend color: "good", message: "Pipeline PASSED"
        }
        failure {
            slackSend color: "bad", message: "Pipeline FAILED!"
        }
    }
}