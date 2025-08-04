# Import Libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load Dataset

df = pd.read_csv("winequality-red.csv")
print("Initial Data : \n ", df.head())
print("\n Data Information \n")
df.info()

# Check for missing values

print("\n Missing Values\n",df.isnull().sum()) 

# We now visualize outliners

plt.figure(figsize=(12,6))
sns.boxplot(data=df,orient="h")
plt.title("Boxplot for outliers")
plt.show()

# Remove outliners 

def remove_outliers(df,column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

for col in df.columns[0:-1]:   # remove 'quality'
    df = remove_outliers(df,col)

# scale features

scaler = StandardScaler()
df[df.columns[0:-1]] = scaler.fit_transform(df[df.columns[0:-1]])

# Final View 

print("\n Cleaned Data Preview :\n",df.head())
print("\n Shape after cleaning :",df.shape)

# Heatmap generation

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(),annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


