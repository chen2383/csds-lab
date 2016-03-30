#!/usr/bin/env python

import sys

for line in sys.stdin:
	linenew = line.split()
    n = len(linenew)
    status = linenew[(n-1)]
    print '%s\t%s' % (status, 1) # str tab str