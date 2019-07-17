import pandas as pd

# with open('H:/datova_analyza/výstupy/RIV_csv/RIV_merged.csv') as f:
#     print(f)

df = pd.read_csv('./výstupy/RIV_csv/RIV_merged.csv', sep=';', warn_bad_lines=True, encoding="cp1250")

print(len(df))

df_missing_values = df.isna().sum()
df_missing_values['stav'] = 'první výsledek'
df_missing_values.to_csv('./výstupy/RIV_csv/missing_values_RIV.csv', sep=';', encoding="cp1250", header=False)

df2 = df.drop_duplicates(subset='id', keep='first')
print(len(df2))



with open ('./výstupy/RIV_csv/missing_values_RIV.csv', 'a') as f:
    df['doc_type2'] = df['doc_type2'].astype(str)
    df['doc_type3'] = df['doc_type3'].astype(str)
    df['projects'] = df['projects'].astype(str)
    df['no_of_projects'] = df['no_of_projects'].astype(str)
    df_missing_values_2 = df.isna().sum()
    df_missing_values_2['stav'] = 'opraveno'
    df_missing_values_2.to_csv(f, header = False, sep=';')

print( df.isna().sum())
