
pipeline {
    agent { label 'built-in' }

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    environment {
        PROJECT_NAME = 'Industrial-IoT-Data-Pipeline'
    }

    stages {

        stage('Checkout GitHub') {
            steps {
                checkout scm

                sh '''
                    set -eu

                    echo "Current commit:"
                    git rev-parse --short HEAD

                    echo "Repository:"
                    git remote -v
                '''
            }
        }

        stage('Validate Repository') {
            steps {
                sh '''
                    set -eu

                    test -f README.md
                    test -f LICENSE
                    test -f Jenkinsfile

                    echo "Repository validation passed."
                '''
            }
        }

        stage('Validate Python Syntax') {
            steps {
                sh '''
                    set -eu

                    python3 - <<'PY'
import ast
from pathlib import Path

excluded = {'.git', '.venv', 'venv'}

files = sorted(
    p for p in Path('.').rglob('*.py')
    if not any(part in excluded for part in p.parts)
)

for path in files:
    with path.open(encoding='utf-8') as f:
        ast.parse(f.read(), filename=str(path))

print(f'Python syntax passed: {len(files)} files')
PY
                '''
            }
        }

        stage('Validate Shell Scripts') {
            steps {
                sh '''
                    set -eu

                    find . -type f -name '*.sh' \
                        -not -path './.git/*' \
                        -exec bash -n {} +

                    echo "Shell syntax passed."
                '''
            }
        }

        stage('Inventory SQL Files') {
            steps {
                sh '''
                    set -eu

                    find . -type f -name '*.sql' \
                        -not -path './.git/*' | sort

                    echo "SQL inventory completed."
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    set -eu

                    if [ -d tests/unit ] && \
                       find tests/unit -type f \
                         \\( -name 'test_*.py' -o -name '*_test.py' \\) \
                         | grep -q .; then

                        python3 -m pytest tests/unit -q

                    else
                        echo "No unit tests found yet."
                    fi
                '''
            }
        }

        stage('Validate Cluster SSH') {
            steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'cluster-ssh-key',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    )
                ]) {
                    sh '''
                        set -eu

                        for NODE in MasterDB WorkerC1 WorkerC2 WorkerC3; do
                            echo "Checking $NODE"

                            ssh \
                              -i "$SSH_KEY" \
                              -o IdentitiesOnly=yes \
                              -o BatchMode=yes \
                              -o StrictHostKeyChecking=yes \
                              -o ConnectTimeout=5 \
                              "$SSH_USER@$NODE" hostname
                        done
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Industrial IoT CI validation passed.'
        }

        failure {
            echo 'Industrial IoT CI validation failed.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
