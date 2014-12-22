Title: Another nice little one-liner; wait until a file is there (or not there)
Date: 2008-09-18 17:55
Author: schof
Category: Linux/Unix, Shell Scripting, System Administration, Technology
Tags: BASH, scripting, Secure Shell, SSH, system administration
Slug: another-nice-little-one-liner-wait-until-a-file-is-there-or-not-there

This is the sort of thing that's second nature to a command-line geek,
but I thought it was cool enough (in its little way) to share.

The problem: I have a process that runs on a remote server for quite a
while. I wish to be alerted when it completes. As long as it's running,
it creates a lockfile in /var/lock. So when the lockfile goes away, I
want to be alerted.

The solution:

Part 1: In my .bashrc file, I've aliased the command "alert" to play a
sound:

``` {lang="bash"}
alias alert='aplay /usr/share/sounds/k3b_success1.wav'
```

But of course, I can only play that on my local machine -- does me no
good to sound an alarm on a computer in the server room, even if it had
speakers.

Part 2: I can create a "while" one-liner that waits until the file is
deleted, then executes the next line:

``` {lang="bash"}
while [ -e ~/lockfile ]; do sleep 10; done; alert
```

However, this can only test against files on my local system. This
brings me to...

Part 3: You can use ssh to run a command on a remote system, instead of
just logging into the remote system:

``` {lang="bash"}
ssh user@example.com "while [ -e /var/lock/program.lock ]; do sleep 10; done" ; alert
```

It runs the while loop on the remote system, not giving back control to
the local system until the while loop exits (which happens when the lock
file no longer exists). Once the while loop exits, ssh exits, and we run
the "alert" command, which plays a sound alerting me to the change.

Took me about 10 times longer to write up than it did to implement. But
it's the sort of thing you can just throw together quickly on a \*nix
system to make your life easier.

