# -*- coding: utf-8 -*-
import requests

base_url = 'http://www.imdb.com/search/title'
params = {'genres': 'action', 'sort': 'moviemeter,asc'}

page = requests.get(base_url, params=params)
page.url
