Title: Working Around VirtualBox Bug 12879
Date: 2014-03-31 11:24
Tags: Vagrant

If you're using [Vagrant](http://www.vagrantup.com/) and you've upgraded
to the latest version of [VirtualBox](https://www.virtualbox.org/)
(4.3.10 as of March 25, 2014), and you've got
[vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest)
installed (as you should) then you've undoubtedly run into a nasty bug:

    default: /vagrant => /YOUR_VAGRANT_DIRECTORY
    Failed to mount folders in Linux guest. This is usually because
    the "vboxsf" file system is not available. Please verify that
    the guest additions are properly installed in the guest and
    can work properly. The command attempted was:
    mount -t vboxsf -o uid=`id -u vagrant`,gid=`getent group vagrant | cut -d: -f3` /vagrant /vagrant
    mount -t vboxsf -o uid=`id -u vagrant`,gid=`id -g vagrant` /vagrant /vagrant

This turns out to be[a bug in the latest version of
VirtualBox](https://www.virtualbox.org/ticket/12879).

The workaround, per that bug ticket, is to issue this command after
SSHing into your virtual machine:

    :::bash
    sudo ln -s /opt/VBoxGuestAdditions-4.3.10/lib/VBoxGuestAdditions /usr/lib/VBoxGuestAdditions

That does work. However, I wanted to make this a little more automated,
as at the moment I'm creating Virtual Machines as examples, and I want
it to be as seamless as possible. I made my Vagrantfile look like this:

    :::ruby
    # -*- mode: ruby -*-
    # vi: set ft=ruby :

    # Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
    VAGRANTFILE_API_VERSION = "2"

    # Provide fix for Bug 12879 in VirtualBox: https://www.virtualbox.org/ticket/12879
    $fix12879 = <<SCRIPT
    if [ -e /opt/VBoxGuestAdditions-4.3.10/lib/VBoxGuestAdditions -a ! -h /usr/lib/VBoxGuestAdditions ]; then
        # If we're on version 4.3.10 of Guest Additions AND we haven't created the symlink:
        ln -s /opt/VBoxGuestAdditions-4.3.10/lib/VBoxGuestAdditions /usr/lib/VBoxGuestAdditions
        echo "Working around bug 12879 in VirtualBox. Next do a vagrant reload --provision'"
        exit 1
    fi
    SCRIPT

    Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    config.vm.provision "shell", inline: $fix12879
    config.vm.provision "shell", path: "bootstrap.bash"

    end


The steps to take, then are:

    :::bash
    vagrant up
    # See the error about vboxsf
    vagrant provision
    # See the message about running "vagrant reload --provision"
    vagrant reload --provision

I'd love to get this even more automated -- as one or two steps instead
of three. If you have any ideas for how to do that, [please get in touch
with me](/contact).

