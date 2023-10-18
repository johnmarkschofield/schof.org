"""This file copyright John Mark Schofield."""


import os
import os.path

from invoke.tasks import task

OUTPUT_DIR = "output"
CACHE_DIR = "cache"
LOCAL_HOST = "http://localhost:8000"
CACHE_SECONDS = 600
CHECKOUT_DIR = "/srv/schof.org/"
BUILD_DIR = os.path.join(CHECKOUT_DIR, OUTPUT_DIR)
PUBLISH_DIR = "/var/www/schof.org"


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
    # c.run('cd %s' % CHECKOUT_DIR)
    theme_path = os.path.join(CHECKOUT_DIR, 'themes_place/gum/')
    c.run('pelican-themes -i %s' % theme_path)
    c.run('pelican -s buildconf.py')


@task
def laptopbuild(c):
    """Build it all."""
    theme_path = os.path.join(os.curdir, 'themes_place/gum/')
    c.run('pelican-themes -i %s' % theme_path)
    c.run('pelican -s localconf.py')


@task
def laptopserve(c):
    """Serve locally on port 8000."""
    c.run('pelican -rl -s localconf.py')


@task
def laptopclean(c):
    """Clean local checkout of build artifacts."""
    if os.path.isdir(OUTPUT_DIR):
        c.run('rm -rf %s' % OUTPUT_DIR)
        c.run('mkdir %s' % OUTPUT_DIR)

    if os.path.isdir(CACHE_DIR):
        c.run('rm -rf %s' % CACHE_DIR)
        c.run('mkdir %s' % CACHE_DIR)

    c.run('rm -f *.pyc')


@task
def publish(c):
    """Publish."""
    c.run('mkdir -p %s' % PUBLISH_DIR)
    c.run('mv %s/ %s.old/' % (PUBLISH_DIR, PUBLISH_DIR))
    c.run('cp -al /srv/schof.org/output %s' % PUBLISH_DIR)
    c.run('rm -rf %s.old' % PUBLISH_DIR)
