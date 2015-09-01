# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 15:58:42 2015

@author: jongbinjung
"""

from __future__ import print_function
import requests
from time import sleep
from random import uniform
import sys

def get_columns(inventory_item, cols):
    return [inventory_item[col] for col in cols]
        
years = ':'.join([str(y) for y in range(2000,2014)])

params = {
    'zipcode': '94305',
    'range': '100',
    'bodyTypes': '',
    'inventoryType': '',
    'mileageRange': '',
    'trims': '',
    'extColors': '',
    'intColors': '',
    'priceRange': '',
    'engineSize': '',
    'transmission': '',
    'driveTrain': '',
    'options': '',
    'pageNumber': '1',
    'pageSize': '500',
    'sortBy':'partner_code',
    'make': '',
    'model': '',
    'years': years
}

targets = [ # list of tuples (make, model)
    ('Acura', ''),
    ('Aston Martin', ''),
    ('Audi', ''),
    ('Bentley', ''),
    ('BMW', ''),
    ('Bugatti', ''),        
    ('Cadillac', ''),
    ('Chevrolet', ''),
    ('Dodge', ''),
    ('Ferrari', ''),
    ('Ford', ''),
    ('Honda', ''),
    ('Infiniti', ''),
    ('Lamborghini', ''),
    ('Lexus', ''),
    ('Maserati', ''),
    ('Tesla', ''),
    ('Toyota', ''),
    ('Volkswagen', '')
]

cols = ['type', 'year', 'make', 'model', 'trim', 'mileage', 'price']

base_url = 'http://www.edmunds.com/api/inventory/v3/upp/getInventories/?'

# print header row
print('\t'.join(cols), file=sys.stdout)

# iterate make/models
for make, model in targets:
    params['make'] = make
    params['model'] = model
    
    # request json file with GET    
    cars = requests.get(base_url, params=params).json()
    
    print('Collect data for', cars['totalCount'], make, 
          'entries', file=sys.stderr)
    
    # print tsv of columns
    for i in cars['inventory']: 
        print('\t'.join(get_columns(i, cols)), file=sys.stdout)

    r = uniform(5,10)
    print('sleep', r, file=sys.stderr)   
    sleep(r)