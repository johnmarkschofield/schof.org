Title: Terminally Incoherent's "Linux Fuckup Of The Day" -- Using Single-User Mode To Recover
Date: 2007-06-25 12:34
Author: schof
Category: Uncategorized
Slug: terminally-incoherents-linux-fuckup-of-the-day-using-single-user-mode-to-recover

From [Terminally
Incoherent](http://www.terminally-incoherent.com/blog/2007/06/25/linux-fuckup-of-the-day/ "Terminally Incoherent's Linux Fuckup Of The Day"):  

> Yep. I just removed myself from all the groups except for *vboxusers*.
> Brilliant! I absolutely hate when I do stupid shit like that. It’s not
> like this was hard to fix - I just didn’t remember of the top of my
> head what groups I was supposed to belong to. Of course since I was no
> longer part of the *sudo* and *admin* groups I could no longer
> <kbd>sudo</kbd>. Luckily enough, back in the day I decided to enable
> the root password. So I was able to <kbd>su</kbd> to become root, and
> then usermod myself to *admin*, and bunch of other groups I needed
> like audio, video, tty, lp and etc… I wonder what would happen if I
> did this on a default Ubuntu box without root account. I wonder if I
> would be able to recover from this that easily.
> </p>

The short answer is "Yes, you would." Single User Mode is your friend.
At bootup, hit ESC to get into the Grub menu, and select recovery mode.
If you haven't entered a root password, recovery mode will dump you to
the console as root. If you HAVE defined a root password, recovery mode
will dump to a login prompt, where you'll have to enter the password.

