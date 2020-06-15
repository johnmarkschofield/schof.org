schof.org
=========

Source for schof.org

SCHOFORGDIR="\~/code/me/schof.org"


cd $SCHOFORGDIR
rmvirtualenv schof.org
mkvirtualenv schof.org -a `pwd`
pip install -r requirements_primary.txt

inv build  # to build
inv publish  # push to live site
