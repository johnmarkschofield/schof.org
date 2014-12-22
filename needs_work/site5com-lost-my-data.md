Title: Site5.com Lost All My Data, Then Warned Me That Closing My Account Might Cause Data Loss 
Date: 2007-06-04 12:39
Author: schof
Category: Linux/Unix, System Administration, Technology
Slug: site5com-lost-my-data

Summary: [Site5 sucks](http://site5.com). They lost all my data and took
my site down until I could restore from backup.

Wednesday night my site went down. Consider it a comment on the level of
service site5.com provides that this didn't worry me too much. I knew it
would be back up shortly, like it always is when Site5.com goes down.
(Several times a week.) I had it on my list to move to a different
hosting provider; I just hadn't done it yet.

Then Thursday morning I get this e-mail:

> From: devnull@site5.com  
>  Subject: Subject: Site5 Incident Notification: oracle.site5.com  
>  Date: May 24, 2007 8:53:45 AM PDT  
>  To: [My E-mail Address]
>
> Dear John Schofield,
>
> My name is Todd Mitchell, I am Chief Operating Officer at Site5. I am
> writing you this morning in regards to the outage with oracle which
> began to affect you at approx. 18:00 EST, May 23rd, 2007.
>
> At approx. 18:00 EST on May 23rd, 2007 oracle became unresponsive and
> as a result one of our system administrators requested a reboot for
> the server. A short time later, less than 10 minutes, our system
> administrator contacted our data center and hardware provider (Net
> Access Corporation / NAC) as the machine did not return to service
> from the unscheduled reboot. Upon further investigation by our data
> center, their initial determination was that the Operating System
> became corrupt and couldn't initialize our disk array on boot.
>
> At this point one of our lead system administrators decided in the
> best interest of our clients to begin a restoration from backup due to
> the inherent difficulties of restoring both a corrupted root and data
> filesystem. Upon making this decision, they proceeded to verify that
> our backups are intact and would at that point initiate our server
> restoration procedures. Unfortunately, after several rounds of
> integrity checking it was discovered that the backups for oracle are
> corrupt and unusable.
>
> I am terribly saddened by this discovery. One of the core values of
> hosting is to first provide a quality hosting environment and
> secondly, ensure that data is available if a server should fail.
> Unfortunately due to dire circumstance, all data for this server is
> corrupt and completely unusable. We are in the process of returning
> our server to its original configuration and returning your account to
> its default state--your username and password remain the same. Please
> use them to FTP into your account and upload your local backups.
>
> We realize how frustrating this is for you so we're offering a 12
> month service credit. This service credit is automatic (no need to
> request it and it will appear on your account within 24 hours) and it
> will be automatically applied to future invoices. Please note that
> this service credit has no cash value and cannot be requested in the
> form of cash, check and/or refund to a credit card. This service
> credit is, however, transferable between Site5 customer accounts.
> Alternatively, if you'd like to terminate your account, I have
> authorized our billing department to refund, back to your credit card
> on file, up to 12 months of previously paid for service.
>
> This incident has been extremely trying for us. Site5 has been in
> business since 1999 and we've never experienced an issue like
> this--our clients have always received the best possible service from
> us. I simply cannot express in words how awful we feel and how
> heartbroken our system administrators are. We will, of course, be
> looking at how this happened and what we can do in the future to avoid
> this at all costs. I hope that we can regain your trust and patronage
> in some capacity.
>
> Sincerely,
>
> Todd Mitchell on behalf of the entire Site5 management team.

OK. So that's completely screwed. I mean, for a professional hosting
company (or any decent-sized company) not testing restores is
unacceptable. It's one of the cardinal rules of backups -- make sure
your backups are actually good. Making this mistake worse, it looks from
the e-mail like they didn't begin the restore process and discover their
backups were corrupt -- this is the classic form of this mistake.
Instead, they did a backup validity check and determined (without having
to perform a restore) that the backup was corrupt. That means they could
have done this backup validity check at any time, without having to do a
full restore -- meaning there is even LESS excuse for this failure.

(In their defense, I have to say I like Site5's handling of the issue,
in terms of issuing credits or refunds. But that's ALL that I like about
this.)

Since I had already decided to leave Site5 at some point, this was an
easy choice: Leave Site5 and get my money back!

> From: John Schofield  
>  To: Billing@site5.com  
>  Date: May 24, 2007 9:23 AM  
>  Subject: Re: Subject: Site5 Incident Notification: oracle.site5.com
>
> We will be canceling our account with Site5. We request, per your e-  
>  mail below, our previous 12 months of charges refunded. I expect to  
>  see no further charges from Site5 on my credit card.
>
> There is nothing I can say about how inexcusable a failure this is on  
>  the part of Site 5. Words fail me.
>
> Sincerely,  
>  John Schofield

Then Site5, clearly determined to add insult to injury, sent this:

> To: [My E-mail Address]  
>  Subject: [Site5 \#QZK-378129]: Re: Subject: Site5 Incident
> Notification: oracle.site5.com  
>  Date: Thu, 24 May 2007 12:25:29 -0400  
>  Reply-To: billing@site5.com
>
> Hello John,
>
> Thank you for writing. Though I am sorry to hear that you wish to
> cancel your account, we would be glad to assist you with any request
> that you may have.
>
> As account cancellation will result in irreversible file loss, can you
> please reply with the following:
>
> 1\. The full domain name of any account(s) you wish to cancel.
>
> 2\. For security purposes, please verify either the last four digits of  
>  the credit card on file in your account details or the physical  
>  address that is on file in your account's contact information.
>
> 3\. Verification of a recent backup of the files. Have you been able to  
>  download an archive of the account or any necessary files?
>
> If you have any additional questions or concerns, feel free to contact
> us at anytime. Thanks again.
>
> ---  
>  Jessica Noling  
>  Customer Service  
>  Site5 Internet Solutions, Inc.  
>  http://www.site5.com

My reply:

> From: John Schofield  
>  To: Billing@site5.com  
>  Date: May 24, 2007 9:30 AM  
>  Subject: Re: [Site5 \#QZK-378129]: Re: Subject: Site5 Incident
> Notification: oracle.site5.com
>
> 1\. [My Domain Name]
>
> 2\. [My address]
>
> 3\. We are canceling our service because Site 5's server went down,  
>  and Site 5 did not have adequate backups in place. Our data has  
>  already been irreversibly lost, by Site5's incompetence. Thanks for  
>  the thought, though.
>
> Sincerely,
>
> John Schofield

Site5 did refund all my hosting fees for the past 12 months, or I'd be
foaming at the mouth far more than I am now. But despite them handling
their failure (AFTER the fact) in a professional and responsible manner,
I'm still thoroughly pissed I ended up in the situation in the first
place.

I was able to restore almost all my content from backups, but some
changes had been made in a DB on the site that had not been backed up
recently -- so I did lose some work because of this.

I've since set this site up (not sudosu.net; a different site) with dual
hosting with two separate hosting companies, and my DNS provider doing
failover between them, and automatic backup. That's a future article.

