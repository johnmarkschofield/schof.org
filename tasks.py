"""This file copyright John Mark Schofield."""


import os
import os.path

from invoke import task

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
    # Fixme: I ran this manually once.
    # theme_path = os.path.join(os.getcwd(), 'pelican-themes/gum/')
    # c.run('pelican-themes -s %s' % theme_path)
    c.run('pelican -s buildconf.py')
    c.run('find /home/schof/schof.org -type d -exec chmod o+rx {} \;')
    c.run('chmod -R a+r /home/schof/schof.org/output')


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
        '--guess-mime-type ' +
        '--default-mime-type="text/css" ' +
        '--add-header="Cache-Control:max-age=%s" ' % CACHE_SECONDS +
        'sync output/ s3://schof.org/')

    # For some reason stuff.css was getting the wrong mime type.
    c.run(
        's3cmd -f ' +
        '--no-preserve --rr ' +
        '--mime-type="text/css" ' +
        '--no-guess-mime-type ' +
        '--add-header="Cache-Control:max-age=%s" ' % CACHE_SECONDS +
        'put output/theme/*.css s3://schof.org/theme/')

    clearcloudfrontcache(c)


@task
def validate(c):
    """Not working yet."""
    c.run('pelican --debug -s validateconf.py')
