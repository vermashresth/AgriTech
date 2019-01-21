import pandas as pd
df=pd.read_csv("file.csv")

print df.head()
df=pd.DataFrame(df.values,columns=['crop','state','mon','yr','price'])

print df.head()
df['time']=df['yr']*12+df['mon']

print df.head()
df=df.sort_values(['crop','state','time'])

print df.head()

data=pd.DataFrame(df[['crop','state','time','price']],columns=['crop','state','time','price'])
print data.describe()