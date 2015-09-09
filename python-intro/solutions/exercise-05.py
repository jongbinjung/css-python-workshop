"""
Solution for Exercise 4 of the CSS Introduction to Python Workshop

@author: Jongbin Jung
"""
import pandas

data_src = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
wine_data = pandas.read_csv(data_src, sep=';')

# 1.
wine_data['sulfur difference'] = (
    wine_data['total sulfur dioxide'] - wine_data['free sulfur dioxide'])
wine_data.head()


# 2. 
wine_data.sort(columns='sulfur difference', ascending=False).iloc[0:10, :]


# 3.
wine_data.groupby('quality').mean().loc[:, 'sulfur difference']