import pandas as pd

df = pd.read_csv('RIV/RIV_merged.csv', sep=';')

print("záznamů celkem", len(df))

print(df_missing_values = (df.isna().sum()))
#vytiskne chybějící hodnoty pro kontrolu, že už žádné nechybí

df['no_of_projects'] = (df['projects'].str.count('P ')).astype('Int64')
df.to_csv('RIV/RIV_merged.csv', sep=';', index=False)


#úkol_1_a_2
df['task_1'] = 1
task_1_df = df.groupby(['year', 'no_of_projects']).count().astype('Int64')['task_1']
task_1_df.to_csv('RIV/projekty_rok.csv', sep=';', header=True)

#úkol_2

df['task_2'] = 1
task_2_df = df.groupby(['langs', 'no_of_projects']).count()['task_2']
task_2_df.to_csv('RIV/projekty_jazyk.csv', sep=';', header=True)

df['task_3'] = 1
task_3_df = df.groupby(['doc_type', 'doc_type2', 'doc_type3', 'no_of_projects']).count()['task_5']
task_3_df.to_csv('RIV/projekty_doc_type.csv', sep=';', header=True)


# df['task_3'] = 1
# task_3_df = df.groupby(['doc_type', 'no_of_projects']).count()['task_3']
# task_3_df.to_csv('RIV/projekty_doc_type.csv', sep=';', header=True)
#
# df['task_4'] = 1
# task_4_df = df.groupby(['doc_type', 'doc_type2', 'no_of_projects']).count()['task_4']
# task_4_df.to_csv('RIV/projekty_doc_type2.csv', sep=';', header=True)
