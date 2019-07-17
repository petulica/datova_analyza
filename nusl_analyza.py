import pandas as pd

df = pd.read_csv('E:/diplomka/praktická_část/xml2csv/NUSL.csv', sep=';', encoding="Windows-1250")

print("total no of records", len(df))

#úkol_1_a_2
df['no_of_records'] = 1

df['year2'] = df['year'].str[:4]
print(df['year2'].tail())
task_1_df = df.groupby(['year2', 'no_of_projects']).count().astype('Int64')['no_of_records']
task_1_df.to_csv('výstupy/NUSL_csv/projekty_rok_NUSL.csv', sep=';', header=True)

#úkol_2
df['langs'] = df['langs'].astype(str)
task_2_df = df.groupby(['langs', 'no_of_projects']).count()['no_of_records']
task_2_df.to_csv('výstupy/NUSL_csv/projekty_jazyk_NUSL.csv', sep=';', header=True)
#1dok ve více jazycích

task_3_df = df.groupby(['doc_type','no_of_projects']).count()['no_of_records']
task_3_df.to_csv('výstupy/NUSL_csv/projekty_doc_type_NUSL.csv', sep=';', header=True)

print(df.tail())
print(df.isna().sum())
