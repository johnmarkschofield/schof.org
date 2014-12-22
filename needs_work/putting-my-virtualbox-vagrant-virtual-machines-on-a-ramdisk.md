Title: Putting my VirtualBox & Vagrant Virtual Machines on a Ramdisk
Date: 2014-01-10 18:09
Author: schof
Category: OS X, Shell Scripting, System Administration, Technology
Slug: putting-my-virtualbox-vagrant-virtual-machines-on-a-ramdisk

I do a lot of work with virtual machines (mainly
[Vagrant](http://www.vagrantup.com/) /
[VirtualBox](https://www.virtualbox.org/) instances for my DevOps work)
and speed is a huge issue for me.

When I started at my new job I requested the fastest computer I could
find -- a new iMac with an SSD drive -- and it's still not fast enough
when you're iterating on virtual machines. So I went old-school, and
created a [ramdisk](https://en.wikipedia.org/wiki/RAM_drive).

I changed my VirtualBox settings to create new virtual machines on the
ramdisk, and my BASH init scripts are set up to create the ramdisk when
they run.

The idea is that my virtual machine files will be stored in RAM on the
ramdisk, and will be much faster to access and change. Of course, the
downside is that when you reboot, you lose the ramdisk, and all its
contents. Because I'm on an iMac and don't reboot too often, this nets
out to be a win for me.

Setting up VirtualBox was trivial: [![Screenshot 2014-01-10
17.57.07](http://schof.org/wp-content/uploads/2014/01/Screenshot-2014-01-10-17.57.07.png)](http://schof.org/wp-content/uploads/2014/01/Screenshot-2014-01-10-17.57.07.png)Setting
up the script to create the ramdisk was a little more complicated.

First of all, here's the command:

> <div id="LC91">
>
>         diskutil erasevolume HFS+ "RAMDISK" \`hdiutil attach -nomount
> ram://\$SIZE\_IN\_SECTORS\`
>
> </div>

That will create a volume called RAMDISK and mount it. I called this
from my \~/.bashrc file. However, I ran into several minor problems, and
my example might save you some time:

First, this runs on creation of every terminal window, and you only want
one ramdisk to exist, so I added logic to test for the existence of the
ramdisk before starting it.

Then I ran into another problem -- when you close the Terminal with
multiple windows open, it will open multiple windows when it starts
again -- and because things are so fast, each window will check for the
existence of the ramdisk, see that it's not there, and create it. You
end up with a dozen ramdisks.

So now my code checks for the existence of the ramdisk. if it's not
there, it sleeps a random amount of time, then checks again, and creates
the ramdisk if needed. I can open two dozen terminal windows at once
with no ramdisk in place, and it will only create one. (It's possible
that a collision could make it generate two or more ramdisks, but I
re-open Terminal with no ramdisk mounted so seldom that it has never
happened to me, and hasn't been worth engineering against.)

Here's the ramdisk stanza I ended up with:

<div id="LC75">

> <div id="LC75">
>
> \# Set up RAM disk for VirtualBox Images
>
> </div>
>
> <div id="LC76">
>
> SIZE\_IN\_GB=14
>
> </div>
>
> <div id="LC77">
>
> SIZE\_IN\_SECTORS=\`echo "\$SIZE\_IN\_GB\*1024\^3/512" | bc\`
>
> </div>
>
> <div id="LC78">
>
> </div>
>
> <div id="LC79">
>
> if [ -d /Volumes/RAMDISK ]; then
>
> </div>
>
> <div id="LC80">
>
> echo "RAMDISK for VirtualBox images already exists. Doing nothing."
>
> </div>
>
> <div id="LC81">
>
> else
>
> </div>
>
> <div id="LC82">
>
> echo "Ramdisk does not exist."
>
> </div>
>
> <div id="LC83">
>
>     SLEEPTIME=\$((\$RANDOM % 30 + 1))
>
> </div>
>
> <div id="LC84">
>
>     \# Sleeping before attempting to create ramdisk, to avoid creating
> multiple ramdisks when opening multiple windows simultaneously.
>
> </div>
>
> <div id="LC85">
>
>     echo "Sleeping \$SLEEPTIME"
>
> </div>
>
> <div id="LC86">
>
>     sleep \$SLEEPTIME
>
> </div>
>
> <div id="LC87">
>
>     if [ -d /Volumes/RAMDISK ]; then
>
> </div>
>
> <div id="LC88">
>
> echo "Another window created the ramdisk. Doing nothing..."
>
> </div>
>
> <div id="LC89">
>
>     else
>
> </div>
>
> <div id="LC90">
>
> echo "Creating ramdisk."
>
> </div>
>
> <div id="LC91">
>
>         diskutil erasevolume HFS+ "RAMDISK" \`hdiutil attach -nomount
> ram://\$SIZE\_IN\_SECTORS\`
>
> </div>
>
> <div id="LC92">
>
>     fi
>
> </div>
>
> <div id="LC93">
>
> fi
>
> </div>

 

[Here's it on GitHub, easily
clonable.](https://github.com/johnmarkschofield/ocd/blob/master/.bashrc)

</div>

The final issue is what happens when you reboot and your virtual
machines disappear. VirtualBox will report that the machines are
"inaccessible." They certainly are! Here's the fix:

> VBoxManage list vms
>
> VBoxManage unregistervm {774a761b-9cf3-45cc-a514-aeec198ea3d0}

Of course, use the guid displayed by "list vms" on your system, not the
guid I used.

So far this has been working well for me, and really speeding things up
for about three weeks.

**  
Update 2014-03-24:**

I created a quick Python script to remove my inaccessible VMs. You can
find it
at <https://github.com/johnmarkschofield/nuke-virtualbox-inaccessible>

