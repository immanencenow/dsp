import pandas as pd
import numpy as np
faculty = pd.read_csv('faculty.csv')
faculty['degree'] = faculty['degree'].str.replace(".","")
#faculty1 = pd.concat([pd.Series(row['degree'], row['name'].split(' '))              
                  # for _, row in faculty.iterrows()]).reset_index()
#faculty1
faculty2 = faculty.groupby(['degree']).size()
faculty2 = faculty2.to_frame()
faculty2 = faculty2.rename(columns={0: "freq"})
faculty2 = faculty2.reset_index()
faculty2 = pd.concat([pd.Series(row['freq'], row['degree'].split(' '))              
                   for _, row in faculty2.iterrows()]).reset_index()
faculty2 = faculty2.rename(columns={0: "freq"})
faculty2 = faculty2.rename(columns={'index': "degree"})
faculty2 = faculty2.groupby(['degree']).sum()
faculty2

