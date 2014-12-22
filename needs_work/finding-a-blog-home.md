Title: Finding a Blog Home
Date: 2012-08-03 19:31
Author: schof
Category: Internet &amp; Web, Technology, Tools
Slug: finding-a-blog-home

*[TL;DR](http://www.urbandictionary.com/define.php?term=tl%3Bdr): If
you're looking for a blogging host and your budget supports \$29 a
month, you should try [WP
Engine.](http://www.shareasale.com/r.cfm?B=398777&U=672925&M=41388&urllink=)*

I've been trying to find a home for my blog for a while now. So long, in
fact, that trying to build or find the perfect blogging platform became,
instead, the perfect procrastination tool.

I've now decided that good enough is... good enough. I looked at the
following major hosts or categories of host:

-   [Squarespace](http://squarespace.7eer.net/c/37109/38421/1291)
-   [Self-Managed WordPress](http://wordpress.org)
-   Managed WordPress ([WordPress.com](http://wordpress.com) &
    [WPEngine.com](http://www.shareasale.com/r.cfm?B=398777&U=672925&M=41388&urllink=))

Squarespace
-----------

I found a number of problems with
[Squarespace](http://squarespace.7eer.net/c/37109/38421/1291). Switching
between themes was buggy if you tried more than a couple of themes (as
you do when you're trying to find a theme for a blog). I contacted
support but they were unable to resolve the issue. Squarespace claimed
they were able to import from WordPress, but this ability is limited --
they have a blogging engine for your site, but the WordPress posts and
pages are imported into a DIFFERENT portion of your site -- it's not
integrated with the built-in Squarespace blogging tools. (I evaluated
version 5 of Squarespace. They're currently on version 6, which I
haven't looked at.)

Self-Managed WordPress
----------------------

That left me with [some variety of
WordPress](http://en.support.wordpress.com/com-vs-org/). I've done
self-managed WordPress in the past, and it's a pain in the ass.
WordPress releases security updates on a fairly regular basis, and you
NEED to install those updates in order to be secure -- otherwise you'll
go to your blog one day and realize your blog is full of linkspam for
Bulgarian Viagra vendors.

WordPress.com
-------------

So that leaves managed. First I looked at
[WordPress.com](http://wordpress.com) -- the folks who write [the
WordPress software](http://wordpress.org). [They're inexpensive: \$13 a
year for a custom domain like schof.org, and \$30 a year to not have any
ads on your website.](http://store.wordpress.com/) Generally blogs
hosted at WordPress.com are fast and stable. But after setting it up I
found the following problems that made me switch away from
WordPress.com:

No plugins. You're stuck with the functionality built into WordPress.
That's generally enough for everyone...but if it's not, you're out of
luck. For several reasons, that was not enough for me.

On WordPress.com, you're limited to a single URL scheme. URLs are
SITE.com/YEAR/MONTH/DAY/POSTNAME. Since I did not use that URL scheme on
my previous site, all my URLs were going to break. Problem.

This revealed another problem -- you can't redirect a page. If an old
link points to SITE.com/FOOBAR, you can't create a rule that sends that
link to SITE.com/YEAR/MONTH/DAY/FOOBAR. This meant that when I switched
to WordPress.com, all my pages in Google and all my incoming links from
other blogs would stop working and return 404 errors. Not good.

On WordPress.com you can't upload a theme -- you've got the (large
number of) built-in themes, and no more.

Most important, there's no real backup possible. Sure, you can download
an XML export of your blog -- but that's a manual process, and there's
no workable way to automate that through WordPress.com. And even if you
did automate that through Selenium or some other web automation tool,
you'd still have the problem of backing up your media files. Backing
those up is completely unsupported on WordPress.com other than manually
downloading each file. Although WordPress.com does internal backups to
multiple sites (so your data is unlikely to disappear through accidents
or errors) it's still a dealbreaker for me -- I require external backups
so that if WordPress.com goes away some day, my data doesn't.

This is a much more minor issue, but revisions are turned off for
performance reasons on WordPress.com -- and since you can't install
plugins, there's no way to get any kind of revisions going.

WP Engine
---------

I ended up switching to
[WPEngine.com](http://www.shareasale.com/r.cfm?B=398777&U=672925&M=41388&urllink=),
and I've been very happy. They address most of the pain I found in
hosting on WordPress.com:

It's definitely more expensive -- WordPress.com is \$43 a YEAR for your
own domain with no ads.
[WPEngine.com](http://www.shareasale.com/r.cfm?B=398777&U=672925&M=41388&urllink=)
is \$29 a MONTH.

WPEngine.com is just as fast (or possibly faster) than WordPress.com --
doing speed tests on the pages was inconclusive -- on some pages
WordPress.com won slightly; on others WP Engine won slightly. My general
conclusion (based on insufficient data) is that WPEngine.com is faster,
but does nothing to optimize images for speed and size when you upload
them, while WordPress.com does -- so on image-heavy pages, WordPress.com
comes out faster. On pages with mostly text, WPEngine.com is faster.
(I'll be learning to optimize my images for speed and writing about that
later.)

However, the admin interface for WPEngine.com is BLAZINGLY faster than
WordPress.com -- if the user-facing speed is a toss-up, the admin speed
is a HUGE win for WPEngine.com. Actions that take 3-10 seconds on
WordPress.com take 1-2 seconds on WPEngine.com -- it makes administering
a blog like this much more enjoyable.

WPEngine.com lets you install plugins. There's a small number of plugins
they support explicitly, and a small number that they ban, but the vast
majority of plugins are unsupported but allowed -- you can install
anything you need. This is vastly freeing -- plugins are one of the best
parts of running WordPress.

On WPEngine.com, you CAN set custom URL schemes -- you have all the
options that the self-hosted WordPress.org software allows. What's more,
WP Engine has an admin interface to do redirects, so you can redirect
one page at an old URL to the new URL. This is a major win!

Since you have FTP access, you can pick from their library of vetted
themes, or upload one you've purchased or written yourself. You can make
any changes you want to installed themes.

WP Engine supports backup! Their sites are backed up in the same manner
as WordPress.com, but in addition, you can set it to back up your
database and all files to an Amazon S3 bucket -- where even if WP Engine
disappears from the Earth, your files and data will be safe. This was
the deciding factor for me in choosing WP Engine.

And finally, because you can install plugins, you can have revisions!

 

**FULL DISCLOSURE: **I have affiliate agreements with [WP
Engine](http://www.shareasale.com/r.cfm?B=398777&U=672925&M=41388&urllink=)
and [Squarespace](http://squarespace.7eer.net/c/37109/38421/1291).
([WordPress.com](http://wordpress.com) does not have an affiliate
program.) If you click the links to either of those sites and end up
subscribing, I'll get some money out of the deal. As you can tell by my
evisceration of Squarespace, I'm keeping my editorial independence.

