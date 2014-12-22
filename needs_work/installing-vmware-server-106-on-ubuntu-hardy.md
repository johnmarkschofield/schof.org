Title: Installing VMware Server 1.0.6 on Ubuntu Hardy
Date: 2008-06-11 17:26
Author: schof
Category: Linux/Unix, System Administration, Technology, Troubleshooting
Tags: command-line, Linux, system administration, Unix, VMWare
Slug: installing-vmware-server-106-on-ubuntu-hardy

It generally works pretty well, but I found the following problem, and
Google was no help:

    Building the VMware VmPerl Scripting API.

    Using compiler "/usr/bin/gcc". Use environment variable CC to override.

    Unable to compile the VMware VmPerl Scripting API.

    ********
    The VMware VmPerl Scripting API was not installed. Errors encountered during
    compilation and installation of the module can be found here:
    /tmp/vmware-config4

    You will not be able to use the "vmware-cmd" program.

    Errors can be found in the log file:
    '/tmp/vmware-config4/control-only/make.log'
    When you look at make.log, you see a series of errors like this:
    In file included from VmPerl.xs:6:
    /usr/lib/perl/5.8/CORE/perl.h:420:24: error: sys/types.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:451:19: error: ctype.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:463:23: error: locale.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:480:20: error: setjmp.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:486:26: error: sys/param.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:491:23: error: stdlib.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:496:23: error: unistd.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:776:23: error: string.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:925:27: error: netinet/in.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:929:26: error: arpa/inet.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:939:25: error: sys/stat.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:961:21: error: time.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:968:25: error: sys/time.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:975:27: error: sys/times.h: No such file or directory
    /usr/lib/perl/5.8/CORE/perl.h:982:19: error: errno.h: No such file or directory

The answer is simple:

``` {lang="bash"}
sudo apt-get install libc6-dev
```

Now Google has the answer.

