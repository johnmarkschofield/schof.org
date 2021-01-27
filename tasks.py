"""This file copyright John Mark Schofield."""


import os
import os.path

from invoke import task

from localprivateconf import *  # noqa

OUTPUT_DIR = "output"
CACHE_DIR = "cache"
LOCAL_HOST = "http://localhost:8000"
CACHE_SECONDS = 600


@task
def localclean(c):
    """Clean local checkout of build artifacts."""
    if os.path.isdir(OUTPUT_DIR):
        c.run('rm -rf %s' % OUTPUT_DIR)
        c.run('mkdir %s' % OUTPUT_DIR)

    if os.path.isdir(CACHE_DIR):
        c.run('rm -rf %s' % CACHE_DIR)
        c.run('mkdir %s' % CACHE_DIR)

    c.run('rm -f *.pyc')


@task
def build(c):
    """Build it all."""
    theme_path = os.path.join(os.getcwd(), 'pelican-themes/gum/')
    c.run('sudo pelican-themes -s %s' % theme_path)
    c.run('pelican -s buildconf.py')


@task
def rebuild(c):
    """Clean and build."""
    localclean(c)
    build(c)


@task
def serve(c):
    """Serve local changes to localhost:8000 for testing."""
    os.chdir(OUTPUT_DIR)

    import http.server
    import socketserver

    PORT = 8000


    Handler = http.server.SimpleHTTPRequestHandler

    Handler.extensions_map={
            '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
            '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg': 'image/svg+xml',
        '.css': 'text/css',
        '.js':  'application/x-javascript',
        '': 'text/html', # Default
        }

    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("serving at port", PORT)
    httpd.serve_forever()


@task
def clearcloudfrontcache(c):
    """Tell Cloudfront to invalidate the entire cache."""
    c.run(
        'aws cloudfront create-invalidation '
        '--distribution-id %s --paths /\*' % DISTRIBUTION_ID)


@task
def publish(c):
    """Publish."""
    build(c)
    c.run(
        's3cmd ' +
        '--no-preserve --rr ' +
        '--delete-removed ' +
        '--mime-type="text/html" ' +
        '--guess-mime-type ' +
        '--add-header="Cache-Control:max-age=%s" ' % CACHE_SECONDS +
        'sync output/ s3://schof.org/')
    clearcloudfrontcache(c)


@task
def validate(c):
    """Not working yet."""
    c.run('pelican --debug -s validateconf.py')
