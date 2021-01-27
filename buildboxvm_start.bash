#!/bin/bash

# This is the startup script for the schof.org build VM. This is what you should run
# from the command-line on your local system to start the buildbox.
# 
#

set -u


git pull
git submodule update --recursive

cp ~/.s3cfg .
mkdir -p ./.aws
cp ~/.aws/credentials ./.aws/


vagrant box update
vagrant box outdated --machine-readable | grep outdated
box_needs_update=$?

echo "First we check if we need to update our box."
if [ "$box_needs_update" -eq "0" ]; then
    echo "We have an outdated box. Need to destroy VM to load"
    echo "the new box."
    # We have to update all plugins when we get a new box version.
    vagrant plugin expunge --reinstall --force
    vagrant destroy -f
fi


echo "Then we make sure the right plugins are installed"
vagrant plugins list | grep -q vagrant-vbguest || vagrant plugin install vagrant-vbguest

echo "about to vagrant up"

time vagrant up
if [ -e reboot-required ]; then
    echo "VM needs a reboot. Doing that..."
    rm reboot-required
    time vagrant reload
fi
time vagrant provision

export machinename=$(basename `pwd` | sed 's/\./-/')
echo "Setting machine name to $machinename"
vagrant ssh -c "sudo hostnamectl set-hostname $machinename"
