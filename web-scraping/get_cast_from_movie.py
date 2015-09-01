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

    This will collect and print  
    {Actor Name}    {Character Name}
    from the cast overview in a given IMDb.com movie page
@author: Jongbin Jung (jongbin at stanford edu)
"""
from bs4 import BeautifulSoup
import requests


def clean_text(text):
    """ Removes white-spaces before, after, and between characters

    :param text: the string to remove clean
    :return: a "cleaned" string with no more than one white space between
    characters
    """
    return ' '.join(text.split())


""" Go to the IMDb Movie page in link, and find the cast overview list.
    Prints tab-separated movie_title, actor_name, and character_played to
    stdout as a result.
"""
link = 'http://www.imdb.com/title/tt0111161/?ref_=nv_sr_1'
movie_page = requests.get(link)

# Strain the cast_list table from the movie_page
soup = BeautifulSoup(movie_page.content)

# Iterate through rows and extract the name and character
# Remember that some rows might not be a row of interest (e.g., a blank
# row for spacing the layout). Therefore, we need to use a try-except
# block to make sure we capture only the rows we want, without python
# complaining.
for row in soup.find_all('tr'):
    try:
        actor = clean_text(row.find(itemprop='name').text)
        character = clean_text(row.find(class_='character').text)

        print '\t'.join([actor, character])

    except AttributeError:
        pass
