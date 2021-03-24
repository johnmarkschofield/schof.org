"""This file copyright John Mark Schofield."""


import os
import os.path

from invoke import task

OUTPUT_DIR = "output"
CACHE_DIR = "cache"
LOCAL_HOST = "http://localhost:8000"
CACHE_SECONDS = 600
CHECKOUT_DIR = "/srv/schof.org/"


@task
def localclean(c):
    """Clean local checkout of build artifacts."""
    c.run('cd %s' % CHECKOUT_DIR)
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
    c.run('cd %s' % CHECKOUT_DIR)
    theme_path = os.path.join(CHECKOUT_DIR, 'pelican-themes/gum/')
    c.run('pelican-themes -s %s' % theme_path)
    c.run('pelican -s buildconf.py')
    # c.run('find /home/schof/schof.org -type d -exec chmod o+rx {} \;')
    # c.run('chmod -R a+r /home/schof/schof.org/output')


@task
def rebuild(c):
    """Clean and build."""
    localclean(c)
    build(c)


# @task
# def publish(c):
#     """Publish."""

#     build(c)

#     c.run(
#         's3cmd ' +
#         '--no-preserve --rr ' +
#         '--delete-removed ' +
#         '--guess-mime-type ' +
#         '--default-mime-type="text/css" ' +
#         '--add-header="Cache-Control:max-age=%s" ' % CACHE_SECONDS +
#         'sync output/ s3://schof.org/')

#     # For some reason stuff.css was getting the wrong mime type.
#     c.run(
#         's3cmd -f ' +
#         '--no-preserve --rr ' +
#         '--mime-type="text/css" ' +
#         '--no-guess-mime-type ' +
#         '--add-header="Cache-Control:max-age=%s" ' % CACHE_SECONDS +
#         'put output/theme/*.css s3://schof.org/theme/')

#     clearcloudfrontcache(c)


# @task
# def validate(c):
#     """Not working yet."""
#     c.run('pelican --debug -s validateconf.py')
