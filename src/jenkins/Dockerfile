FROM jenkins/jenkins:lts
USER root

# Install docker
# https://www.jenkins.io/doc/book/installing/docker/#on-windows
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli

# Install maven
RUN apt-get update && apt-get install -y maven
RUN mvn -v

# # Setup known host
# # RUN ssh-keyscan -H jenkins-agent >> /var/jenkins_home/.ssh/known_hosts

RUN chown -R 1000:1000 /var/jenkins_home
# USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow json-path-api slack sonar htmlpublisher"