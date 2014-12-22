Title: Linux From Scratch
Date: 2003-10-12 01:20
Author: schof
Category: Linux/Unix, Technology
Slug: linux-from-scratch-2

Worked on Linux From Scratch today. Did pretty well. Ran into a problem
in Chapter six with creating the chroot environment. It reported that
the /static/bin/env file didn't exist when it clearly did. Googled on
LinuxFromScratch.org and found out that one of my packages probably
wasn't compiled right. Found out which package contained env and
recompiled, and voila; I'm in chroot.

Next step is changing ownership of /static, but every attempt gives me
this: **"bash: /static/bin/chown: No such file or directory."** Turns
out I needed to recompile fileutils, as it wasn't compiled statically.
Some of the articles I've Googled say to use "ldd " to determine whether
or not the file uses dynamically linked libraries. That's how I found
out I needed to recompile chroot and chown. I did a "ldd
\$LFS/static/bin/\*" and it turned out a bunch of files were not linked
statically. I'm not sure why. I was very careful with each command, but
obviously I wasn't careful enough. I'm going to go through all files in
\$LFS/static now and make sure each is compiled statically.

I've started writing scripts for everything I do, rather than typing on
the command line. If I record everything in scripts, it makes it much
easier to change when I make mistakes, and I could eventually meld them
together into one huge meta-script that did a complete LFS install. I
just started doing that, so I don't have the whole process recorded --
but it wouldn't be too much trouble to go back and redo the first five
chapters. I'm discovering a real aversion to typing the same thing more
than once, and these script files help me with that. I wish I had been
doing it from the beginning.

<div class="blogger-post-footer">

<img alt width="1" height="1"></img>

</div>
