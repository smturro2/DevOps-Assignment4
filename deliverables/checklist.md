# Part 1: Environment Configuration
Question 1

Explain the differences between development, integration, staging, and production environments. In your answer, address:

- [] Purpose and characteristics of each environment
- [] Data management strategies for each environment
- [] Access control and security considerations
- [] Testing approaches appropriate for each environment


# Part 2: Practical Implementation

- [X] Database integration (PostgreSQL, MySQL, or MongoDB)
- [X] Database schema files for staging database creation
- [X] At least 2 API endpoints that interact with the database
- [X] One end-to-end test that tests a user journey
- [X] Performance test configuration for load testing
- [X] SonarQube integration for code quality analysis
- [X] Notification setup for pipeline status (Slack or email)

Question 2: Jenkins Agent Configuration

Set up at least one Jenkins agent (slave node), configure agent labels for specific tasks (e.g., testing, deployment), distribute pipeline workload across multiple agents, and document agent setup and configuration process.

Deliverables:

- [X] Screenshots of Jenkins agent configuration and status
- [X] Jenkins agent labels configuration

Question 3: Source Control Integration

Configure webhook triggers from your Git repository and set up branch-specific pipeline behavior based on your preferences (e.g., different stages for main vs feature branches).

Deliverables:

- [X] Webhook configuration screenshots from Git repository
- [X] Jenkinsfile showing branch-specific pipeline logic
- [X] Screenshot of webhook triggering pipeline runs

Question 4: Build and Package

Build application artifacts, version your builds using semantic versioning or build numbers, and store artifacts in Jenkins artifacts.

Deliverables:

- [] Build logs showing successful artifact creation
- [] Screenshots of versioned artifacts in Jenkins
- [] Build configuration in Jenkinsfile

Question 5: Code Quality Analysis

Integrate with SonarQube to analyze code for bugs, vulnerabilities, and code smells, and configure quality gates that prevent deployment if quality standards aren't met.

Deliverables:

- [X] SonarQube project configuration screenshots
- [X] SonarQube analysis reports with quality metrics
- [] Quality gate configuration and pipeline failure evidence when standards not met

Question 6: Database Management

Write the staging database schema to build staging database from scratch and seed staging database with test data.

Deliverables:

- [X] Database schema scripts (SQL files or equivalent)
- [X] Test data seeding scripts
- [X] Screenshots showing successful database creation and seeding

Question 7: End-to-End Testing

Execute one end-to-end test scenario that simulates real user workflows to test user journey using testing frameworks like Selenium, Cypress, or Playwright, and generate test reports.

Deliverables:

- [X] End-to-end test code/scripts
- [X] Test execution screenshots 
- [X] Generated test reports (HTML, XML, or similar format)

Question 8: Performance Testing

- [X] Load test configuration files
- [X] Performance test execution logs
- [X] Performance reports with metrics and thresholds

Question 9: Notification System

- [X] Notification configuration in Jenkins
- [X] Screenshots of successful deployment notifications
- [X] Screenshots of failure notifications with error details

