import pandas as pd
import numpy as np

# 1. Dataset download & load
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Raw file save karo repo ke liye
df.to_csv("titanic_raw.csv", index=False)
print("Raw dataset saved as 'titanic_raw.csv'")

# 2. Duplicates check and remove
duplicates_count = df.duplicated().sum()
df = df.drop_duplicates()
print(f"Duplicates removed: {duplicates_count}")

# 3. Column names clean karo
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 4. Missing values handle karo
df['age'] = df.groupby('pclass')['age'].transform(lambda x: x.fillna(x.median()))
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
if 'cabin' in df.columns:
    df.drop(columns=['cabin'], inplace=True)

# 5. Data types standardize karo
df['survived'] = df['survived'].astype('int')
df['pclass'] = df['pclass'].astype('category')
df['sex'] = df['sex'].astype('category')
df['embarked'] = df['embarked'].astype('category')

# 6. Cleaned dataset export karo
df.to_csv("titanic_cleaned.csv", index=False)
print("Data Cleaning Complete! 'titanic_cleaned.csv' successfully created.")
