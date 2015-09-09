# -*- coding: utf-8 -*-
""" Web scraping script using requests and bs4
    Used for web scraping tutorial session by the Stanford Data Science
    Drop-in. February 2, 2015.

    Requires:
    BeautifulSoup(http://www.crummy.com/software/BeautifulSoup)
        pip install beautifulsoup4
            or
        easy_install beautifulsoup4
    Requests(http://docs.python-requests.org/)
        pip install requests
            or
        easy_install requests

    This will use some basics of BeautifulSoup to explore the source (html) of
    the BeautifulSoup website itself!
    (http://www.crummy.com/software/BeautifulSoup/)
@author: Jongbin Jung (jongbin at stanford edu)
"""

from bs4 import BeautifulSoup
import requests

web_page = requests.get('http://www.crummy.com/software/BeautifulSoup/')

soup = BeautifulSoup(web_page.content)

# Read the first H1 tag (usually the 1st-level header, unless you're dealing
# with a rogue  web designer)
soup.h1

# return the first link (an a tag), get its address (href property)
soup.a
soup.a.get('href')

# find all the links in the document
soup.a.find_all('a')

# get all the link addresses using a for loop
for link in soup.a.find_all('a'):
    print link.get('href')

# or make a list of the addresses with list comprehension
addresses = [link.get('href') for link in soup.a.find_all('a')]
print addresses

