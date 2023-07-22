import pandas
import csv

df = pandas.read_csv('merged.csv')
print(df.shape)

del df['luminosity']
del df['radius']
del df['mass']
del df['distance']

df = df.rename({
    'distance_ly':'distance',
}, axis='columns')

df.to_csv('proj130cleaned.csv')

df = pandas.read_csv('proj130cleaned.csv')
print(df.shape)
