#pip install pandas-profiling==2.7.1
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('Automobile.csv')
print(df.head())
profile = ProfileReport(df)
profile.to_file(output_file="Automobile.html")
