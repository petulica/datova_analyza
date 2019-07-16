import pandas as pd

df = pd.read_csv('H:/datova_analyza/xml2csv/OpenAIRE.csv', sep=';', encoding="utf-8") #Windows-1250

print(len(df))
print(len(df['id'])) #kontrola chybějících hodnot v id

print(df.tail())


df_missing_values = (df.isna().sum())
df_missing_values.to_csv('H:/datova_analyza/výstupy/OpenAIRE_csv/missing_values.csv',
sep=';', encoding="utf-8", header=False)

#první zobrazení duplicit
dup_ids = df.pivot_table(index=['id'], aggfunc='size')
#print(dup_ids)
print(df.duplicated(subset='id', keep='first'))

#druhé zobrazení duplicit
dup_ids_druhy= pd.concat(g for _, g in df.groupby("id") if len(g) > 1)
print(dup_ids_druhy)

#zahození duplicit v novém df
df2 = df.drop_duplicates(subset='id', keep='first')
print(len(df2))
