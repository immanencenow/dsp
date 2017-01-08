import pandas as pd
faculty = pd.read_csv('faculty.csv')
faculty['degree'] = faculty['degree'].str.replace(".","")
faculty2 = faculty.groupby(['degree']).size()
faculty2 = faculty2.to_frame()
faculty2 = faculty2.rename(columns={0: "freq"})
faculty2 = faculty2.reset_index()
faculty2 = pd.concat([pd.Series(row['freq'], row['degree'].split(' '))              
                   for _, row in faculty2.iterrows()]).reset_index()
faculty2 = faculty2.rename(columns={0: "freq"})
faculty2 = faculty2.rename(columns={'index': "degree"})
faculty2 = faculty2.groupby(['degree']).sum()
faculty2 = faculty2.reset_index()
faculty2.loc[faculty2.degree=='0', 'degree'] = 'No degree'
faculty2 = faculty2.sort_values(by = 'freq', ascending=0)
faculty2
