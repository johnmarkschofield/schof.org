Title: Rimage
Date: 2004-05-10 00:18
Author: schof
Category: OS X, Technology
Slug: rimage

I'm working full-time now as head geek at a large photo lab in Los
Angeles. We've been burning customer files to CD and DVD, then
handwriting customer information on the disk with Sharpies. This seems
pretty unprofessional to me, so one of my first moves was to find some
better way of doing things. After some research and calling a few
people, I decided to get an evaluation copy of a
[Rimage](http://www.rimage.com/) CD / DVD burner.

In my first week on the job I convinced Advanced Tek Rep (ATR) to loan
us a Rimage Protege II with an Everest II CD label printer. The hardware
on the Protege is impressive -- rock solid and well-designed. The
Rimage's ability to burn CDs consistently and in great numbers is
impressive, and the full-color labels (actually printed directly on the
CD, not on a label) are frankly beautiful. There isn't anything else on
the market like it.

It's hard to believe the software comes from the same company. Rimage's
suite of six different programs seem poorly designed and implemented --
patched together from bailing wire, chewing gum, and hope.

Rimage claims their products are Macintosh-compatible, but once you try
using their software in a Macintosh environment you quickly learn that
they are not. It truely seemed at times that the Rimage software
development team didn't even own a Mac.

My guides through all this madness was Tony Lanzi and Tony Cahill at
ATR. Though they seemed to be a little new at the Macintosh, they were
determined to get me up and running. Because the Rimage was a loaner
from ATR, the Tonies worked long hours on the phone and on-site trying
to solve the problems I'll detail below. Each Tony put in dozens of
hours, all of it on ATR's dime -- didn't cost me a cent. Five weeks
after it was first installed, the Rimage is up and running, and being
integrated into our shop's workflow. I'm reasonably pleased with the
outcome, though I'm frustrated it took as long as it did. This is why it
took so long:

I thought in looking through Rimage's literature that the best way to
set this up was to install Rimage's Java-based burning client on a Mac,
and connect that to the PC-based Rimage Control Center (a Windows 2000
Professional box from Dell). Turns out that the Rimage software requires
a shared volume to be created both on the Macintosh and on the PC and
the burning client on the Mac only sends the request to the PC; the PC
actually creates the image from files on the shared volume on the
Macintosh.

We quickly encountered a problem with Macintosh type-and-creator issues.
SMB or CIFS, the Windows file-sharing solution, doesn't recognize
Macintosh [resource forks](http://www.macdisk.com/macforken.php3). This
means that burned CDs open fine on PCs, but open without preview
thumbnails on Macintoshes, and can not be opened by double-clicking.
(They are PhotoShop files; our clients expect them to open when
double-clicked in Photoshop rather than Preview.)

Rimage was very little help on this issue. ATR spent almost three weeks
working on this issue before they finally figured out how to resolve it.
It's impossible with only Rimage software, but it turns out if you
install [Dave](http://www.thursby.com/products/dave.html) on a Macintosh
and share the files you want to burn via Dave, the PC Control Center can
mount the network share, burn the files to CD, and create a proper, PC
and Macintosh-compatible, fully previewed CD-ROM or DVD-ROM. We never
did get the Macintosh client working properly, but the PC client can
select the files on the shared volume on the Macintosh and create
Macintosh-compatible disk images.

How it's possible that Rimage claims to be Macintosh-compatible, but in
reality can only achieve that by adding third-party software boggles the
mind. The mind boggles still further because Rimage didn't realize that
Dave was needed until two weeks into the trouble-shooting process -- I
have to assume they spouted that "Macintosh-compatible" bullshit without
ever testing that it actually worked.

It turned out that this major hurdle was far from the last in this long
process. Once ATR in combination with Rimage figured out how to keep the
type-and-creator information correct on CDs and DVDs, we ran into more
problems.

Rimage has two main interfaces for creating CDs -- QuickDisk, which has
a fairly intuitive, easier interface, and CD-R Workstation, which is
older, no longer supported by Rimage, and much less intuitive. Two
servers run on the PC Rimage Control Center, an Imaging Server that
creates CD image files, and the Production Center, which controls CD and
DVD burning and label-printing. QuickDisk worked wonderfully for CDs,
but it turned out that Rimage left out of QuickDisk the ability to
create Macintosh-compatible DVDs.

So Rimage told us to use CD-R Workstation, their no-longer-supported
burning client, but it turned out that the Imaging Server would choke if
asked to create a CD or DVD image with subdirectories on it. We spent
about two more weeks troubleshooting that, before the third version of
an updated binary from Rimage fixed the problem.

I've got to give a thumbs-up to ATR for successfully holding Rimage's
feet to the fire on these issues, and actually getting them to create a
resolution. ATR also put so many hours into this project that they
unquestionably blew any profit margin they had on the machine -- yet
they never charged me a dime for all their work getting this going.

So now we've developed and documented a workflow, (using just CD-R
Workstation) and our production people are trained in it -- and we're
starting to use the Protege on a daily basis. Despite my lingering
feelings of bitterness towards Rimage, I'm happy with what we have --
the Rimage makes beautiful disks.

