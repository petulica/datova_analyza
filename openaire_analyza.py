import pandas as pd

df = pd.read_csv('D:/diplomka/praktická_část/xml2csv/OpenAIRE.csv', sep=';', encoding="Windows-1250")

print("total no of records", len(df))
df = df.drop_duplicates(subset='id', keep='first')
print("no of records after dropping the duplicates", len(df))

#úkol_1_a_2
df['no_of_records'] = 1

task_1_df = df.groupby(['year', 'no_of_projects']).count().astype('Int64')['no_of_records']
task_1_df.to_csv('výstupy/OpenAIRE_csv/projects_year_OpenAIRE.csv', sep=';', header=True)

#úkol_2
task_2_df = df.groupby(['langs', 'no_of_projects']).count()['no_of_records']
#task_2_df.loc[task_2_df['langs'].len() > 3] = :2
task_2_df.to_csv('výstupy/OpenAIRE_csv/projects_langs_OpenAIRE.csv', sep=';', header=True)

#úkol_3
task_3_df = df.groupby(['doc_type','no_of_projects']).count()['no_of_records']
task_3_df.to_csv('výstupy/OpenAIRE_csv/projects_doc_type_OpenAIRE.csv', sep=';', header=True)

print(df.tail())
print(len(df))
print(df.isna().sum())
