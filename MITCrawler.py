#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import *
import urllib2
import mechanize
import cookielib
import time
import random

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

linkIndex = 0
limit = 300

while linkIndex < limit:
	br.open('https://my.mit.edu/uaweb/guestbook.htm?_flowId=guestbook-flow')
	#soup = BeautifulSoup(br.response().read())

	link = br.find_link(text='Show All')
	br.follow_link(link)

	br.response().read()

	listOLinks = br.links()

	secondLinkList = []

	for link in listOLinks:					#move links from an iterator to a list
		secondLinkList.append(link)
		
	limit = len(secondLinkList)				#make sure we get everyone
	
	for g in range(linkIndex,len(secondLinkList)):
		link = secondLinkList[g]
		try:
			if(link.attrs[1][1]=='guestbooklinkname'):
				br.follow_link(link)
				soup = BeautifulSoup(br.response().read())
				anchor = soup.find("span",{"class":"guestbooknamelabel"}).parent
				if(len(anchor.contents[6])>1):						#cuts empty messages
					print anchor.contents[6][25:][:-21].replace("&#039;","'").replace("&amp;","&")	#looks nicer
				linkIndex+=1
		except IndexError:
			print "index error"
		except AttributeError:
			if(link.attrs[1][1]=='guestbooklinkname'):
				br.follow_link(link)
				print linkIndex							
			break
		except UnicodeEncodeError:
			linkIndex+=0
		
