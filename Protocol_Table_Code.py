import pandas as pd
must = pd.read_csv('dump.csv', sep=',', header=0)
result = must.groupby(['Source', 'Protocol'])['No.'].count()
df = pd.DataFrame(result)
df = df.rename(columns = {'No.': 'Number'}) 
df.to_csv('dump2.csv')
print(result)
