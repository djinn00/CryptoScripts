#!/usr/bin/env python2

from sys import argv, exit
import string

def vigenere(s, key):
    letters = string.ascii_uppercase
    out = ""
    x = 0
    for c in s:
        if c in letters:
            i = letters.index(c)
            n = letters.index(key[x % len(key)])
            ni = int((i + (n % len(letters))) % len(letters))
            out += letters[ni]
            x += 1
        else:
            out += c
    return out

if __name__ == '__main__':
    if len(argv) != 3:
        print('Usage: %s [plaintext] [key]' % argv[0])
        exit(1)

    s = argv[1]
    key = argv[2]
    print vigenere(s.upper(), key.upper())

