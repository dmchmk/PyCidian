#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2, re
import lxml.html

f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=遥远工作')
#f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=遥远')

#print f.read()

doc = lxml.html.document_fromstring(f.read())

WORD_NOT_FOUND = doc.xpath('/html/body/div[@id="container"]/div[@id="main"]/div[@id="ajax_search"]/descendant::div[@class="margin_left"]/text()')

if WORD_NOT_FOUND:
    print "True"
    chin = doc.xpath('/html/body/div[@id="container"]/div[@id="main"]/div[@id="ajax_search"]/div[@class="margin_left"]/div[@id="ch"]/text()')
    #print chin[0]
    rus = doc.xpath('/html/body/div[@id="container"]/div[@id="main"]/div[@id="ajax_search"]/div[@class="margin_left"]/noindex/div[@class="green pt12"]/text()')
    #print rus[0]
else:
    chin = doc.xpath('/html/body/div[@id="container"]/div[@id="main"]/div[@id="ch"]/text()')
    rus = doc.xpath('/html/body/div[@id="container"]/div[@id="main"]/div[@class="ru"]/div/text()')
    print "False"

print "%s - %s" % (chin[0],rus[0])
