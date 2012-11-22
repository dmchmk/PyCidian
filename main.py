#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import sys, urllib2
#from plugins import bkrs
from plugins import zhonga

string = u''
string = sys.stdin.read()

f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=%s' % string)
#print f.read()

#f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=遥远工作')
#f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=遥远')

#bkrs.word_search(string.strip('\n'))
zhonga.word_search(string.strip('\n'))

#print string.strip('\n')
