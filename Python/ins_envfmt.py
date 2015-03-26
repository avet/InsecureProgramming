#!/usr/bin/env python
'''
AVET Information and Network Security Sp. z o.o. (In)secureProgramming series
WARNING: This code contains vulnerabilities and other defects. The purpose of this
code is to demonstrate insecure programming practices and provide examples for
testing static analysis methods. DO NOT RUN in production systems.
For more details please visit us at: www.avet.com.pl
Latest version of this code can be downloaded at: https://github.com/avet/InsecureProgramming 
'''

import sys


def show_usage():
    print 'Usage:', sys.argv[0], ' [options]'
    sys.exit(1)


def show_used_options():
    print 'Bad options used:',
    for arg in sys.argv[1:]:
        print arg,
    sys.exit(2)


def main():
    if len(sys.argv) < 2:
        show_usage()
    if len(sys.argv) != 3:
        show_used_options()

    sys.exit(0)

if __name__ == '__main__':
    main()
