# -*- coding: utf-8 -*-
# install selenium with
#   $ pip install selenium
# in the command prompt

from selenium import webdriver
from bs4 import BeautifulSoup  # optional for bs4 implementation


def print_text(browser, class_='_xlv_S'):
    """Get list of senders from current browser view"""
    for element in browser.find_elements_by_class_name(class_):
        print element.text


def print_text_with_bs4(browser, class_='_xlv_S'):
    """Alternative implementation of get_senders with bs4"""
    html = browser.page_source
    soup = BeautifulSoup(html)
    for sender in soup.find_all('div', class_=class_):
        print sender.text

if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get('http://webmail.stanford.edu')

    # manually login from the browser

    print_text(browser)  # use default class_ for now
    print_text_with_bs4(browser)  # use default class_ for now

    # This is just an EXAMPLE of how to get a div scrolled.
    #   Note that it won't get the exact position/elements we require
    #   and further development into doing so would require more javascript,
    #   which is beyond the scope of this workshop.
    panes = browser.find_elements_by_class_name('scrollContainer')
    for pane in panes:
        if '_xlv_e1' in pane.get_attribute('class'):
            browser.execute_script('arguments[0].scrollTop = '
                                   'arguments[0].scrollHeight', pane)
