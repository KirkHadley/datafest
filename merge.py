__author__ = 'kirk'

#datasets came in 3 separate csvs
#merged them into one her

import pandas as pd
first = pd.read_csv("/home/kirk/First37.csv")
second = pd.read_csv("/home/kirk/Second37.csv")
third = pd.read_csv("/home/kirk/Third36.csv")



combined = first.append(second)
combined = combined.append(third)
del first
del second
del third
combined.to_csv('/home/kirk/sets123.csv')

