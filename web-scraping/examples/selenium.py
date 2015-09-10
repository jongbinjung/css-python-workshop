# -*- coding: utf-8 -*-
"""
Web scraping with selenium webdriver

Requires selenium
    pip install selenium

@author: Jongbin Jung (jongbin at stanford edu)
"""

from selenium import webdriver


browser = webdriver.Firefox()

browser.get('http://webmail.stanford.edu')

for element in browser.find_elements_by_class_name('_xlv_S'):
    print element.text
