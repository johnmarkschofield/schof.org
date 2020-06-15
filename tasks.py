"""This file copyright John Mark Schofield."""


import os
import os.path
# import sys
import http.server
import socketserver

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
    theme_path = os.path.join(os.getcwd(), 'themes/gum/')
    c.run('pelican-themes -s %s' % theme_path)
    c.run('pelican -s publishconf.py')


@task
def rebuild(c):
    """Clean and build."""
    localclean(c)
    build(c)


# Not sure what I'm actually using this for. Maybe delete.
# @task
# def watch(c):
#     """Watch for local changes."""
#     c.run('pelican -r -s localconf.py')


@task
def serve(c):
    """Serve local changes to localhost:8000 for testing."""
    os.chdir(OUTPUT_DIR)

    port = 8000

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("serving at port", port)
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
    # c.run('git status | grep -q "nothing to commit, working dir. clean"')
    # c.run('git status | grep -q "Your branch is up-to-date with"')
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
def cleanup(c):
    """Fix everything."""
    localclean()
    publish()
    c.run(
        's3cmd ' +
        '--no-preserve ' +
        '--delete-removed ' +
        '--check-md5 ' +
        '--mime-type="text/html" ' +
        '--guess-mime-type ' +
        '--add-header="Cache-Control:max-age=%s" ' % CACHE_SECONDS +
        'sync output/ s3://schof.org/')
    c.run('s3cmd --recursive modify --add-header="Cache-Control:' +
          'max-age=%s" ' % CACHE_SECONDS +
          's3://schof.org/')
    clear_cloudfront_cache()


@task
def validate(c):
    """Not working yet."""
    c.run('pelican --debug -s validateconf.py')


# @task
# def image(c):
#     """Not tested."""
#     # God this is so fragile and lame, but I'm only parsing HTML that I've
#     # generated myself from Lightroom so it should be OK.
#     image_page = prompt('What is the HTML page of the image? ')
#     img_page_nohost = image_page.replace(LOCAL_HOST, '')
#     image_page_html = requests.get(image_page)
#     if image_page_html.status_code != 200:
#         abort('Unable to download image page from localhost.')
#     for line in image_page_html.text.split('\n'):
#         if "<img src" in line:
#             image_url_fragment = line.split('<img src="')[1].strip('"')
#             break
#     image_url_nohost = '/'.join(img_page_nohost.split('/')[:-1]) + '/' + image_url_fragment  # noqa

#     print('[![](%s)](%s)' % (image_url_nohost, img_page_nohost))
