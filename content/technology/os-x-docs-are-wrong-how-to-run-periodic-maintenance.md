Title: OS X Docs are Wrong; How To Run Periodic Maintenance
Date: 2009-03-12 11:09
Tags: os x

I just reimaged my laptop, and discovered that the "apropos" command had
nothing in its database. (You use "apropos" to look up man pages related
to a topic. It looks through an index to find appropriate pages to list,
and the periodic maintenance tasks had not created the index.) OK. No
problem. Google is my friend.

Google took me to an Apple Knowledge Base article that is out of date:
<http://support.apple.com/kb/HT2319>

This article states that you should, from the terminal, run "/etc/daily"
to run the daily maintenance tasks. That may have been true before
LaunchD took over from cron, but it's not true anymore. There is no
/etc/daily file on my 10.5 system.

The other option they suggest, "sudo periodic weekly" did work, and
generated the apropos index files.

