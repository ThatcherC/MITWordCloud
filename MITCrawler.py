#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import *
import urllib2
import mechanize
import cookielib
import time

import settings

import codecs
import locale
import sys

# Wrap sys.stdout into a StreamWriter to allow writing unicode.
#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 
#-----------------------------------------

#set up BeautifulSoup and Mechanize
#Mechanize setup from: http://stackoverflow.com/questions/23102833/how-to-scrape-a-website-which-requires-login-using-python-and-beautifulsoup
cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_cookiejar(cj)

#sign in to MyMIT
br.open("https://my.mit.edu/uaweb/login.htm")
br.select_form(nr=0)
br.form['j_username'] = settings.creds['username']
br.form['j_password'] = settings.creds['password']
br.submit()

br.open('https://my.mit.edu/uaweb/guestbook.htm?_flowId=guestbook-flow')

#soup = BeautifulSoup(br.response().read())

br.find_link(text='Show All')
req = br.click_link(text='Show All')
br.open(req)



#nameLinks = soup.findAll('a')
#print nameLinks[31]
