#!/usr/bin/env python2

# Note that there is no error checking

import sys

argv = sys.argv
argc = len(argv)

if argc != 2:
    print 'Usage: ', argv[0], ' [hex string]'

h = argv[1]

print h.decode('hex').encode('base64')
