Title: Fixing OS X ACL Entries for Deleted Users
Date: 2013-08-29 18:56
Tags: consulting, OS X

I had my favorite kind of consulting gig recently -- a friend who runs a
consulting company called, and said he had a problem his guys couldn't
figure out. I love being tech support for other smart geeks!

It's pretty hard to find a solution to this on Google, so I figured I'd
write it down for anyone else in this situation.

A client of my friend's had an OS X file server with very complicated
ACLs ([Access Control Lists](http://support.apple.com/kb/PH8010)) on
each file and directory.

They had created ACL entries for many individual users, and then had
removed those users from the system as they left the company, got
transferred, etc. You can list ACLs with "ls -le". Here's a sample of a
broken one:

    :::bash
    $ ls -le -rw-r-----+ 1 schof staff 0 Aug 27 14:27 testfile 0: ADFB6DAF-96D1-4F78-8A16-4CBF465EC283 allow read

You can see the user name has been replaced with a GUID.

Normally to remove an ACL entry you would use "chmod -a". That doesn't
work when the username has been replaced with a GUID:

    :::bash
    $ chmod -a "ADFB6DAF-96D1-4F78-8A16-4CBF465EC283 allow read" testfile
    chmod: Unable to translate 'ADFB6DAF-96D1-4F78-8A16-4CBF465EC283' to a UID/GID`

My friend was stuck. I figured out that you could use the =a# option to
chmod to change a particular ACL line. You can use this to change the
GUID line to a valid ACL line, and then use "chmod -a" to remove the
fixed line:

    :::bash
    $ ls -le total 0 -rw-r-----+ 1 schof  staff  0 Aug 27 14:27 testfile 0: ADFB6DAF-96D1-4F78-8A16-4CBF465EC283 allow read

    $ chmod =a# 0 "schof allow read" testfile

    $ ls -le total 0 -rw-r-----+ 1 schof  staff  0 Aug 27 14:27 testfile 0: user:schof allow read

    $ chmod -a "schof allow read" testfile

    $ ls -le total 0 -rw-r-----  1 schof  staff  0 Aug 27 14:27 testfile

That takes care of the problem nicely.

Of course, my friend's client had tens of thousands of files that had
this problem, so fixing it manually was not an option. I wrote him a
script that checked for GUID ACL entries, and then removed them using
this method. Worked like a charm!
