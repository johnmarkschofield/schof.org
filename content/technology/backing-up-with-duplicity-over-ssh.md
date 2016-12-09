Title: Backing up with Duplicity over SSH
Date: 2008-07-03 15:06
Tags: backup software

I'm attempting to set up [Duplicity](http://duplicity.nongnu.org/) as a
backup tool, running from cron over ssh, to backup my home directory to
another server.

I of course already have password-less SSH set up to connect to that
server, and use ssh-agent to store the passphrase for my SSH key, [as
described in another
entry](/2008/06/09/seamless-ssh "Seamless SSH").
However, I could not get password-less SSH to work from a cron job. If
anyone has tips on how to do that, I'd love to hear it.

So I created a second SSH public/private key pair with no passphrase,
(in \~/.ssh/backup and \~/.ssh/backup.pub) and figured out how to have
Duplicity call ssh, scp, and sftp with the correct parameters to specify
the new key pair. (There's about a zillion different ways of specifying
that, and only ONE that works across all three programs.)

The passphrase mentioned here is the one used to encrypt the duplicity
backups.

    :::bash
    PASSPHRASE='YourPassphraseGoesHere' duplicity \
        --no-print-statistics \
        --ssh-options "-oIdentityFile=/home/schof/.ssh/backup" \
        /home/schof \
        scp://johnmarkschofield@example.com/duplicity
