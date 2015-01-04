Title: Seamless SSH
Date: 2008-06-09 11:59
Tags: linux, os x, obsolete

I'm transitioning my daily work desktop from OS X Leopard to Kubuntu
Hardy. (I'll be writing more about that in the future.) My job is split
between managing people and doing development and system administration
for a bunch of Ubuntu boxes, so running the same platform that I'm
administering makes a lot of sense. I DO miss some of the fit-and-finish
of OS X, though, and I haven't completely transitioned over to Linux for
everything.

Ssh-agent is a great program that lets you add the password to your SSH
private key to memory, and then you don't need to type in the ssh key
passphrase every time. The basic usage is that you start BASH as a child
of ssh-agent, and then use a program called ssh-add to prompt you for
the password and store it in memory.

On OS X, there's a GREAT program called SSHKeychain that handles this,
storing the password in your OS X keychain, so it's really seemless.

On Linux, you need to type in "ssh-add" manually every time you want to
store the key, and after that your SSH sessions will be seamless.

However, I'm always forgetting to do that, and thus getting prompted for
the password. Too many seams. I added the following code snippet to the
end of my .bashrc file, and thus, every time I open a bash shell, it
checks whether ssh-agent has any keys in memory. If it does, the shell
starts as normal. If ssh-agent doesn't have any keys in memory, it
prompts you for the password. Simple, and as seamless as I can make it.

    :::bash
    ## Add key to ssh-add if it has not been added.

    ssh-add -l &> /dev/null
    SSHADDRESULT=$?
    if [ "$SSHADDRESULT" -ne "0" ]; then
        ssh-add
    fi


**UPDATE 2008-07-02**: Here's a much more succinct way of writing that:

    :::bash
    ssh-add -l &>/dev/null || ssh-add
