#exploratory data analysis of the first test data set 

import pandas as pd

data_location = r"C:\Users\perez\OneDrive\Documents\Professional\EuropeDataSystem\DataQualityAnalyzer\data\monthly_hourly_load_values_2025.csv"
df = pd.read_csv(data_location, sep="\t")

with open(data_location ,"r", encoding='utf-8') as file:
    print(repr(file.readline()))

print(df.head(10))

print(df.shape)

print(df.columns)

print(list(df.columns))
