Title: How to Remove All Subversion Folders From A Directory Tree
Date: 2007-06-23 15:20
Tags: command line

Say you've got a
[Subversion](http://subversion.tigris.org/ "Subversion Version Control System")
source code tree checked out, and for whatever reason you want to remove
all Subversion directories inside that tree. (The thing that makes a
Subversion tree a Subversion tree is the presence of a ".svn" folder in
every folder of the tree. If you had a complicated source tree with lots
of subdirectories, it would take you forever to remove each one.) You
can remove all ".svn" directories starting below
"\~/svn/exampleproject" -- change this to suit your system -- with the
following command:

    :::bash
    find ~/svn/exampleproject -name ".svn" -exec rm -rf {} ;

To make sure that the above command is going to do what you want it to
do, you may want to first generate a list of what it will delete (I
highly recommend it).

    :::bash
    find ~/svn/exampleproject -name ".svn" -exec echo "rm -rf {}" ;
