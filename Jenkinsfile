pipeline{
    agent {
        label 'master'
    }

    parameters {
        choice(name: 'browser', choices: ['chrome', 'no_gui', 'remote'], description: 'Running type')

    }

    stages{
        stage('自动测试程序源码同步') {
            steps {
                sh 'mkdir -p iSelenium_Python'
                dir("iSelenium_Python"){
                    git branch:'docker', url:'git@github.com:princeqjzh/iSelenium_Python.git'
                }
            }
        }

        stage('运行自动化测试') {
            steps {
                sh '''
                    . ~/.bash_profile

                    cd iSelenium_Python

                    #更新python依赖库
                    pip3.9 install -r requirements.txt

                    #运行自动化测试
                    pytest -sv test/web_ut.py
                '''
            }
        }
    }

    post {
        always {
            emailext body: '$DEFAULT_CONTENT', recipientProviders: [[$class: 'RequesterRecipientProvider']], subject: '$DEFAULT_SUBJECT'
        }
    }
}