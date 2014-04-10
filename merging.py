__author__ = 'kirk'
import pandas as pd
details = pd.read_csv("/home/kirk/bldg_details.csv")
pre_install_details = pd.read_csv("/home/kirk/bldg_utility_pre_install.csv")
first = pd.read_csv("/home/kirk/First37.csv")
second = pd.read_csv("/home/kirk/Second37.csv")
third = pd.read_csv("/home/kirk/Third36.csv")



combined = first.append(second)
combined = combined.append(third)
del first
del second
del third
combined.to_csv('/home/kirk/sets123.csv')
