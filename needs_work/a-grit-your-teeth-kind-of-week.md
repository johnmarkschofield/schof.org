Title: A grit-your-teeth kind of week
Date: 2005-11-11 21:22
Author: schof
Category: System Administration, Technology, Troubleshooting
Slug: a-grit-your-teeth-kind-of-week

It was a grit-your-teeth kind of week.

The task before me seemed simple. Install backup software on a server so
that we can back up our other servers to our Overland LTO2 tape jukebox.

Well, the software we spec'd out was BRU, from Tolisgroup. We needed to
install it on already-purchased hardware, an IBM x306 server.

Not all linuxes are compatible with BRU, and not all linuxes are
supported by IBM -- I tried to install my personal favorite server
distro, Debian -- and couldn't get the mirrored boot drive to work --
and IBM was no help, since they don't support Debian.

SuSE Linux is supported on IBM hardware. And the BRU guys said SuSE was
a great linux, and BRU was very stable on it.

Solution found. Order SuSE, install it, and install BRU. Well, SuSE
loved the IBM hardware -- found the boot RAID, found all hardware, and
worked right off the bat.

Got BRU installed, and ran into a bunch of minor problems -- for
instance, the way it handles e-mail is quirky. You enter an e-mail
address to send reports to, and it connects to the SMTP server for the
destination address and tries to send a message. There's no way to
configure authentication, and no way to change the "from" address in the
message -- in my case, it was bru-server@bru.dakim.com, which is not how
I would have liked it. Annoying, but not a deal-breaker.

What turned out to be a deal-breaker was reliability -- the reason we'd
chosen BRU on linux in the first place. We started getting "sense
errors" where BRU would be able to do one backup session, but would not
be able to do another one until the server had been rebooted.

BRU blamed that on SuSE's stock 2.6.5 kernel -- said SuSE shipped a
kernel with poor SCSI support. (Which was kind of frustrating, because
we bought the damn thing on their recommendation.) So I compiled the
latest kernel, a 2.6.14, and that seemed to solve the problem -- I
configured BRU to back up all our servers and desktops -- and the next
day I was getting sense errors again. Sometimes after the first backup,
sometimes after several backups -- but it never got to the point where
it was reliable.

BRU was little help on this one -- kept going in circles trying the same
things, and then they attempted to solve the problem by throttling down
the speed of our SCSI card -- not a great solution from a speed
perspective, and even less attractive because it didn't solve the
problem.

So we decided to punt. We got the first sense error November 4. Here it
was the 11th, and still no love. We got an evaluation copy of Dantz
Retrospect (runs on Windows) and we had an unused legit copy of XP
laying around, so I wiped the system and attempted to install XP. Well,
IBM only supports server-level OS's on their systems -- so I was
completely unable to get it to recognize the boot RAID, and even after
splitting the boot RAID into individual drives, which made installation
possible, I couldn't get the Broadcom network hardware recognized in
Windows. IBM's site directed me to three different driver packages for
the NIC -- I tried all three, and none of them seemed to work.

I've been running production servers under Windows since I switched my
DOS-based BBS from Desqview to a beta version of Windows 95. (It was an
improvement.) I am GOOD at getting recalcitrant Windows drivers to
behave. I'm stumped. We may have to buy a Windows 2003 Server license --
on top of the money we've already blown on SuSE linux and BRU -- if I
can't get this damn NIC working. I'll be talking with IBM support on
Monday, so we'll see then. They weren't able to do much to get the boot
RAID working, but hopefully a NIC is a little simpler.

Maybe I'll take up gardening. Or woodworking. I like the smell of
sawdust.

