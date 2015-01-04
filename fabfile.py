from fabric.api import *  # noqa
import os
import os.path
import sys
import SimpleHTTPServer
import SocketServer
import requests

OUTPUT_DIR = "output"
CACHE_DIR = "cache"
LOCAL_HOST = "http://localhost:8000"


def clean():
    if os.path.isdir(OUTPUT_DIR):
        local('rm -rf %s' % OUTPUT_DIR)
        local('mkdir %s' % OUTPUT_DIR)

    if os.path.isdir(CACHE_DIR):
        local('rm -rf %s' % CACHE_DIR)
        local('mkdir %s' % CACHE_DIR)


def build():
    local('pelican-themes -s ~/code/schof/pelican-schof/themes/gum/')
    local('pelican -s localconf.py')


def rebuild():
    clean()
    build()


def watch():
    local('pelican -r -s localconf.py')


def serve():
    os.chdir(OUTPUT_DIR)

    PORT = 8000

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        ('127.0.0.1', PORT),
        SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()


def publish():
    clean()
    local('git status | grep -q "nothing to commit, working directory clean"')
    local('git status | grep -q "Your branch is up-to-date with"')
    local('pelican -s publishconf.py')
    # local('git commit -a && git push origin master')
    local(
        's3cmd ' +
        '--check-md5 ' +
        '--delete-removed ' +
        'sync output/ s3://schof.org/')


def deploy():
    publish()


def pub():
    publish()


def validate():
    local('pelican --debug -s validateconf.py')


def image():
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
