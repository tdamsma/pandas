import pandas as pd
data = {'B' : dict(col1=1), 'A' : dict(col1=2), 'C' :dict(col1=3, col2=4.1)}
df = pd.DataFrame.from_dict(data, orient='index')
df = df.fillna('')
df.to_excel('test2.xlsx', as_table=True)