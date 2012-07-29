#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, urllib2
from plugins import bkrs

string = sys.stdin.read()

#f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=%s' % string)
#print f.read()

bkrs.word_search(string.strip('\n'))

#print string.strip('\n')
