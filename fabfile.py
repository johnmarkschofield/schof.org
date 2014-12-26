from fabric.api import *
import os
import sys
import SimpleHTTPServer
import SocketServer

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))


def build():
    local('pelican -d --ignore-cache -s localconf.py')


def rebuild():
    clean()
    build()


def watch():
    local('pelican -r -s localconf.py')


def serve():
    os.chdir(env.deploy_path)

    PORT = 8000

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        ('', PORT),
        SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()


@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    # local('git commit -a && git push origin master')
    local(
        's3cmd ' +
        '--check-md5 ' +
        '--delete-removed ' +
        'sync output/ s3://schofdotorg-pelican/')


def deploy():
    publish()


def pub():
    publish()
