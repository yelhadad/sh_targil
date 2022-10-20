node {
    agent {
        docker { image 'yelhadad/shabak:4'}
    }
    stage('Build') {
        sh 'python3 /tmp/zip_job,py'
    }

    stage('Publish') {
        steps {
            def server = Artifactory.newServer url: 'some-url', username: 'super-user', password: 'Qw123456!'
            def uploadSpec = """ {
                "files": [
                {
                   "pattern": "/tmp/ziped_files",
                   "target": "."
                 }
                ]
            }"""
            server.upload spec: uploadSpec
        }
    }
}