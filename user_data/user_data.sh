#!/bin/bash
sudo yum update -y
sudo yum install git -y
git clone https://github.com/nijin39/nopo-dirty.git /home/ec2-user/nopo-dirty
cat >/home/ec2-user/nopo-dirty/src/main/resources/application.properties <<EOL
spring.datasource.driverClassName=org.mariadb.jdbc.Driver
spring.datasource.url=jdbc:mariadb://{user-datasource}/nopo
spring.datasource.username=admin
spring.datasource.password={user-password}
springdoc.swagger-ui.path=/swagger-ui.html
springdoc.swagger-ui.use-root-path=true
EOL
sudo yum localinstall https://corretto.aws/downloads/latest/amazon-corretto-17-x64-linux-jdk.rpm -y
cd /home/ec2-user/nopo-dirty && nohup ./gradlew bootRun --args='--server.port=80' &