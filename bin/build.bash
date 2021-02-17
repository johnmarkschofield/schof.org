#!/bin/bash

./update_dev_server.bash
ssh schof@utility.schof.in "cd schof.org ; inv build"
scp schof@utility.schof.in:~/schof.org/requirements.txt .