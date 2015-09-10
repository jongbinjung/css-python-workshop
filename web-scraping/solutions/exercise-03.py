# -*- coding: utf-8 -*-
"""
Web scraping with access to json api using requests

Requires
    Requests(http://docs.python-requests.org/)
        pip install requests
            or
        easy_install requests

    This will collect and print
    VIN, year, trim, mileage, price
    for all used cars available within 50 miles of specified
    zipcode, make, and model

@author: Jongbin Jung (jongbin at stanford edu)
"""

import requests


# set parameters
make = 'Honda'
model = 'Accord'
params = {
    'zipcode': '94305',
    'range': '50',
    'make': make,
    'model': model,
}

# specify the items we're interested in
keys = ['vin', 'year', 'trim', 'mileage', 'price']

base_url = 'http://www.edmunds.com/api/inventory/v3/upp/getInventories/?'

# request json file with GET
cars = requests.get(base_url, params=params).json()

# print tsv of columns
for car in cars['inventory']:
    print '\t'.join([car[key] for key in keys])

print 'Collected data for', cars['totalCount'], make, model, 'listings'