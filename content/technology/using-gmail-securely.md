Title: Using gMail Securely, Even on Wireless
Date: 2007-08-04 23:48
Tags: obsolete, security

If you see "http://" in the address bar for a website, that connection
is unsecured. Anyone eavesdropping can access everything sent and
received between you and the website. Which is no problem if you're
reading [tmz.com](http://tmz.com), but a big problem if you're on
[wamu.com](http://wamu.com).

If you see "https://" in the address bar,
that connection is generally secure. In many cases, you can make an
insecure connection secure by adding an "s" in the address bar and
hitting "enter." (Whether or not it works depends on the site's web
server configuration. Some aren't set up to support secure connections.)

Google redirects you to a secure https connection while you're logging
in, but sends you back to http for everything else. So if you use Google
Mail (aka gMail) without doing anything to secure it, any eavesdropper
can read all your mail. This is not a huge problem on a wired
connection, but if you're using any kind of wireless connection, you
should be concerned -- and if you use an open wireless connection, you
should be alarmed.

The "add an 's'" trick doesn't always work with
gMail, as I've noticed it switching back to http seemingly at random.
You can get around this by bookmarking <https://mail.google.com/mail> --
if you start there, Google will leave the entire session protected.
Another solution is Mark Pilgrim's
[Grease Monkey](http://www.greasespot.net/ "Greasemonkey Firefox Extension")
extension to Firefox, GMailSecure. _(Editor's Note: GMailSecure is no longer available or
needed. See the end of this article for a modern replacement.)_

With GMailSecure, your browser automatically redirects from http://mail.google.com to
https://mail.google.com -- nicely solving this problem. Typing just
"gmail.com" in the address bar first redirects to
"http://mail.google.com/mail" (because of Google) and then redirects
from there to "https://mail.google.com/mail" (because of GMailSecure).

__Note From December 2014__: Use the [EFF's](https://www.eff.org/)
"[HTTPS Everywhere](https://www.eff.org/HTTPS-EVERYWHERE)" extension instead.