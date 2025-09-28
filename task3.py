import pandas as pd
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
print(df.head())
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
df.dropna(how='all', inplace=True)
df.columns = df.columns.str.strip()
str_cols = df.select_dtypes(include='object').columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())
df = df[(df['Sales'] >= 0) & (df['Profit'] >= 0)]
df.to_csv("Superstore_Cleaned.csv", index=False)
print("✅ Data cleaned and saved as 'Superstore_Cleaned.csv'")