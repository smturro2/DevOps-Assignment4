

pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}


// // Docs:
// // - https://www.jenkins.io/doc/book/pipeline/docker/
// // - youtube tutorial: https://www.youtube.com/watch?v=ZPD_PzGOvFM
// pipeline {
//     agent any
//     stages {
//         stage("verify tooling") {
//             steps {
//                 sh '''
//                 docker version
//                 docker info
//                 docker compose version 
//                 curl --version
//                 '''
//             }
//         }
//         stage("build") {
//             steps {
//                 sh 'docker-compose up -d --build'
//             }
//         }
//     }

//     post {
//         always {
//             sh 'docker-compose down'
//         }
//     }
// }