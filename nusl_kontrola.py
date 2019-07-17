import pandas as pd

df = pd.read_csv('E:/diplomka/praktická_část/xml2csv/NUSL.csv', sep=';', encoding="Windows-1250")
# , encoding="Windows-1250"

print("záznamů celkem", len(df), "ids", len(df['id']))

df2 = df.drop_duplicates(subset='id', keep='first')
print("záznamy po odstranění duplicit", len(df2))


df_missing_values = df.isna().sum()
df_missing_values.to_csv('výstupy/NUSL_csv/missing_values_NUSL.csv', sep=';', header=False)

df['langs'] = df['langs'].astype(str)
print(df.isna().sum())
