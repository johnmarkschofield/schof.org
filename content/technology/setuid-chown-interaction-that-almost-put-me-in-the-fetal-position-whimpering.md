Title: Setuid & Chown interaction that almost put me in the fetal position, whimpering
Date: 2007-10-18 22:43
Tags: linux, os x, command line

I'm putting together a postinst (post installation) script for a Debian
package I created for work. And there's a little C program in there that
needs to run as root, but be called by a regular user.

Well, there's a standard way of doing that in Linux/Unix, called setuid.
You set the "setuid bit" to on, and the program will run as the owner of
the program. So, since it's owned by root, a regular user can run a
particular program, and have that program run with the permissions that
root has. Very handy.

But I couldn't figure out why the program was not being installed setuid
root. I could see in the postinst script that the command was valid. I
could cut-and-paste the chmod line (that set the setuid bit) from the
script to the command-line, run it, and it worked perfectly. And there
weren't any other commands in the postinst script that affected
permissions (the setuid bit is a permission bit) for that file.

However, there WAS a chown command later in the script. (It started in a
parent directory and recursed into the directory with the C program I
was dealing with.) Eventually, I narrowed it down to that chown line,
and once I saw chown was the cause, I guess it sort of made sense. I was
able to reproduce the problem by chowning a file after setting the
setuid bit.

I guess from a security standpoint, you could do a lot of stupid things
by setting the setuid bit (making a program operate as the owner of the
program) and then changing the owner. So, to prevent you from shooting
yourself in the foot, changing ownership of a file unsets the setuid
bit.

Still, this seems somewhat counter to the philosophy of Unix -- first,
to not do unexpected things, and second, to give users approximately an
order of magnitude more rope than they'd need to hang themselves. I
can't think of many other commands that silently prevent you from doing
something that MAY be stupid. Unix usually assumes that you know what
you're doing -- even to the point that you can enter a command to delete
every file on your hard drive, and Unix will happily delete all your
files without asking for confirmation. The fact that chown has this
behavior was NOT obvious to me.

(This is a highly technical rant, and I'm writing it late at night after
coding for a while -- if it doesn't make any sense, it's probably me,
not you.)

