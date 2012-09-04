#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2 # in python3 urllib2 was splited
import lxml.html

def word_search(word):
    f = urllib2.urlopen('http://bkrs.info/slovo.php?ch=%s' % word)
    doc = lxml.html.document_fromstring(f.read())

    WORD_NOT_FOUND = ''

    if doc.xpath('//div[@id="ajax_search"]/descendant::div[@class="margin_left"]/noindex/div[@class="green pt12"]/text()') == [u'Такого слова нет ']:
        WORD_NOT_FOUND = u'Такого слова нет'

    translate = u''
    word = word.decode('utf-8')
    if WORD_NOT_FOUND:
        #print "Word not found"
        num = 1
        #print word, WORD_NOT_FOUND
        translate += '[=== %s: %s ===]\n\n' % (word, WORD_NOT_FOUND)
        #print '\n'
        while True:
            chinese = doc.xpath('//div[@id="ajax_search"]/div[@class="margin_left"]/table/tr[@class="vtop"]/td[%s]/div[@class="ch2"]/a[@class="black"]/text()' % (num))
            pinyin = doc.xpath('//div[@id="ajax_search"]/div[@class="margin_left"]/table/tr[@class="vtop"]/td[%s]/div[@class="py2"]/text()' % (num))
            russian = doc.xpath('//div[@id="ajax_search"]/div[@class="margin_left"]/table/tr[@class="vtop"]/td[%s]/div[@class="ru"]/div/text()' % (num))
            examples = doc.xpath('//div[@id="ajax_search"]/div[@class="margin_left"]/table/tr[@class="vtop"]/td[%s]/div[@class="ru"]/div[@class="m2"]/div[@class="ex"]/text()' % (num))
            for ch in chinese:
                for py in pinyin:
                    #print ch, py
                    translate += '-- %s %s --\n' % (ch, py)
                    for ru in russian:
                        #print ru
                        ### TODO: Add `text_content()` to get all the contents of the russian translation
                        translate += '%s\n' % (ru)
                    #print '\n'
                    #print 'Примеры:'
                    translate += '\nExamples:\n'
                    for ex in examples:
                        #print ex
                        translate += '%s\n' % (ex)
            num += 1
            if not russian:
                break
            #print '\n'
            translate += '\n'
            #print '====================================='
            #print translate
    else:
        print "Word found"
        pinyin = doc.xpath('//div[@class="py"]/text()')
        rus_single = doc.xpath('//div[@class="ru"]/text()') # checking whether searched word has many meanings or not. If it is, we show rus_full, if it's not, we show rus_single
        rus_full = doc.xpath('//div[@class="ru"]/*[not(@class="ex")]')
        examples = doc.xpath('//div[@class="ru"]/div[@class="m2"]/div[@class="ex"]')

        #print u'%s: %s' % (word, pinyin[0].strip())
        translate += u'%s: %s\n' % (word, pinyin[0].strip())

        if rus_single[0].strip():
            #print rus_single[0]
            translate += '%s\n' % (rus_single[0])
        else:
            #print "No rus"
            for ru in rus_full:
                #print ru.text_content()
                translate += '%s\n' % (ru.text_content())
            for ex in examples:
                #print ex.text
                translate += '%s' % (ex.text)
    print translate.encode('utf-8')
