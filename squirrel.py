import pandas as pd
sq=pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
"""for i in list(sq.columns):
    if 'Color' in i:
        print(i)"""

#df1=sq.groupby('Primary Fur Color').count()
df1=sq['Primary Fur Color']
print(type(df1))