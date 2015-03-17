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

link = br.find_link(text='Show All')
br.follow_link(link)

br.response().read()

listOLinks = br.links()

counter = 0

for link in listOLinks:
	counter+=1
	try:
		if(link.attrs[1][1]=='guestbooklinkname'):
			br.open(link.url)
			soup = BeautifulSoup(br.response().read())
			anchor = soup.find("span",{"class":"guestbooknamelabel"}).parent
			print anchor.contents[6][25:]
			#br.back()
	except:
		v = 1+1

print counter
