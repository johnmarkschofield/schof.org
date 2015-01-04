Title: Resolving a Very Uninformative Debootstrap Error Message
Date: 2006-05-22 13:02
Tags: linux

So I'm trying to do an install with debootstrap onto a virgin partition.
From my custom Ubuntu-based distribution. And I get the following error
message:

    E: Couldn't find these debs: 33024830

The error code itself is **not** Googleable, because it apparently
changes for each install. (I got several different codes during the
course of my troubleshooting.) Google got me
[here](http://wiki.xensource.com/xenwiki/DebianDomU), where I learned
that the "--resolve-deps" option was the secret. Appears to be working --
at least, I'm much farther along in the process without failing.

