

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
        stage("verify tooling") {
            steps {
                sh 'docker version'
                sh 'docker info'
                sh 'docker compose version'
            }
        }
        stage("static testing") {
            steps {
              withSonarQubeEnv('SonarQube') {
                sh 'mvn clean package sonar:sonar'
              }
            }
        }
        // stage("build") {
        //     steps {
        //         sh 'docker compose up -d --build'
        //     }
        // }
        // stage("integreation test") {
        //     steps {
        //         sh 'docker compose exec web pytest tests --html=reports/report.html --self-contained-html --capture=tee-sys --log-cli-level=INFO'
        //     }
        // }
        // stage('load test') {
        //     steps {
        //         script {
        //             // Run k6 container to perform load testing
        //             sh """
        //             docker run --rm -i -v \$(pwd):/scripts loadimpact/k6 run /scripts/k6-load-tests.js > k6-output.txt
        //             """
        //         }
        //     }
        // }
    }

    // post {
    //     always {
    //         sh 'docker compose down'
    //     }
    // }
}