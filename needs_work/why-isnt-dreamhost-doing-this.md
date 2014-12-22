Title: Why Is Dreamhost Not Talking About Grids?
Date: 2006-10-14 16:34
Author: schof
Category: Internet &amp; Web, System Administration, Technology
Slug: why-isnt-dreamhost-doing-this

[Media Temple](http://www.mediatemple.net/) is talking about a new
service called
[Grid-Server](http://www.mediatemple.net/company/whatsnew/gsgridserver.php)
([via](http://paulstamatiou.com/2006/10/10/media-temples-grid-server-coming-next-weekish/)).
It's not available yet, but it's supposed to be coming this month.

I have no experience with Media Temple. But Grid-Server seems like one
of the brilliant ideas that are obvious once someone else invents them.
Oh sure, other people have done redundant web hosting before. Thousands
of little guys plus Google, Amazon, Yahoo, MySpace, etc. are dividing
web-hosting duties between many computers such that if one goes, down,
the others can keep the website running.

But no commercial webhosting company I'm aware of currently offers
grid-based hosting. This leads to outages and slowness for clients.
[DreamHost](http://dreamhost.com/) has had a number of recent problems.
To their credit, they are quite open and honest about what
[went](http://blog.dreamhost.com/2006/08/01/anatomy-of-an-ongoing-disaster/)
[wrong](http://blog.dreamhost.com/2006/09/19/anatomy-of-a-disaster-part-2/).
But there's also a constant parade of announcements of servers going
down for 10 minutes here, 10 minutes there for [RAM
upgrades](http://www.dreamhoststatus.com/2006/10/09/ram-upgrades-2/),
[hardware
replacements](http://www.dreamhoststatus.com/2006/10/06/problem-with-aviation-server/),
etc.

There is NO REASON I can think of why my website, even at DreamHost's
low prices, should be dependent on [ONE database
server](http://www.dreamhoststatus.com/2006/10/07/database-server-odie-hardware-troubles/),
[ONE web
server](http://www.dreamhoststatus.com/2006/10/10/tequila-being-moved-to-new-hardware/),
and [ONE file
server](http://www.dreamhoststatus.com/2006/09/30/quick-battery-swap-in-a-file-server/).
Any one of them goes down; my website goes down.

Creating a grid of dozens of computers, each of which can shuffle around
websites to balance load or handle failures is not an easy task. It
would take me loads of research before I was even ready to begin that
sort of project, and I'd have to hire a team of people to do it. It's a
big deal.

On the other hand, it's been proven that this sort of thing is possible.
It's not like we need basic research or feasibility studies. You can
hire people who know how to do this if you're willing to pay for it.

It's not like this should be a tough decision for DreamHost. One of the
primary benefits of this technology is to eliminate [problems with over-
and
under-selling](http://blog.dreamhost.com/2006/05/18/the-truth-about-overselling/).
The host has a pool of resources that can be grown incrementally, as
resource use grows, without worrying about the growth rates of
individual sites.

Sites have fewer worries about going down, both from the Slashdot / Digg
effect, and from hardware failure or misconfiguration at the hosting
company.

So why isn't DreamHost doing this? My hope is that they're already
working on it -- but I wish they'd let us know.

UPDATE June 9, 2007: This site is now hosted at
[NearlyFreeSpeech.net](http://nearlyfreespeech.net "Sudosu.net's web host, NearlyFreeSpeech.net").
So far, I love them. (An unfortunate truism of web hosting is that all
hosts are great until they start to suck.) I've eventually been
disappointed with every host I've tried. I host both personal and
business websites; so far,
[pair.com](http://pair.com "A web host John Mark Schofield likes, Pair.com")
and nearlyfreespeech.net are the only hosts on my "not sucking yet"
list.

