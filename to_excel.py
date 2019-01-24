import pandas as pd
data = {'B' : dict(col1=1), 'A' : dict(col1=2), 'C' :dict(col1=3, col2=4.1)}
df = pd.DataFrame.from_dict(data, orient='index')
df.to_excel('test1.xlsx', engine='xlsxwriter', as_table=True, index=True)
df.to_excel('test2.xlsx', engine='openpyxl', as_table=True, index=True)