#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import urllib2 # in python3 urllib2 was splited
import lxml.html

def word_search(word):
    f = urllib2.urlopen('http://www.zhonga.ru/search/?q=%s' % word)
    doc = lxml.html.document_fromstring(f.read())

    print doc
