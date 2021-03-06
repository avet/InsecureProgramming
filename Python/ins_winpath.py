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

filename = sys.argv[1] + '\\' + sys.argv[2]

if os.path.isfile(filename):
    print filename, 'exists'
else:
    print filename, 'not found'


