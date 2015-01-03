Title: File "Created Date" Under OS X -- Harder Than You Think
Date: 2009-04-11 14:28
Tags: OS X, programming, consulting

A client had an OS X server with tens of thousands of files in a
directory tree, and wanted to move some of them based on their creation
date. I put together a Python script that worked perfectly on my test
system, but failed in production. (I put in a "--dryrun" option, so no
harm was done.)

The modification date the script reported was correct, but the creation
date the script reported was different from the creation date that doing
"Get Info" in the OS X Finder reported. Hmm. Not good. I did some
investigating.

Let's look at a test file. The Finder reports the following creation and
modification dates:

    Created: Monday, April 10, 2006 17:04
    Modified: Thursday, April 13, 2006 15:54

Python reports a different creation date and the same modification date:

    :::python
    >>> import os.path
    >>> import time
    >>> stamp = os.path.getctime('datetest.txt')
    >>> time.ctime(stamp)
    'Fri Apr 10 15:51:10 2009'
    >>> stamp = os.path.getmtime('datetest.txt')
    >>> time.ctime(stamp)
    'Thu Apr 13 15:54:43 2006'

Hmmm. What does "ls" in the Terminal report? The standard "ls -l"
reports creation date. Adding "-T" makes it report the full date in all
cases. And "-c" counter-intuitively means "display modification date."

    :::bash
    $ ls -lT datetest.txt
    -rwxr-xr-x@ 1 schof  schof  2448091 Apr 13 15:54:43 2006 datetest.txt
    $ ls -lcT datetest.txt
    -rwxr-xr-x@ 1 schof  schof  2448091 Apr 10 15:51:10 2009 datetest.txt

The plot thickens. The modification date matches the Finder and Python,
but both Python and ls are reporting an incorrect (according to the
Finder) creation date.

Quite a bit of Googling showed me the
"[mdls](http://developer.apple.com/documentation/Darwin/Reference/Manpages/man1/mdls.1.html)"
tool -- or "metadata ls." Very useful. This shows the complete set of
metadata for a file. Including the OS X creation date. Actually, two
creation dates, one for the file, and one for the file content. (I'm not
sure what circumstances would make those creation dates differ. The
[documentation I've been able to
find](http://developer.apple.com/macosx/spotlight.html) has been unclear
and
[contradictory](http://developer.apple.com/documentation/Carbon/Reference/MetadataAttributesRef/Reference/CommonAttrs.html).)

    :::bash
    $ mdls datetest.txt
    kMDItemContentCreationDate     = 2006-04-10 17:04:34 -0700
    kMDItemContentModificationDate = 2006-04-13 15:54:43 -0700
    ...
    kMDItemFSContentChangeDate     = 2006-04-13 15:54:43 -0700
    kMDItemFSCreationDate          = 2006-04-10 17:04:34 -0700
    ...
    kMDItemLastUsedDate            = 2009-04-11 11:48:03 -0700
    kMDItemUsedDates               = (
    2009-04-11 00:00:00 -0700
    )

Now that we've got all that information, what does it tell us? The
Unix/Linux standard for "creation date" is to show you the date on which
a particular file was created. If you copy file "a" to file "b," those
are two different files, and the "creation date" for file "b" will be
the date you made the copy.

OS X metadata travels with the file, so if you copy file "a" to file "b"
using ditto on the command-line or using the Finder, the Unix creation
date will be the date the copy was done, but the OS X creation date of
file "b" will be the same as file "a."

There's good arguments for handling "creation date" the Unix way, and
there are good arguments for doing "creation date" the OS X way, but
mixing them as OS X does is kind of frustrating.

I've written a quick-and-dirty Python example script that reports the
Unix creation date and the OS X creation date for any particular file.
Since it's released under the open-source MIT license, feel free to use
it in your own programs. You can [find it on
github](https://github.com/johnmarkschofield/getcreationdate/blob/master/getcreationdate.py "Get Creation Date Script in Python").
