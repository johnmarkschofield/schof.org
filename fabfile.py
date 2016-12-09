"""This file copyright John Mark Schofield."""

import SimpleHTTPServer
import SocketServer
import os
import os.path
import sys

from fabric.api import *  # noqa

import requests

OUTPUT_DIR = "output"
CACHE_DIR = "cache"
LOCAL_HOST = "http://localhost:8000"


def clean():
    """Clean Slate."""
    if os.path.isdir(OUTPUT_DIR):
        local('rm -rf %s' % OUTPUT_DIR)
        local('mkdir %s' % OUTPUT_DIR)

    if os.path.isdir(CACHE_DIR):
        local('rm -rf %s' % CACHE_DIR)
        local('mkdir %s' % CACHE_DIR)

    local('rm *.pyc')


def build():
    """Build it all."""
    theme_path = os.path.join(os.getcwd(), 'themes/gum/')
    local('pelican-themes -s %s' % theme_path)
    local('pelican -s publishconf.py')


def rebuild():
    """Clean and build."""
    clean()
    build()


def watch():
    """Watch for local changes."""
    local('pelican -r -s localconf.py')


def serve():
    """Serve local changes to localhost."""
    os.chdir(OUTPUT_DIR)

    port = 8000

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    handler.extensions_map.update({
        '': 'text/html'})
    server = AddressReuseTCPServer(
        ('127.0.0.1', port),
        handler)

    sys.stderr.write('Serving on port {0} ...\n'.format(port))
    server.serve_forever()


def publish():
    """Publish."""
    local('git status | grep -q "nothing to commit, working directory clean"')
    local('git status | grep -q "Your branch is up-to-date with"')
    rebuild()
    local(
        's3cmd ' +
        '--check-md5 --no-preserve ' +
        '--delete-removed ' +
        '--mime-type="text/html" ' +
        '--guess-mime-type ' +
        '--cf-invalidate --cf-invalidate-default-index ' +
        'sync output/ s3://schof.org/')


def deploy():
    """AKA publish."""
    publish()


def update_virtualenv():
    """Update local virtualenv."""
    if hasattr(sys, 'real_prefix'):
        local("pip install -r requirements.txt")
        local("pip freeze --local | grep -v '^\-e' | "
              "cut -d = -f 1  | xargs pip install -U")
        local('Pip freeze --local > requirements.txt')
    else:
        fabric.utils.abort("Not running in a virtualenv. Fix that.")


def pub():
    """AKA publish."""
    publish()


def validate():
    """Not working yet."""
    local('pelican --debug -s validateconf.py')


def image():
    """Not tested."""
    # God this is so fragile and lame, but I'm only parsing HTML that I've
    # generated myself from Lightroom so it should be OK.
    image_page = prompt('What is the HTML page of the image? ')
    img_page_nohost = image_page.replace(LOCAL_HOST, '')
    image_page_html = requests.get(image_page)
    if image_page_html.status_code != 200:
        abort('Unable to download image page from localhost.')
    for line in image_page_html.text.split('\n'):
        if "<img src" in line:
            image_url_fragment = line.split('<img src="')[1].strip('"')
            break
    image_url_nohost = '/'.join(img_page_nohost.split('/')[:-1]) + '/' + image_url_fragment  # noqa

    print('[![](%s)](%s)' % (image_url_nohost, img_page_nohost))
