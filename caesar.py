#!/usr/bin/env python3

from sys import argv, exit
import string

def caesar(s, n):
    letters = string.ascii_uppercase
    out = ""
    for c in s:
        if c in letters:
            i = letters.index(c)
            ni = int((i + (n % len(letters))) % len(letters))
            out += letters[ni]
        else:
            out += c
    return out

if __name__ == '__main__':
    if len(argv) != 3:
        print('Usage: %s [input string] [key (as integer)]' % argv[0])
        exit(1)

    try:
        print(caesar(argv[1].upper(), int(argv[2])))
    except ValueError:
        print('Key must be an integer.')
        exit(1)
