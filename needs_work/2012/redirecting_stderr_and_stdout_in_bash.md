Title: Redirecting STDERR and STDOUT in BASH
Date: 2012-04-20 19:13
Author: schof
Category: Linux/Unix, OS X, Shell Scripting, System Administration, Technology
Tags: BASH, command-line, Linux, OS X, POSIX, scripting, Unix
Slug: redirecting_stderr_and_stdout_in_bash

One of my clients (a Mac-based computer consulting company here in Los
Angeles) had a BASH script they wanted me to look at -- a couple of
things weren't working the way the client thought they should be
working.

The client's issues are resolved, but I noticed something in the script
that I wanted to dig into further. They were redirecting STDOUT and
STDERR to a file like this:

``` {lang="bash"}
command_to_execute &> logfile.txt
```

This is a wonderfully efficient (in terms of characters typed) and clear
way of doing the redirection. It's much more elegant than the way I
normally do this type of redirection:

``` {lang="bash"}
command_to_execute > logfile.txt 2>&1
```

Let me briefly break down what each of the above commands are doing, and
then I'll explain why the way I do it (despite being ugly) is better
than the elegant way in most cases.

Command-line programs running under Linux and Unix (including OS X)
output to either STDOUT (for standard output) or STDERR (for error
output). When you're running a command interactively on the terminal,
you see both STDOUT and STDERR together, and in fact, you can't tell
visually what output comes from STDOUT and what comes from STDERR.

When you want to save output to a file, though, you have choices.
Redirecting with just a \> gets just STDOUT. The following will save
STDOUT to the log file and print STDERR output on the screen:

``` {lang="bash"}
command_to_execute > logfile.txt
```

The following will save STDERR to the log file and print STDOUT on the
screen:

``` {lang="bash"}
command_to_execute 2> logfile.txt
```

But what if you want to redirect BOTH STDERR and STDOUT to the log file?
Using the &\> notation is certainly less typing, but it only works in
BASH versions since 4. My web host running FreeBSD has version 4.0.35
(so &\> would work) but my OS X desktop running Mountain Lion has
version 3.2.48, so the &\> trick wouldn't work. It also doesn't work in
sh, Dash, or most shells except recent versions of BASH.

What I do is, first, use a single \> to redirect STDOUT to a file, and
then use 2\>&1 to redirect STDERR to STDOUT. This works in every shell
I've tested it in, from old versions of sh to dash, BASH, and others.
It's a little more to type, and you really have to memorize it because
it's not an intuitive syntax, but once you do it's almost as easy to use
as &\>.

My reference for this, as it usually is for BASH scripting issues, was
the most excellent [Advanced Bash-Scripting
Guide](http://tldp.org/LDP/abs/html/io-redirection.html "Advanced BASH-Scripting Guide, IO Redirection Chapter").

