# -*- coding: utf-8 -*-
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