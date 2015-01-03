Title: Another Nice Little One-Liner; Wait Until a File is There (or not There)
Date: 2008-09-18 17:55
Tags: command line

This is the sort of thing that's second nature to a command-line geek,
but I thought it was cool enough (in its little way) to share.

The problem: I have a process that runs on a remote server for quite a
while. I wish to be alerted when it completes. As long as it's running,
it creates a lockfile in /var/lock. So when the lockfile goes away, I
want to be alerted.

The solution:

__Part 1__: In my .bashrc file, I've aliased the command "alert" to play a
sound: (This works only on Linux. I'm sure you could do something similar
on OS X.)

    :::bash
    alias alert='aplay /usr/share/sounds/k3b_success1.wav'

But of course, I can only play that on my local machine -- does me no
good to sound an alarm on a computer in the server room, even if it had
speakers.

__Part 2__: I can create a "while" one-liner that waits until the file is
deleted, then executes the next line:

    :::bash
    while [ -e ~/lockfile ]; do sleep 10; done; alert

However, this can only test against files on my local system. This
brings me to...

__Part 3__: You can use ssh to run a command on a remote system, instead of
just logging into the remote system:

    :::bash
    ssh user@example.com "while [ -e /var/lock/program.lock ]; do sleep 10; done" ; alert

It runs the while loop on the remote system, not giving back control to
the local system until the while loop exits (which happens when the lock
file no longer exists). Once the while loop exits, ssh exits, and we run
the "alert" command, which plays a sound alerting me to the change.
