# Example
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
