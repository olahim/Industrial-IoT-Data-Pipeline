# Jenkins on MasterControl

Install Jenkins and GNU Make on MasterControl. Configure Jenkins to checkout the GitHub repository. The pipeline validates, tests, asks for approval on `main`, deploys through SSH/rsync, and verifies. Ensure Jenkins has a scoped SSH key and access to the configured cluster nodes. Deployment requires `CONFIRM_DEPLOY=yes`; do not store passwords in `.env`. Review the Jenkinsfile and configure branch discovery to support `when { branch 'main' }`.
