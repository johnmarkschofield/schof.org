Title: Archiving RSS Links Through Pinboard
Date: 2012-07-31 20:38
Author: schof
Category: Internet &amp; Web, Python Programming, Technology, Tools
Slug: archiving-schof-org-links-through-pinboard

I've been moving many posts from past websites I've had into schof.org,
so schof.org will be the unitary place to get my writing on the web.

In going through the old posts, I was shocked to find out how many links
I've posted are no longer valid.

I use [Pinboard](http://pinboard.in) and like it a great deal. For [\$25
a year](http://pinboard.in/tour/#archive) Pinboard will archive your
bookmarks -- saving a cache of the state of the web link when the
Pinboard server visits it. (Which may be a day or two after you bookmark
it.) If the link later disappears, you've got the archived content on
Pinboard.

I've been using this manually, but wanted a way to automate adding links
from my WordPress blog, schof.org. I was able to build a recipe from
[ifttt.com](http://ifttt.com/) that would automatically add my posts to
Pinboard, but I need something that will add links in my posts to
Pinboard.

Pinboard's API to the rescue! I wrote a simple little script in 20
minutes that downloads my RSS feed, parses each entry for links, and
submits any links it finds to Pinboard, using the link text as the title
and the URL as the description.

I set it to run every four hours by putting it into my crontab.

It's quick and dirty, and it's not a general-purpose application (the
URL for my feed is hard-coded in there). Right now you need to know
basic Python to get it to work, as well as how cron works in order to
automate it.

If there's interest in this, I'll be happy to turn it into a more
general-purpose tool.

You'll have to install
[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/),
[python-pinboard](https://github.com/mgan59/python-pinboard), and
[feedparser](http://code.google.com/p/feedparser/) to run this.

[Source code is on
Github](https://github.com/johnmarkschofield/WordPress-To-Pinboard-Archive),
as usual.

