import pandas as pd

df = pd.read_csv('xml2csv/NUSL.csv', sep=';', encoding="Windows-1250") #df = dataframe

print("záznamů celkem", len(df))
df.duplicated(subset='id', keep='first')
print("záznamů celkem", len(df))

df_missing_values = (df.isna().sum())
df_missing_values.to_csv('NUSL/missing_values.csv', sep=';', header=False)

#for index, row in df.iterrows():
#	print(index, row ['projects'])
#	hodí se, když se potřebuju podívat co je všechno v nějakém sloupci

#celkem 30 653

#úkol_1_a_2
df['task_1'] = 1
df['year2'] = df['year'].str[:4]
print(df['year2'])

task_1_df = df.groupby(['year2', 'no_of_projects']).count().astype('Int64')['task_1']
task_1_df.to_csv('NUSL/projekty_rok.csv', sep=';', header=True)

#úkol_2

df['task_2'] = 1
task_2_df = df.groupby(['langs', 'no_of_projects']).count()['task_2']
task_2_df.to_csv('NUSL/projekty_jazyk.csv', sep=';', header=True)
#1dok ve více jazycích

df['task_3'] = 1
task_3_df = df.groupby(['doc_type','no_of_projects']).count()['task_3']
task_3_df.to_csv('NUSL/projekty_doc_type.csv', sep=';', header=True)



#df.loc[~df['návaznosti'].str.contains('P')] - neobsahuje 'P'; ~ se píše alt a 1 na nenumerické klávesnici


"""

neopravovat a nesplitovat v rámci pole 999, ale říct, že tam takový problém je.
"""
