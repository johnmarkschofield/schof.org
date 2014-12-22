Title: Google FTW: Fixing Arrow Problems in OS X Python
Date: 2007-11-15 17:38
Author: schof
Category: Python Programming, Technology
Tags: OS X, python
Slug: google-ftw-fixing-arrow-problems-in-os-x-python

I lived with it for ages. I tried to fix it on my own, by selecting
different emulation types. Finally I Googled for it. And [pretty much
instantly](http://forums.macosxhints.com/archive/index.php/t-64151.html)
[found the
answer](http://simplygenius.com/2005/08/readline-for-python-on-osx_30.html):

``` {lang="python"}
python `python -c "import pimp; print pimp.__file__"` -i readline
```

Moral? If at first you don't succeed, Google. If Google fails, try, try
again.

**Update:** And to make forward-delete work, [try
this.](http://www.macosxhints.com/article.php?story=20050525040921189)

