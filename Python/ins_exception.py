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

data = ''

try:
    fin = open(sys.argv[1], 'r')
    data = fin.readlines()
    fin.close()
except:
    pass

print 'Data size = ', len(data)
