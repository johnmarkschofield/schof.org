#!/bin/bash

USERNAME="schof"
HOMEDIR="/home/$USERNAME"
MAINDIR="$HOMEDIR/schof.org"

mkdir -p $MAINDIR

apt-get update
apt-get dist-upgrade -y


apt-get install -y python3-pip
apt-get install -y s3cmd
apt-get install -y awscli
apt-get install -y tree

apt-get -y autoremove

pip3 install pelican
pip3 install invoke
pip3 install html5lib
pip3 install Markdown
pip3 install py_w3c
pip3 install Pillow
pip3 install Piexif

# Document our package versions
pip3 freeze > $MAINDIR/requirements.txt

# Copy reference s3 config file from document root to where s3cmd expects it.
cp $MAINDIR/.s3cfg $HOMEDIR
mkdir -p $HOMEDIR/.aws
cp $MAINDIR/.aws/credentials $HOMEDIR/.aws/

chown -R $USERNAME:$USERNAME $HOMEDIR

