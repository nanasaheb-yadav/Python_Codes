import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")
print(df.columns)
# Below are quick example
#Repalce NaN with zero on all columns
df2 = df.fillna(0)

#Repalce inplace
df.fillna(0,inplace=True)

# Replace on single column
df["country"] = df["country"].fillna(0)

# Replace on multiple columns
df[["country","touristArrivals"]] = df[["country","touristArrivals"]].fillna(0)

# Using replace()
df["country"] = df["country"].replace(np.nan, 0)

# Using replace()
df2 = df.replace(np.nan, 0)


