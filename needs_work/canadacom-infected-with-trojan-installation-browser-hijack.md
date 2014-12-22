Title: Canada.com Infected With Trojan-Installation Browser Hijack
Date: 2007-11-07 20:24
Author: schof
Category: Security, Technology, Troubleshooting
Tags: browser hijacking, malware, security, wired
Slug: canadacom-infected-with-trojan-installation-browser-hijack

**Summary:** Visitors to Canada.com (not hyperlinked for obvious
reasons) will have their browsers hijacked, and a series of prompts will
download and attempt to install malicious software. This will happen
ONLY on the first visit from an IP address. Subsequent visits to
Canada.com will not experience the browser hijack.

*NOTE: I have only experienced this on the Vancouver Sun section of
Canada.com. I'm currently out of different IP addresses to try. I'll try
again from home to see if the rest of Canada.com is infected.*

**How I found The Problem:** I followed a link from
[Bynkii.com](http://Bynkii.com) to a Vancouver Sun story that Bynkii
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

> File <span id="status_nombre">Install-MnBhY2lmaWM-a2V5aW4-a2V5a</span>
> received on <span id="status_fecha">11.08.2007 03:28:07 (CET)</span>
>
> <table id="tablaMotores" width="550" border="0" cellspacing="0" cellpadding="0">
> <tbody>
> <tr>
> <th>
> Antivirus
>
> </th>
> <th>
> Version
>
> </th>
> <th>
> Last Update
>
> </th>
> <th>
> Result
>
> </th>
> </tr>
> <tr>
> <td>
> AhnLab-V3
>
> </td>
> <td>
> 2007.11.8.0
>
> </td>
> <td>
> 2007.11.08
>
> </td>
> <td>
> -
>
> </td>
> </tr>
> <tr>
> <td>
> Authentium
>
> </td>
> <td>
> 4.93.8
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td class="positivo">
> could be infected with an unknown virus
>
> </td>
> </tr>
> <tr>
> <td>
> AVG
>
> </td>
> <td>
> 7.5.0.503
>
> </td>
> <td>
> 2007.11.08
>
> </td>
> <td class="positivo">
> Generic9.HLR
>
> </td>
> </tr>
> <tr>
> <td>
> CAT-QuickHeal
>
> </td>
> <td>
> 9.00
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td>
> -
>
> </td>
> </tr>
> <tr>
> <td>
> DrWeb
>
> </td>
> <td>
> 4.44.0.09170
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td>
> -
>
> </td>
> </tr>
> <tr>
> <td>
> eTrust-Vet
>
> </td>
> <td>
> 31.2.5278
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td>
> -
>
> </td>
> </tr>
> <tr>
> <td>
> FileAdvisor
>
> </td>
> <td>
> 1
>
> </td>
> <td>
> 2007.11.08
>
> </td>
> <td>
> -
>
> </td>
> </tr>
> <tr>
> <td>
> F-Prot
>
> </td>
> <td>
> 4.4.2.54
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td class="positivo">
> W32/Heuristic-119!Eldorado
>
> </td>
> </tr>
> <tr>
> <td>
> Ikarus
>
> </td>
> <td>
> T3.1.1.12
>
> </td>
> <td>
> 2007.11.08
>
> </td>
> <td class="positivo">
> Virus.Win32.Renos.AE
>
> </td>
> </tr>
> <tr>
> <td>
> McAfee
>
> </td>
> <td>
> 5158
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td class="positivo">
> BraveSentry
>
> </td>
> </tr>
> <tr>
> <td>
> NOD32v2
>
> </td>
> <td>
> 2645
>
> </td>
> <td>
> 2007.11.08
>
> </td>
> <td class="positivo">
> Win32/Hoax.Renos.PY
>
> </td>
> </tr>
> <tr>
> <td>
> Panda
>
> </td>
> <td>
> 9.0.0.4
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td class="positivo">
> Suspicious file
>
> </td>
> </tr>
> <tr>
> <td>
> Rising
>
> </td>
> <td>
> 20.17.22.00
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td>
> -
>
> </td>
> </tr>
> <tr>
> <td>
> Sunbelt
>
> </td>
> <td>
> 2.2.907.0
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td>
> -
>
> </td>
> </tr>
> <tr>
> <td>
> TheHacker
>
> </td>
> <td>
> 6.2.9.119
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td>
> -
>
> </td>
> </tr>
> <tr>
> <td>
> VirusBuster
>
> </td>
> <td>
> 4.3.26:9
>
> </td>
> <td>
> 2007.11.07
>
> </td>
> <td class="positivo">
> Trojan.Renos.Gen.2
>
> </td>
> </tr>
> </tbody>
> </table>
> <table id="tablaInformacion" width="550" border="0" cellspacing="0" cellpadding="0">
> <tbody>
> <tr>
> <th>
> Additional information
>
> </th>
> </tr>
> <tr>
> <td>
> File size: 31288 bytes
>
> </td>
> </tr>
> <tr>
> <td>
> SHA1: ef6fce7ad9a01d6cabb84bffc3bddee6f43bfe4e
>
> </td>
> </tr>
> </tbody>
> </table>

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

