#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2 # in python3 urllib2 was splited
import lxml.html

BASE_PATH = '/html/body/div[@id="container"]/div[@id="main"]/'

def word_search(word):
    f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=%s' % word)
    doc = lxml.html.document_fromstring(f.read())

    WORD_NOT_FOUND = ''

    if doc.xpath(BASE_PATH + 'div[@id="ajax_search"]/descendant::div[@class="margin_left"]/noindex/div[@class="green pt12"]/text()') == [u'Такого слова нет ']:
        WORD_NOT_FOUND = u'Такого слова нет'

    #print f.read()
    #f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=遥远工作')
    #f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=遥远')

    chin = ""
    rus = ""
    #table = ""

    if WORD_NOT_FOUND:
        num = 1
        while True:
            chinese = doc.xpath('%sdiv[@id="ajax_search"]/div[@class="margin_left"]/table/tr[@class="vtop"]/td[%s]/div[@class="ch2"]/a[@class="black"]/text()' % (BASE_PATH, num))
            pinyin = doc.xpath('%sdiv[@id="ajax_search"]/div[@class="margin_left"]/table/tr[@class="vtop"]/td[%s]/div[@class="py2"]/text()' % (BASE_PATH, num))
            russian = doc.xpath('%sdiv[@id="ajax_search"]/div[@class="margin_left"]/table/tr[@class="vtop"]/td[%s]/div[@class="ru"]/div/text()' % (BASE_PATH, num))
            examples = doc.xpath('%sdiv[@id="ajax_search"]/div[@class="margin_left"]/table/tr[@class="vtop"]/td[%s]/div[@class="ru"]/div[@class="m2"]/div[@class="ex"]/text()' % (BASE_PATH, num))
            for ch in chinese:
                for py in pinyin:
                    print ch, py
                    for ru in russian:
                        print ru
                    #print '\n'
                    print 'Примеры:'
                    for ex in examples:
                        print ex
            num += 1
            if not russian:
                break
            print '\n'
    else:
        chin = doc.xpath(BASE_PATH + 'div[@id="ch"]/text()')
        #rus = doc.xpath(BASE_PATH + 'div[@class="ru"]/text()')
        rus = doc.xpath(BASE_PATH + 'div[@class="ru"]/div/text()')

        print "%s: %s" % (word, WORD_NOT_FOUND)
        for i in rus:
            print i
