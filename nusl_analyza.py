import pandas as pd

df = pd.read_csv('xml2csv/NUSL.csv', sep=';', encoding="Windows-1250")

print("záznamů celkem", len(df))
df.duplicated(subset='id', keep='first')
print("záznamů celkem", len(df))

df_missing_values = (df.isna().sum())
df_missing_values.to_csv('NUSL_csv/missing_values_NUSL.csv', sep=';', header=False)


#úkol_1_a_2
df['no_of_records'] = 1
df['year2'] = df['year'].str[:4]
print(df['year2'])

task_1_df = df.groupby(['year2', 'no_of_projects']).count().astype('Int64')['no_of_records']
task_1_df.to_csv('NUSL_csv/projekty_rok_NUSL.csv', sep=';', header=True)

#úkol_2

df['no_of_records'] = 1
task_2_df = df.groupby(['langs', 'no_of_projects']).count()['no_of_records']
task_2_df.to_csv('NUSL_csv/projekty_jazyk_NUSL.csv', sep=';', header=True)
#1dok ve více jazycích

df['no_of_records'] = 1
task_3_df = df.groupby(['doc_type','no_of_projects']).count()['no_of_records']
task_3_df.to_csv('NUSL_csv/projekty_doc_type_NUSL.csv', sep=';', header=True)

# df.loc[~df['návaznosti'].str.contains('P')] - neobsahuje 'P'; ~ se píše alt a 1 na nenumerické klávesnici
# for index, row in df.iterrows():
# 	print(index, row ['projects'])
# 	hodí se, když se potřebuju podívat co je všechno v nějakém sloupci
