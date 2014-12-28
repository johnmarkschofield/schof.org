Title: Announcing Two New Free Demos for AT&T's M2X Project
Date: 2014-04-02 10:33
Tags: linux, unix, python, system administration

I'm doing some work on demo projects for [AT&T's
M2X](https://m2x.att.com).\* Prior to this there was example code, but
there wasn't a quick and easy way of getting a working example going.

I've now created two new demos, with two hosting options:

-   [m2x-demo-openshift](https://github.com/attm2x/m2x-demo-openshift)
-   [m2x-demo-vagrant](https://github.com/attm2x/m2x-demo-vagrant)

The [Vagrant](http://www.vagrantup.com/) demo, of course, is free to
host, as it runs on your personal computer. The
[OpenShift](https://www.openshift.com/) demo is free to use as long as
you have fewer than three OpenShift applications already running.
(There's a limit of three free applications.)

Both demo repos contain
[loadreport.rb](https://github.com/attm2x/m2x-demo-vagrant/blob/master/loadreport.rb)
and
[stockreport.py](https://github.com/attm2x/m2x-demo-vagrant/blob/master/stockreport.py).
Loadreport reports the system load to AT&T's M2X system every minute.
Stockreport reports the current value of AT&T's stock to M2X every
minute. Both create their M2X Blueprints automatically.

The script stockreport.py uses the [M2X Python
package](https://github.com/attm2x/m2x-python). The loadreport.rb script
uses the [Ruby M2X gem](https://github.com/attm2x/m2x-ruby). This may be
the first working Ruby code for creating M2X blueprints that's been
published.

Because M2X is currently free for developers, it is important to provide
free options for developers to use to experiment with M2X. With these
two solutions, you can have a free M2X testing environment, either on
your computer or in the OpenStack cloud.

There are [more demo
languages](https://m2x.att.com/developer/client-libraries) and more demo
environments coming, and I'll be announcing those here as they're
published.

\* I don't speak for AT&T or
[Citrusbyte](https://citrusbyte.com/about-us).

