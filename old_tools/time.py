from matplotlib import pyplot as plt
import pandas as pd
df=pd.read_csv("fileshort.csv")

print df.head()
df=pd.DataFrame(df.values,columns=['crop','state','mon','yr','price'])

print df.head()
df['time']=df['yr']*12+df['mon']

print df.head()
df=df.sort_values(['crop','state','time'])

print df.head()

data=pd.DataFrame(df[['crop','state','time','price']],columns=['crop','state','time','price'])
print data.describe()
series=data[data['crop']==0][data['state']==0]

series= series[['time','price']]
print series.head
#series.plot()
plt.plot(series['time'],series['price'])

series=data[data['crop']==0][data['state']==1]

series= series[['time','price']]
print series.shape	
plt.plot(series['time'],series['price'])
plt.show()