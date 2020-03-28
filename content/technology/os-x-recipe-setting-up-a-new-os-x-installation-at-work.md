Title: OS X Recipe: Setting up a New OS X Installation at Work
Date: 2012-08-01 22:28
Tags: os x, productivity

I installed a new hard drive in my work computer, and I'm taking this
opportunity to do a clean install of OS X. And I'll be documenting that
here, both for myself and because my choices may be instructive to some
of you.

I have a Mac Pro from 2006 with dual-core Xeons, 6 GB RAM, and a 250 GB
7200 RPM drive. I replaced the drive with a new 10k RPM hard drive
because my system was dog slow whenever I tried do something
disk-intensive, such as run a Windows virtual machine. Since I'm now
doing a lot of Windows testing, that became a problem.

For the clean install, I booted off a Snow Leopard installation
DVD. Once you select the language, go to Disk Utility and repartition
the hard drive as a single partition. (Give it a more descriptive name
than "Macintosh HD." I called mine "Startup," but "Bob" would also
work -- if you'll remember what computer "Bob" is.) Choose a custom
install, and deselect the extra languages and language fonts (unless
you're going to use one of those languages.) Simmer slowly while it
installs. Once it's installed, apply all updates. Apply them again.
Apply them until there's no more to be applied. Set the system to NOT
auto-login. Let's not just invite the world in, mkay? For the same
reason, let's set it to require password to wake from sleep or screen
saver. And let's turn on the firewall and open holes only for specific
services and applications. Also, take this opportunity to go to the
preferences and set a hot corner to start your screensaver. Give your
laptop a good name in system preferences, sharing, and turn on Remote
Login. Because a computer you can't SSH to isn't much good.

I removed my Downloads, Documents, Music, etc. folders, and replaced
them with symlinks to folders with the same name in my DropBox folder:

    ln -s ~/Dropbox/Desktop Desktop

I've got the habit of putting all the manually-installed applications
(where you drag the program to the Applications folder) to an
Applications folder inside my home folder. It makes it easier to keep
programs I install separate from programs that came with the system.

I manually install the following programs (in no particular order):

-   [LaunchBar](http://www.obdev.at/products/launchbar/index.html) -
    Quicksilver replacement.
-   [CrashPlan](http://www.crashplan.com/) - Best OS X backup program.
-   [Delivery
    Status](http://junecloud.com/software/mac/delivery-status.html) (I
    run it on my iPhone as well. Love this app.)
-   [Dropbox](https://www.dropbox.com/) - My beloved "magic folder.'
-   [Flash Player Update](http://get.adobe.com/flashplayer/) - I yearn
    for the day when I don't need to install this.
-   [CoRD](http://cord.sourceforge.net) -- simply the best Microsoft
    Remote Desktop client.
-   [Adium](http://adium.im/) - My preference for a chat client.
-   [Emacs](http://emacsformacosx.com/) - The one editor to rule them
    all.
-   [SuperDuper](http://www.shirt-pocket.com/SuperDuper/SuperDuperDescription.html) -
    Best whole-disk hard-drive backup software ever.
-   [Timer](http://www.apimac.com/mac/timer/) - For setting a timer when
    I'm doing something monotonous and need motivation. ([Pomodoro
    technique](http://en.wikipedia.org/wiki/Pomodoro_Technique).)
-   [Google Chrome](https://www.google.com/chrome/browser/desktop/index.html) -
    Best web browser
-   [VMWare
    Fusion](http://www.vmware.com/products/fusion/overview.html) - A VM
    that doesn't show ads.
-   [Divvy](http://mizage.com/divvy/) - Move windows around quickly. A
    must for shuffling a half-dozen terminal windows.
-   [MailPlane](http://mailplaneapp.com/) - Best way to use gMail on
    your Mac.
-   [Git](http://git-scm.com/downloads) - Version control tool for
    programmers.

From the App Store:

-   [1Password](https://agilebits.com/onepassword) - If you get nothing
    else from this post, get 1Password. It's life-changing. That good.
    Syncs passwords with Mac, iPhone and iPad.
-   [MailMate](http://freron.com/) - My new favorite mail program.
-   [JustNotes](http://selfcoded.com/justnotes/) - Excellent note
    syncing with the Simplenote web site, Simplenote iOS app, and
    Dropbox (via Simplenote Web).
-   [Soulver](http://www.acqualia.com/soulver/) - Math problem
    solving -- I use it as my scratchpad and calculator
-   [DaisyDisk](http://daisydiskapp.com/) - Where did all my hard disk
    space go? DaisyDisk answers that question.
-   [Apple Remote Desktop](http://www.apple.com/remotedesktop/) -
    Essential for work. I connect to other people's desktops for
    troubleshooting and updates.
-   [PDFPen](http://smilesoftware.com/PDFpen/) - Edit PDF files.
-   [ReadLater](http://mischneider.net/readlaterapp/) - Desktop
    Instapaper client
-   [Growl](http://growl.info/) - Not sure if I still need this...
-   [Kindle](http://www.amazon.com/gp/feature.html/ref=kcp_mac_mkt_lnd?docId=1000464931) -
    For reading reference books on my Mac
-   [Reeder](http://reederapp.com/) - Google Reader desktop client.
    Excellent.

 

