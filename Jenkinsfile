// Docs:
// - https://www.jenkins.io/doc/book/pipeline/docker/
// - youtube tutorial: https://www.youtube.com/watch?v=ZPD_PzGOvFM
pipeline {
    agent any

    environment {
        BASE_VERSION = "1.0"
        BUILD_NUMBER = "${BASE_VERSION}.${env.BUILD_NUMBER}"
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
                // https://stackoverflow.com/questions/53849416/how-to-configure-jenkinsfile-to-analyze-python-code-with-sonar
                script {
                    def scannerHome = tool 'SonarQube';
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
        
        stage("Run Docker Containers") {
            steps {
                sh 'docker compose up -d'
            }
        }
        stage("Integration Test") {
            steps {
                    def version = "${BASE_VERSION}.${env.BUILD_NUMBER}"
                    sh """
                        docker compose exec web \
                        pytest tests \
                        --html=reports/pytest_report_${version}.html \
                        --self-contained-html \
                        --capture=tee-sys \
                        --log-cli-level=INFO
                    """
                    archiveArtifacts artifacts: "src/web/reports/pytest_report_${version}.html", allowEmptyArchive: true
            }
        }

        stage("Load Testing (dev only)") {
            when {
                branch 'dev'
            }
            steps {
                    def version = "${BASE_VERSION}.${env.BUILD_NUMBER}"
                    sh """
                        docker compose exec k6 \
                        k6 run /k6-load-tests.js \
                        --out json=/src/web/reports/k6_report_${version}.json
                    """
                    archiveArtifacts artifacts: "src/web/reports/k6_report_${version}.json", allowEmptyArchive: true
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