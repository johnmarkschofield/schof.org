#!/bin/bash


/usr/bin/rsync -apv --exclude '.git*' ~/code/me/schof.org/ schof@utility.schof.in:~/schof.org/