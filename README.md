# Example




Program 2
git config --global user.name "Neha Devarasetty"
git config --global user.email "your-email@example.com"

git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
git pull origin main

Program 3
:: Verify Docker
docker --version
docker info

:: Pull Ubuntu image
docker pull ubuntu

:: Check images
docker images

:: Run Ubuntu container
docker run -it ubuntu

:: INSIDE THE CONTAINER RUN:
cat /etc/os-release
exit

:: Back in Windows terminal
docker ps
docker ps -a

:: Remove the stopped Ubuntu container (replace with actual container ID)
docker rm <container_id>

:: View images
docker images

:: Create project folder
mkdir flask-docker-app
cd flask-docker-app

:: Create app.py
notepad app.py

:: Create requirements.txt
notepad requirements.txt

:: Create Dockerfile
notepad Dockerfile

:: Verify files
dir

:: Build Docker image
docker build -t flask-app .

:: Verify image
docker images

:: Run Flask container
docker run -d -p 5000:5000 flask-app

:: Verify container is running
docker ps

:: Open in browser
http://localhost:5000

:: Login to Docker Hub
docker login

:: Tag image
docker tag flask-app YOUR_DOCKERHUB_USERNAME/flask-app

:: Verify tag
docker images

:: Push to Docker Hub
docker push YOUR_DOCKERHUB_USERNAME/flask-app

Program 5

mkdir DockerComposeFile
cd DockerComposeFile

notepad docker-compose.yml

docker compose config

docker compose up -d

docker ps

:: Open in browser
http://localhost:9090

docker compose down

docker ps

docker-compose.yml
services:
  web:
    image: nginx
    ports:
      - "9090:80"

  database:
    image: redis
	
Program 6
Download Jenkins (.msi) file
localhost:8080

Install Docker Desktop

Download SonarQube via docker

docker run -d --name sonarqube -p 9000:9000 sonarqube

open in localhost:9000

In Sonar Qube
my acc->security->generate token
save the token

Go to Jenkins
plugins
download SonarQube Scanner

Go to System
sonarqube server->add new sonarqube server->add token->secret text->select from drop down menu

click save

Go to Tools
add sonarqube scanner

new item
pipeline script(install via python)
node {

    stage('Checkout') {
        git branch: 'main',
            url: 'https://github.com/Neha-140/Example'
    }

    stage('SonarQube Analysis') {

        def scannerHome = tool 'SonarScanner'

        withSonarQubeEnv('SonarQube') {

            bat """
            "${scannerHome}\\bin\\sonar-scanner.bat" ^
            -Dsonar.projectKey=example ^
            -Dsonar.projectName=example ^
            -Dsonar.sources=.
            """
        }
    }
}

build and see status in sonarqube
pipeline script (via zip) 
node {

    stage('Checkout') {
        git 'https://github.com/bloodbankmanagement.git' (This is the URL from github)
    }

    stage('SonarQube Analysis') {
        withSonarQubeEnv('SonarQube') {
            bat """
            "C:/Program Files/sonar-scanner-cli-8.0.1.6346-windows-x64/sonar-scanner-8.0.1.6346-windows-x64/bin/sonar-scanner.bat" ^
            -Dsonar.projectKey=bloodbank ^
            -Dsonar.sources=. ^
            -Dsonar.host.url=http://localhost:9000 ^
            -Dsonar.login=squ_cb15c70ff72e8ee75528eff441e1efe92d3e2a11
            """
        }
    }
}


node {

    stage('Checkout') {
        git branch: 'main',
            url: 'https://github.com/Neha-140/Example'
    }

    stage('SonarQube Analysis') {

        def scannerHome = tool 'SonarScanner'

        withSonarQubeEnv('SonarQube') {

            bat """
            "${scannerHome}\\bin\\sonar-scanner.bat" ^
            -Dsonar.projectKey=example ^
            -Dsonar.projectName=example ^
            -Dsonar.sources=.
            """
        }
    }
}
Program 7
donwlooad maven and gradle

Program 8
mvn --version

mvn archetype:generate -DgroupId=com.example -DartifactId=myapp -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

cd myapp

mvn clean install

Program 9
mvn archetype:generate -DgroupId=com.example -DartifactId=prog9 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

cd prog9

mvn clean install

gradle init

Found a Maven build. Generate a Gradle build from this?
yes

Select build script DSL:
2 (Groovy)

Generate build using new APIs and behavior?
no

rmdir /s /q src\test

gradle build

gradle run
change in build.gradle
plugins {
    id 'java-library'
    id 'maven-publish'
    id 'application'
}

in the end
application{
	mainClass= "com.example.App"
}







