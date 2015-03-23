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
    if len(sys.argv) < 2:
        print 'Usage: %s filenames' % sys.argv[0]
    else:
        for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            try:
                filehash = hashlib.md5()
                fin = open(arg,'rb')
                buf = fin.read()
                filehash.update(buf)
                print '%s MD5 = ' % (arg, filehash.hexdigest())

if __name__ == '__main__':
    main()
