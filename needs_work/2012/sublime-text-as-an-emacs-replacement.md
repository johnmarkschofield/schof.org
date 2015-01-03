Title: Sublime Text as an Emacs Replacement
Date: 2012-08-23 10:15
Author: schof
Category: Linux/Unix, OS X, Python Programming, Technology
Slug: sublime-text-as-an-emacs-replacement

I've been an [Emacs](http://www.gnu.org/software/emacs/) guy for a
while, for the following reasons:

1.  You should pick one editor, and learn it deeply.
2.  Emacs works [on my OS X desktops](http://emacsformacosx.com/) and on
    the Linux/Unix computers I SSH to. This means I can use the same
    keyboard commands to edit text locally and over an SSH connection to
    another computer -- giving me added benefits from learning Emacs
    deeply.
3.  Emacs can be modified using Emacs-Lisp (a dialect of Lisp). This
    creates a [virtuous
    circle](http://en.wikipedia.org/wiki/Virtuous_circle_and_vicious_circle) where
    your use of Emacs allows you to tailor Emacs to you better, which
    allows you to better use Emacs to tailor Emacs to you better, until
    the end result is that you've got an editor perfectly adapted to you
    and your use case.

However, there's one big problem -- I haven't learned Emacs Lisp to the
point where I can actually do interesting work with it. I started by
copying and pasting snippets of other people's Emacs config files, and
graduated to making changes and troubleshooting my own -- but I never
got deeply enough into Emacs that I was able to reap the benefits of its
customization.

When I heard about [Sublime Text](http://www.sublimetext.com/) I was
interested -- [some people I respect seem to like
it](http://www.marco.org/2012/08/10/next-text-editor) -- and when I
heard it was customizable like Emacs, but in the Python language, I was
hooked. I use Python daily, so the barrier to entry for me hacking into
Sublime Text is much lower.

There are a few major downsides to Sublime Text, though. First, it's not
free in any sense -- it's not open source, like Emacs, [and it costs
\$59](http://www.sublimetext.com/buy). The \$59 cost isn't much of an
issue (especially since it allows you to test it out thoroughly before
buying it) but the lack of open source is. Emacs will never die. If
Richard Stallman, [the original author of
Emacs](http://en.wikipedia.org/wiki/Emacs#History), is hit by a bus,
Emacs will be almost completely unaffected. Other people have the source
code and will continue updating Emacs. If Jon Skinner, the author of
Sublime Text, is hit by a bus, all development on Sublime Text may stop.
A program that isn't actively developed will soon cease to be useful --
programs are like sharks; when they stop moving they die.

Since the whole point of learning an editor is so that you can invest
time in it to build skill and knowledge, and then have that investment
pay off over time, the lack of open source for Sublime Text is a
significant stumbling block. There's lots of other reasons Sublime Text
may go away, even discounting buses -- the company could be bought by
Google and the product shelved; the author may stop putting effort into
it; it may be that editors are a bad business and sales can't support
the author and his family -- there's a variety of reasons Sublime Text
may go away. Still, I'm drawn enough by the idea of modifying Sublime
Text in Python that I'm giving it a try. Here's my current setup:

1.  Install [Sublime Text](http://www.sublimetext.com/2)
2.  [Use DropBox to store your Sublime Text
    config](http://wheels.onebuttonapps.net/2012/04/use-dropbox-to-store-your-sublime-text-2-settings/).
    (Except that I used one symlink to the "Sublime Text 2" folder
    rather than 3 symlinks.)
3.  Install [Sublime Package
    Control](http://wbond.net/sublime_packages/package_control/installation) using
    the installation instructions for the CTRL-\` shortcut.
4.  Install git and subversion packages using Sublime Package Control
5.  Install
    [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) via
    Sublime Package Control
6.  [Commit your Sublime Text 2 config files to
    github](http://www.sublimetext.com/forum/viewtopic.php?f=3&t=3259).

This still leaves me with [one problem I haven't resolved yet --
replicating Emacs' tab
behavior.](http://sublimetext.userecho.com/topic/123604-emacs-like-indentation/)In
Emacs, I can do the following:

1.  If I hit TAB with the cursor placed anywhere on a line in Emacs, the
    whole line will indent. If I hit TAB with the cursor placed in the
    middle of a line in Sublime Text, it will insert a tab (or spaces)
    in the middle of the line.
2.  If I hit TAB repeatedly on a line in Emacs, it will cycle through
    the possible legal Python indentations for that spot in the code. If
    I hit TAB repeatedly on a line in Sublime Text, it will repeatedly
    indent the line.

Thus far, I haven't been able to reproduce that behavior in Sublime
Text. This may be a deal-breaker. I'm going to work with it for a little
longer to see if there's any other deal-breakers, or if I can get used
to doing indentation Sublime Text's way.

**UPDATE**:
[Solved](http://sublimetext.userecho.com/topic/123604-emacs-like-indentation/).
At least, partially. With Shift-TAB and TAB I can cycle through possible
indentations (including illegal ones). It's enough to keep me in Sublime
Text. I've added [my Sublime Text config to
Github](https://github.com/johnmarkschofield/sublime_text_config), so
feel free to take a look.

