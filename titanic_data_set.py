import pandas as pd
data_set= pd.read_csv('titanic.csv')  # ds = data set
print('first 5 rows of the ds')
print(data_set.head())     # .head desplays only five iterms in the list
print(data_set.info())
print(data_set.describe())