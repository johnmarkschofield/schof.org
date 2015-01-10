Title: Fixing Double-Click in Sublime Text
Date: Thu, 2015-01-08 20:39
Tags: productivity, programming, what i learned today, sublime text

I love the fact that in [iTerm 2](http://iterm2.com/), double-clicking a GUID or an IP address selects it.

However, it's been really irritating that in [Sublime Text 3](http://www.sublimetext.com/), that doesn't happen. Double-clicking the "192" in "192.168.1.1" selects only the "192."

I found the setting to change that in Sublime Text 3, and it's awesome.

The setting is called "word_separators." To get the current value, I hit CTRL-` to load the Sublime Text 3 console, and then entered:

    :::python
    view.settings().get('word_separators.')

Then I pasted that into Preferences.sublime-settings, and edited it to remove dashes and periods as word separators:

    :::json
    "word_separators": "/\\()\"':,;<>~!@#$%^&*|+=[]{}`~?"

Now Sublime Text is behaving the way I think it should.
