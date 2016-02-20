Title: A Good BASH Script Template
Date: 2015-02-09 21:00
Tags: BASH, Programming

I start out all my BASH scripts with the following boilerplate:

    :::bash
    #!/bin/bash
    set -e
    set -o pipefail
    set -u

Let's talk for a minute about why each one of those lines is a good idea.

set -e: Exit immediately if a simple command exits with a non-zero status. If the command is part of an if or while or until command, or is used with && or ||, it doesn't exist immediately. This is incredibly useful if you have a script that's a list of commands, and you don't want to have error checking after each line, but you do want to exit the script with an error if one of the commands fails.

set -o pipefail: In a vanilla BASH script, as long as the last command in a pipeline exits successfully, the pipeline is treated as though every step in it succeeded. You probably don't want that. This setting means that if any step in a pipeline fails, it's treated as an error.

set -u: Treat an unset variable as an error, and exit. This is HUGELY important. Here's an example that actually happened to someone:

The script removed everything below a directory:

    :::bash
    rm -rf ${SCRIPTDIR}/

However, $SCRIPTDIR was not set, so the script removed everything starting at the root directory. if the script's author had done a "set -u," then the script would have exited at that line with an error instead of attempting to delete everything on the system.
