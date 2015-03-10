#!/usr/bin/env python
'''
AVET Information and Network Security Sp. z o.o. (In)secureProgramming series
WARNING: This code contains vulnerabilities and other defects. The purpose of this
code is to demonstrate insecure programming practices and provide examples for
testing static analysis methods. DO NOT RUN in production systems.

For more details please visit us at: www.avet.com.pl
Latest version of this code can be downloaded at: https://github.com/avet/InsecureProgramming 
'''

import os
import sys
import hashlib


def main():
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            m = hashlib.md5()
            fin = open(arg, 'r')
            data = fin.read()
            m.update(data)
            print arg, ' ', m.hexdigest()


if __name__ == '__main__':
    main()

