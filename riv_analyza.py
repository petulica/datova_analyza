import pandas as pd

df = pd.read_csv('výstupy/RIV_csv/RIV_merged.csv', sep=';')

print("total no of records", len(df))

# spočítá projekty na výsledek a zapíše do nového sloupce
df['projects'] = df['projects'].astype(str)
df['no_of_projects'] = (df['projects'].str.count('P ')).astype('Int64')
df.to_csv('výstupy/RIV_csv/RIV_merged.csv', sep=';', index=False)

df['no_of_records'] = 1

#úkol_1_a_2
task_1_df = df.groupby(['year', 'no_of_projects']).count().astype('Int64')['no_of_records']
task_1_df.to_csv('výstupy/RIV_csv/projects_year_RIV.csv', sep=';', header=True)

#úkol_2
task_2_df = df.groupby(['langs', 'no_of_projects']).count()['no_of_records']
task_2_df.to_csv('výstupy/RIV_csv/projects_langs_RIV.csv', sep=';', header=True)

#ukol_3
df['doc_type2'] = df['doc_type2'].astype(str)
df['doc_type3'] = df['doc_type3'].astype(str)
task_3_df = df.groupby(['doc_type', 'doc_type2', 'doc_type3', 'no_of_projects']).count()['no_of_records']
task_3_df.to_csv('výstupy/RIV_csv/projects_doc_type_RIV.csv', sep=';', header=True)

print(df.tail())
print(df.isna().sum())

# task_5_df = df.groupby(['doc_type', 'no_of_projects']).count()['no_of_records']
# task_5_df.to_csv('RIV/projekty_doc_type.csv', sep=';', header=True)
#
# task_4_df = df.groupby(['doc_type', 'doc_type2', 'no_of_projects']).count()['no_of_records']
# task_4_df.to_csv('RIV/projekty_doc_type2.csv', sep=';', header=True)
