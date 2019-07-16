import pandas as pd

df = pd.read_csv('xml2csv/NUSL.csv', sep=';', encoding="Windows-1250") #df = dataframe

print("záznamů celkem", len(df))
df2 = df.drop_duplicates(subset='id', keep='first')
print("záznamy po odstranění duplicit", len(df2))


df_missing_values = (df.isna().sum())
df_missing_values.to_csv('NUSL/missing_values.csv', sep=';', header=False)
