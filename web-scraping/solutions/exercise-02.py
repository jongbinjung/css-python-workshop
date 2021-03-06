# -*- coding: utf-8 -*-
"""
Web scraping script using requests and bs4

Requires
    BeautifulSoup(http://www.crummy.com/software/BeautifulSoup)
        pip install beautifulsoup4
            or
        easy_install beautifulsoup4
    Requests(http://docs.python-requests.org/)
        pip install requests
            or
        easy_install requests

    This will collect and print
    {Movie Title}   {Released Year}    {Gross Box Office Income}
    for the each of the top 250 movies in the IMDb Top comedy

@author: Jongbin Jung (jongbin at stanford edu)
"""

from time import sleep
from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    base_url = 'http://www.imdb.com/search/title'

    # loop over the pages with the start parameter
    for start in range(1, 250, 50):
        # Use requests to set URL with params and load
        params = {'genres': 'comedy',
                  'sort': 'boxoffice_gross_us',
                  'start': start}
        sleep(3)  # sleep before calls
        page = requests.get(base_url, params=params)

        # Parse the html content of the web page with BeautifulSoup
        soup = BeautifulSoup(page.content)

        for movie in soup.find('table', class_='results').find_all('tr'):
            try:
                title = movie.find('td', class_='title').a.text
                year = (movie.find('td', class_='title')
                             .find('span', class_='year_type')
                             .text)
                gross = movie.find('td', class_='sort_col').text

                print title, year, gross
            except AttributeError:
                pass
