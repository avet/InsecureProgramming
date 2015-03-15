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

import tempfile
import sqlite3


def main():
    print 'Using %s as temp directory' % tempfile.gettempdir()
    tmp_filename = tempfile.mktemp()
    print 'Using %s as temp filename' % tmp_filename
    if os.path.isfile(tmp_filename):
        print 'Temp file %s already exists.' % tmp_filename
    dbcon = sqlite3.connect(tmp_filename)
    dbcursor = dbcon.cursor()
    dbcursor.execute("create table users (username text, password text)")
    dbcursor.execute("insert into users values ('test-user','password')")
    dbcon.commit()

    dbcursor.execute("select * from users where username = '%s'" % sys.argv[1])
    dbcursor.close()
    dbcon.close()


if __name__ == '__main__':
    main()
