

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
        stage("Static Testing") {
            steps {
              withSonarQubeEnv('SonarQube') {
                sh 'mvn clean package sonar:sonar'
              }
            }
        }
        
        stage('SonarQube Quality Gate') {
            steps {
                // https://www.youtube.com/watch?v=jrksCo-M1Ns
                waitForQualityGate abortPipeline: true
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
    }

    // post {
    //     always {
    //         sh 'docker compose down'
    //     }
    // }
}