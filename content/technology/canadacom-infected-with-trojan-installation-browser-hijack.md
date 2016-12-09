Title: Canada.com Infected With Trojan-Installation Browser Hijack
Date: 2007-11-07 20:24
Tags: data security

**Summary:** Visitors to Canada.com (not hyperlinked for obvious
reasons) will have their browsers hijacked, and a series of prompts will
download and attempt to install malicious software. This will happen
ONLY on the first visit from an IP address. Subsequent visits to
Canada.com will not experience the browser hijack.

*NOTE: I have only experienced this on the Vancouver Sun section of
Canada.com. I'm currently out of different IP addresses to try. I'll try
again from home to see if the rest of Canada.com is infected.*

**How I found The Problem:** I followed a link from
[Bynkii.com](https://web.archive.org/web/20080412054849/http://www.bynkii.com/) to a Vancouver Sun story that Bynkii
discussed. My browser was immediately hijacked. I visited the site
again, and found no errors. I then tried from a laptop connected to our
company's wireless network (completely separate from our internal
network, and through a separate ISP) and saw the hijack again. That time
I got
[screencaps](http://flickr.com/photos/schof/sets/72157603001488073/).
Visiting the site through the wireless again showed no problems, leading
me to believe that this displays one time per IP address. Trying
multiple browsers did not result in another browser hijack, and neither
did clearing cookies, making me think it's recording IP address and
attacking once per IP address.

**Details:**

The first time you visit Canada.com, your browser will flash through a
few redirects, and then the following popup will appear:  

[![FirstPopUp](http://farm3.static.flickr.com/2273/1911230563_b7e7d02adc_o.png)](http://www.flickr.com/photos/schof/1911230563/ "Photo Sharing")

Note that hitting either Cancel or OK appears to have the same result --
you can't get out of there. Your browser will then appear to scan your
hard drive for viruses. It's all theater; it's not actually doing
anything at this point:

[![scanningmysystem](http://farm3.static.flickr.com/2413/1912063850_5564a68325.jpg)](http://www.flickr.com/photos/schof/1912063850/ "Photo Sharing")

It will then pop up a message (in an Windows-style message box -- not
sure how it did that):

[![RemoveErrors](http://farm3.static.flickr.com/2227/1912064916_c6dfaba36f.jpg)](http://www.flickr.com/photos/schof/1912064916/ "Photo Sharing")

If you're on a Macintosh, it will then offer to download an EXE file.
I'm not sure if it will automatically download and run the file on a
Windows machine, because I'm not about to try.

[![DownloadInstaller](http://farm3.static.flickr.com/2044/1911232457_6dde35973b.jpg)](http://www.flickr.com/photos/schof/1911232457/ "Photo Sharing")

I uploaded the downloaded file to virustotal.com, and it found a variety
of badness there, general consensus seems to be that this file isn't so
bad by itself, but will once installed download and install an
additional slew of malware and trojans of unknown potency. (I was unable
to find really definitive information about this file; I'm open to
suggestions for better places to look.)

I submitted this to the [Internet Storm Center](http://isc.sans.org/),
along with a malware sample, and e-mailed webmaster@canada.com with a
warning.

**Update November 15, 2007:** [Wired just wrote about the
issue](http://blog.wired.com/business/2007/11/doubleclick-red.html);
apparently it affects a number of different sites, as the hijack script
was distributed via the Doubleclick ad network.

**Update November 16, 2007**: Wired [wrote about the issue
again](http://www.wired.com/techbiz/media/news/2007/11/doubleclick),
quoting me this time.

