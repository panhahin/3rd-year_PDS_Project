import pandas as pd
import helpers as help

df = pd.read_csv("data/students.csv")
df = help.clean_data(df)
print(df)