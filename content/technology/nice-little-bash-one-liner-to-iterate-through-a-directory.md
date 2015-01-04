Title: Nice little BASH one-liner to iterate through a directory
Date: 2008-04-29 14:23
Tags: command line

    :::bash
    for afile in /home/auser/adirectory/*; do echo $afile; done

Useful for all kinds of things. And I can never remember how the syntax
changes between doing a for statement in a bash script and doing it as a
one-liner on the command line.
