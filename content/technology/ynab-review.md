Title: Review of You Need A Budget
Date: 2021-09-14 15:51
Tags: personal_finance, software, Saas, review


The value I get from [You Need A Budget](https://www.youneedabudget.com) (YNAB) for managing my personal finances is immense. I really like the mental model of putting money aside for specific future expenses, and it causes my savings rate to be significantly higher. If you're trying to manage your budget to reduce your expenses and save more money, I can't recommend YNAB highly enough.

YNAB is probably my least-favorite software that I use daily. This review could probably end there. I get tremendous value from YNAB and recommend it to others, but there's so much about it I just haaaaaaaaaaaate.

There are two root causes for almost all of my unhappiness with YNAB: It is brittle and it feels unstable and uncertain.

The brittle part is probably not the fault of the folks at YNAB. Every personal finance software I've tried that has imported transactions from financial institutions has sucked, with the possible exception of manually downloading QFX files -- I remember those importing reliably.

But anything that connects directly to your bank or credit card and downloads transactions sucks. It's just not reliable. Accounts that used to work stop working. You have to notice and re-enter your credentials and then they generally start working again.

Transactions on my Amazon credit card used to show the item name in the memo field, which was awesome for approving transactions. Then the link to my card stopped working, and when I noticed and got it reconnected again, the memo field was blank on all new transactions.

I think the root cause of this is not YNAB's fault -- it's the banks with antiquated back-end systems that don't support this use case well, and they don't have much motivation to fix this. (I would switch to any bank that offered this as a competitive advantage.) At present my experience on Quicken or YNAB being bad doesn't hurt Synchrony one bit.

I do want to point out one thing the folks at YNAB could fix and certainly are responsible for -- when they know a financial institution won't work, they should tell you! I was doing a zoom demo of YNAB to a friend I had evangelized it to, and we thought we had successfully connected his bank. There were no transactions, but ... I assured him they would start showing up. But they didn't, and they didn't, and then we found on the status page that transactions with this bank were not working for a vast majority of customers and had not been for months. Obviously my friend didn't keep using YNAB, and I was really frustrated with how much of our time this had wasted. If we'd been told off the bat "You're probably going to have to manually enter transactions" we could have saved time and felt better about YNAB.

This leads me to the second major problem, which is entirely within YNAB's control -- it just doesn't feel stable. YNAB started out as a spreadsheet, but I knew it first as a standalone Mac app that was simply excellent. I'm sure there were faults that I've forgotten, but I remember it as solid, stable and delightful.

YNAB has switched from a model where you purchase software that you download and run on your computer to a SaaS model, where you use YNAB on their website, and pay a subscription. I Have no objection to the subscription, but the switch to SaaS has not been smooth. They had significant scaling problems at launch, specifically about their ability to ingest their desktop application's files as part of a one-time conversion. I remember this taking months to resolve, but scaling is hard, and I don't know enough to have an opinion on their design choices.

I know nothing about YNAB's infrastructure. The following is an accurate review of how using YNAB feels, plus speculation about their infrastructure. (I welcome facts from anyone in the know, and will publish either with or without attribution.)

Everything on YNAB feels like it's eventually correct. It feels like they run lots of stuff in batches rather than real time. Software, especially software dealing with money should be right all the time, and it should be instantly right. Anything less feels unstable and out of control. It kind of feels like they're running a bunch of individual versions of their old desktop product, but on resource-constrained servers on the web instead of your desktop.

Look at downloading transactions from financial institutions. This is not predictable. The more you use the site, the more frequently they seem to check for updates. So if you're using it daily, you'll log in and either see new transactions immediately or see new transactions a few minutes after you log in.

If you haven't used it for a few weeks though, it can show "no new transactions" for 45 minutes or more before they work their way through the queue and actually check for new data.

And telling you that there's updates is a little wonky too. There's a little white ball to the left of an account name that shows up when there are transactions that need to be approved or that need to be imported. What's supposed to happen is that you click the account with the white ball, and then on that account screen there's a header bar that tells you there's X new transactions to import. Clicking the header shows you the list of transactions to approve. Lots of times that header bar isn't there. 

Only recently did I realize there's a little "import" button near the top of the screen and it's **optional.** If you never press it, eventually the transactions will be imported and you'll see the header bar announcing the new transactions. But if the white ball is lit up but the header bar is not there, you can press the "import" button and it will import the new transactions. Most of the time. Sometimes the white ball won't go away no matter what you do. I strongly suspect that I have not captured how this whole white-dot-import business works internally -- I suspect the state machine here is very complicated.

Also you can import and categorize pending transactions, but you'll need to do it again when they stop being pending.

YNAB publishes a metric called "Age of Money" which is supposed to be how long you've had your money before you spend it. If you earn a dollar today and spend it today your AoM would be 0, but if you got paid last month and only spent that money for rent today, your AoM could be 30 days. I'm not convinced this is an important metric, but at a bare minimum it's fun to track. If your AoM is trending upward you're probably doing OK.

However, how your AoM is updated isn't OK. You'd think that you enter a transaction, and your AoM updates. Nope. It updates when it updates. This seems to be a queued job that executes every couple of days. Frequency seems to vary between 1.5 and 3 days between updates.

All of this is very frustrating and if there was anything I liked better than YNAB I'd switch in a heartbeat. But there doesn't seem to be anything better.