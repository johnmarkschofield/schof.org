Title: Backing up Windows Machines through Retrospect
Date: 2002-10-11 11:38
Author: schof
Category: Technology
Slug: backing-up-windows-machines-through-retrospect

From [MacFixIt](http://www.macfixit.com)

Backing up Windows Machines through Retrospect; Dantz Investigating

Bob Cullia reports problems backing up Windows systsems on a local
network using the most recent Retrospect update, 5.0.236, released late
yesterday:

"Using a Mac G4 under Mac OS X 10.2.1 as the backup machine, all Mac
clients appear to work just fine. However, the Windows backup fails and
the log window reports that the data to be backed up is huge, 758GB,
when it is actually 254 MB. Of course the backup is them terminated. It
appears that Retrospect is incorrectly calculating the size of the stuff
on the Windows box."

Dantz says the Retrospect 5.0.236 update provides improved support for
Mac OS X 10.2 (Jaguar) specifically, and for Mac OS X in general. "Mac
OS 9 users will also enjoy several improvements, including faster
scanning of Mac OS X clients. Dantz recommends that all owners of
Retrospect 5.0 install this update."

UPDATE: Neil Herber offers additional confirmation of the Windows backup
bug. In his case the files with incorrectly reported sizes were being
pulled from a Flash memory card seated in a PC running Windows Millenium
Edition:

"I just updated to 5.0.236 and the backup log of a laptop running
Windows ME with a 20 GB drive showed several files over 250 GB each that
were not backed up. On the Windows machine, all of the affected files
are reported as less than 20 KB each. These files were coming off a
Flash card."

UPDATE: Eric Ullman in Technical Marketing let us know that Dantz is
looking into the issue:

"We're investigating now. I'll let you know as soon as we determine what
exactly is happening."

