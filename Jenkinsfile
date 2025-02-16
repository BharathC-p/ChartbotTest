pipeline {
    agent any

    environment {
        APP_SERVER_IP = '35.154.48.37'
        APP_SERVER_USER = 'ubuntu'
        SSH_KEY = "/var/lib/jenkins/app.pem"  // Use the ID from Jenkins Credentials
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/chatbot.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Deploy to Application Server') {
            steps {
                sh """
                ssh -i $SSH_KEY $APP_SERVER_USER@$APP_SERVER_IP << EOF
                cd /home/$APP_SERVER_USER/chatbot
                git pull origin main
                pip3 install -r requirements.txt
                sudo systemctl restart chatbot
                EOF
                """
            }
        }
    }
}
