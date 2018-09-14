#!/usr/bin/env python2

from sys import argv, exit
import os


def xors(a, b):
	out = ''
	if len(a) > len(b):
		a,b = b,a

	for i in xrange(len(a)):
		out += chr(ord(a[i]) ^ ord(b[i]))
	return out


if len(argv) != 4:
	print('Usage: %s [file1] [file2] [outfile]' % argv[0])
	exit(1)


if not os.path.exists(argv[1]):
	print('File %s does not exist' % argv[1])
	exit(1)

if not os.path.exists(argv[2]):
	print('File %s does not exist' % argv[2])
	exit(1)


with open(argv[1], 'rb') as f1:
	p1 = ''.join(f1.readlines())

with open(argv[2], 'rb') as f2:
	p2 = ''.join(f2.readlines())

out = xors(p1, p2)

with open(argv[3], 'wb') as fout:
	fout.write(out)

