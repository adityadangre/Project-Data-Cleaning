import csv 
import pandas as pd

df = pd.read_csv('final_stars.csv')

del df['']
del df['']
del df['Star_name']
del df['Distance']
del df['Mass']
del df['Radius']


df = df.rename({
    'Star_name' : 'star_name',
    'Distance' : 'distance',
    'Mass' : 'mass',
    'Radius' : 'radius',
    'Luminosity' : 'luminosity',
}, axis = 'columns')

df.to_csv('star_main.csv')