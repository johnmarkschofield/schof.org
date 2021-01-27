#!/bin/bash

# This is a provisioing script run by Vagrant on the VM.
# It should not be run manually.

set -u

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
pip3 freeze > /vagrant/requirements.txt

# Copy reference s3 config file from document root to where s3cmd expects it.
cp /vagrant/.s3cfg /home/vagrant
mkdir -p /home/vagrant/.aws
cp /vagrant/.aws/credentials /home/vagrant/.aws/

grep -q vagrant /home/vagrant/.profile || echo "cd /vagrant" >> /home/vagrant/.profile

chown -R vagrant:vagrant /home/vagrant

if [ -f /var/run/reboot-required ]; then
    echo "Copying reboot-required file to /vagrant."
    cp /var/run/reboot-required /vagrant/
fi
