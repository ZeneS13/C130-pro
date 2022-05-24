import csv
import pandas as pd

df = pd.read_csv("Data_merged.csv")


del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Unnamed: 0"]
del df["Unnamed: 5"]

df = df.rename({
    'StarName':"Star_name"
},axis='columns')

df.to_csv('final.csv')