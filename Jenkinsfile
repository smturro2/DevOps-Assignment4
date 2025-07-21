// Docs:
// - https://www.jenkins.io/doc/book/pipeline/docker/
// - youtube tutorial: https://www.youtube.com/watch?v=ZPD_PzGOvFM
pipeline {
    agent any

    environment {
        API_VERSION = "1.0.1"
        WEB_VERSION = "1.0.1"
        K6_VERSION = "1.0.1"
    }

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
                // sh 'mvn clean package sonar:sonar'
                 sh 'sonar-scanner'
              }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    docker.build("countries-app/api:${API_VERSION}", './src/api')
                    docker.build("countries-app/web:${WEB_VERSION}", './src/web')
                    docker.build("countries-app/k6:${K6_VERSION}", './src/k6')
                }
            }
        }
        
        stage("Run Docker Containers") {
            steps {
                sh 'docker compose up -d'
            }
        }
        stage("integration test") {
            steps {
                sh 'docker compose exec web pytest tests --html=reports/pytest_report.html --self-contained-html --capture=tee-sys --log-cli-level=INFO'
                archiveArtifacts artifacts: 'src/web/reports/reports/pytest_report.html', allowEmptyArchive: true
            }
        }

        stage("Load Testing (dev only)") {
            when {
                branch 'dev'
            }
            steps {
                sh 'docker compose exec k6 k6 run /k6-load-tests.js --out json=/src/web/reports/k6_report.json'
                archiveArtifacts artifacts: 'src/web/reports/reports/k6_results.json', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            sh 'docker compose down'

            // Publish pytest reports
            // see: https://plugins.jenkins.io/htmlpublisher/
            publishHTML (target : [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'src/web/reports',
                reportFiles: 'pytest_report.html',
                reportName: 'Pytest Report',
                reportTitles: 'Pytest Report'
            ])

            // Publish load reports
            publishHTML (target : [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'src/web/reports',
                reportFiles: 'src/web/reports/k6_report.json',
                reportName: 'K6 Report',
                reportTitles: 'K6 Report'
            ])

        }
        success {
            slackSend color: "good", message: "Pipeline PASSED"
        }
        failure {
            slackSend (
                color: "danger",
                message: "Pipeline FAILED!\n" +
                            "Job: ${env.JOB_NAME}\n" + 
                            "Build Number: ${env.BUILD_NUMBER}\n" +
                            "Failed Stage: ${env.BUILD_URL}\n" +
                            "See details: ${env.STAGE_NAME}"
            )
            
        }
    }
}