import pandas as pd

columns = ['Articolo','Citazioni']
df_complete = pd.read_csv('oci_raw_dataset.csv', usecols = columns)
df_complete['Citazioni'] = pd.to_numeric(df_complete['Citazioni'], downcast='unsigned')
# divido il dataframe in pezzi
n = 10000 
chunks = [df_complete[i:i + n] for i in range(0, df_complete.shape[0], n)]
del df_complete
del columns

columns_dblp = ['author','title','year','url','Articolo']
df_dblp = pd.read_csv('dblp_dataframe.csv', usecols = columns_dblp)
del columns_dblp
df_dblp['year'] = pd.to_numeric(df_dblp['year'], downcast='unsigned')



header = True
i =1
for chunk in chunks:
	df_merge_col = pd.merge(chunk, df_dblp, on='Articolo')
	print(f'Merge parziale n. {i} eseguito')
	i+=1
	df_merge_col.to_csv('complete_dataframe.csv', mode='a', header=header)
	header = False
