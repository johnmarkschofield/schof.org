Title: Linux From Scratch
Date: 2003-10-07 23:20
Author: schof
Category: Linux/Unix, Technology
Slug: linux-from-scratch

I got interested in a project called [Linux From
Scratch](http://www.linuxfromscratch.org/) (LFS) about a year ago, going
so far as to have a copy place print out the 4.0 version of the book.
Never really did anything about it, though. This weekend I started
working on the 4.1 version, working on the website while I waited for
stuff to compile. It's pretty cool. The best way analogy I've found is
automobiles; building a Linux From Scratch system is like building a car
from parts. I'm compiling from source every single file that's needed
for the system, I'm writing configuration files (or at least, I will
be) -- in short, I'm putting the entirety of the operating system
together.

I'm still in the compiling things in static mode stage -- meaning that
there's a whole lot more work to do. I've only run into a couple of
problems the book didn't prepare me for. The book said to use cfdisk to
partition the hard drive for the LFS installation; cfdisk isn't
installed in Red Hat 8. I tracked down an RPM to install it, and got it
to work but couldn't figure out how to use it, at least well. (It
required you to input partition sizes in a way that required that you
know exactly what you want to do before you do it. Since I was making
stuff up as I went along, I ran into trouble.) I tried fdisk (I've used
the same-named but different MS-DOS version of this program many times)
and I was able to figure it out without trouble. The next problem was
that two libraries I needed, libcurses.a and libncurses.a, were not
present. I had to track down the right version of the development
version of the package, but I did and got it to work. Two steps forward;
one step back. That's teaching yourself LInux. I'll keep you posted as
the project progresses.

<div class="blogger-post-footer">

<img alt width="1" height="1"></img>

</div>
