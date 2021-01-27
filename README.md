schof.org
=========

Source for schof.org

SCHOFORGDIR="\~/code/me/schof.org"


cd $SCHOFORGDIR
./buildboxvm_start.bash

vagrant ssh
cd /vagrant
inv build  # to build
inv publish  # push to live site
