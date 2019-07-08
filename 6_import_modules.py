#!/bin/sh
''''which python3 >/dev/null 2>&1 && exec python3 "$0" "$@" # '''
''''which python2 >/dev/null 2>&1 && exec python2 "$0" "$@" # '''
''''which python  >/dev/null 2>&1 && exec python  "$0" "$@" # '''
''''exec echo "Error: I can't find python anywhere"         # '''

import sys
print (sys.argv)

#import PyMySQL
#import math

#db=PyMySQL.connect(passwd="moonpie",db="thangs")

#print (math.e)
#print (math.pi)

