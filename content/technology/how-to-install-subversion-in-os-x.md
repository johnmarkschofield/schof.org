Title: How To Install Subversion in OS X
Date: 2007-03-04 17:28
Tags: os x, obsolete

The folks behind [Subversion](http://subversion.tigris.org) don't
produce an OS X binary, so they link to [a third party who produced
one](http://metissian.com/projects/macosx/subversion/). Unfortunately,
the current regular version is 1.4.3, and the latest OS X binary is 1.3.

I found a different binary at [Martin Ott's
site](http://www.codingmonkeys.de/mbo/articles/tag/subversion). I have
no idea why his site isn't linked from Subversion's, but his binary is
1.4.3, the latest.

Simply run the installer in his package, and it will do ALMOST all
that's needed. However, you still won't be able to run svn from the
command-line, because the package installs it in /usr/local/bin, and
that path isn't in Apple's default.

For those new to the terminal, the path variable is a list of
directories where OS X should look for applications. This applies only
to the command line. For instance, if you type "ls" on the command line,
it will look for the "ls" program in each directory listed in the path.
Since it finds it in /bin, it will run ls. The path is why running "ls"
is the same as running "/bin/ls".

To find out what your path is currently, enter the following command:

    :::bash
    echo $PATH

(Capitalization does matter.)

To add /usr/bin/local to your path, copy and paste the following line
into your terminal:

    :::bash
    echo "export PATH=$PATH:/usr/local/bin" \>\> \~/.profile

This will not affect the shell you're running now, so type "exit" to
leave the shell. Then hit CMD-N to get a new terminal, and type "svn"

You should get a message telling you to type "svn help" for more
information. Success, svn is installed and configured properly.

