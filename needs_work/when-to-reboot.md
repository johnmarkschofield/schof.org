Title: When to Reboot
Date: 2005-03-18 23:02
Author: schof
Category: Technology, Troubleshooting
Tags: computers, repair, troubleshooting, windows
Slug: when-to-reboot

Someday, people will read this essay and lack the context to understand
it — their hardware and software will work reliably. Until that day
comes, the information in this essay will be valuable.

Standard advice to people experiencing computer problems is to reboot.
I've known technicians who refuse to even listen to a question if people
haven't rebooted. It's simply amazing how many problems in the Windows
world can be fixed that way. Modern PCs like to be rebooted every couple
of days or so — it used to be daily, with Windows 98, so at least it's
gotten a little better. No sysadmin I know lets a Windows box go longer
than a month without rebooting under any circumstance. Macintosh OS 9
systems have similar traits, although OS X machines seem to share the
tolerance for upatime of their unix predecesors. Still, even on Linux
and Macintosh boxes, the occasional reboot solves all kinds of problems.
(If you're savvy enough to object that a reboot destroys valuable
forensic evidence that lets you identify the cause of the freeze, you're
right -- but you're also savvy enough to figure out when to reboot on
your own. This essay isn't written for you.)

Still, there's some things about rebooting you need to keep in mind.
First of all, it's not a panacea. There's many things it can't fix. Many
more are fixed only temporarily by a reboot — if you're having to reboot
three times a day, it's time to get someone in there who knows what
they're doing to take a look at the thing. (In a later article, I'll
explain enough of the troubleshooting process that you can be that
person.)

There's times when you shouldn't be too quick to reboot, either. Some
processes can take a while to complete. This is especially true if your
computer is connected to a network. There are no hard-and-fast rules,
and in some very specific conditions you would wait much longer, but in
general five minutes is long enough for your computer to do just about
anything. I'm speaking here of waiting for your computer with no visible
response — if your computer has a moving progress bar, I never reboot
unless the wait time is much, much, much longer than than my experience
tells me it should be and the program doesn't respond to a cancel
command.

Telling whether a computer is frozen or merely working hard (or staging
a dramatic pause) can be difficult, even for advanced techs. One trick
is to look at signs on the computer other than the video display.
(Assuming that the video display appears frozen.) Can your hear the hard
drive or CD drive spinning? Regular whining of the drive spinning idly,
or the irregular sound of the drive mechanism seeking data? Flickering
activity LEDs on the front of the case for hard drives and CD drives,
and other disks? Ones on the back for network or other activity lights?
Some people claim they can hear the sound of electricity going through
the motherboard. (I could have sworn there was an article on SlashDot?
about this. Anyone remember seeing anything? It was about using the
sound made by electronics to aid cryptanalysis.)

In noisy environments I've been able to tell by putting my hand on the
computer itself and feeling the vibration of the hard or CD drive.
(Doesn't work with every case.) Sometimes when trying to boot a computer
from a CD I'll be able to hear whether it's booting from the hard drive
or from the CD as intended. If the computer gets really frozen the Caps
Lock (and Num Lock and Scroll Lock, if present) LEDs on the keyboard
won't change when you hit the corresponding key. That means reboot for
sure. For the borderline cases, wait five minutes longer than you think
you should and reboot.

