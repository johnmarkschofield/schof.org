Title: Update to Ubuntu Geek's "How To Check Your External IP Address From The Command Line"
Date: 2007-11-07 19:20
Author: schof
Category: Linux/Unix, OS X, Shell Scripting, System Administration, Technology
Tags: OS X, scripting, system administration, Ubuntu, whatismyip
Slug: update-to-ubuntu-geeks-how-to-check-your-external-ip-address-from-the-command-line

I follow the [Ubuntu Geek](http://www.ubuntugeek.com/) blog, and have
found some very useful tips there. However, there's a problem with their
latest tip, "[Howto Check you (sic) external IP Address from the command
line](http://www.ubuntugeek.com/howto-check-you-external-ip-address-from-the-command-line.html)."

Some background: There's a very useful website located at
[whatismyip.com](http://whatismyip.com), which reports the IP you used
to connect to the site. If you're on a computer behind a router which
does NAT ([Network Address
Translation](http://en.wikipedia.org/wiki/Network_address_translation)),
you can't find out what your external IP is by issuing commands on the
computer. Your computer's address is (for instance) 192.168.1.5, but
when traffic reaches the router, the router translates (with NAT) your
address to an external IP address, such as 34.23.64.9 (an IP address I
just made up).

WhatIsMyIP.com (and other sites like it) sprang up to fill that void,
and give you a simple way of finding out what external IP address you're
using.

Ubuntu Geek's script fetches the whatismyip.com page with wget, parses
it to find the IP address, and prints the IP address.

I tried it on my OS X box, and it didn't work, because wget isn't
installed on OS X -- but curl, a similar tool, is.

So I started modifying the script to use curl -- and discovered an
interesting comment in the source code to whatismyip.com's page:

> \<!--Please set your code to scrape your IP from
> www.whatismyip.com/automation/n09230945.asp Please set your code to
> hit this page at a REASONABLE pace. For more info, please see our
> "What's New" page.--\>

Hitting that link gets you just your IP address, which has two benefits
over Ubuntu Geek's implementation -- it means you have no parsing to do,
and it gives a SIGNIFICANTLY lower load to WhatIsMyIP's servers. (It's
rude to slam someone else's servers with an automated script -- even
though a script that simply fetches a web page once doesn't slam a
server, 10,000 people running that script would.)

Here's my take on Ubuntu Geek's BASH script:

``` {lang="bash"}
#!/bin/bash

echo -n "Your external IP Address is: "
curl http://www.whatismyip.com/automation/n09230945.asp
echo "."
```

For comparison's here's Ubuntu Geek's original script:

``` {lang="bash"}
#!/bin/bash

echo Your external IP Address is:
wget http://Www.whatismyip.com -O - -o /dev/null |
grep '' | sed -r 's/WhatIsMyIP.com - //g' |
sed -r 's///g'
exit 0
```

Moral of the story? Always look for a simpler way of doing things.

