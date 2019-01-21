from matplotlib import pyplot as plt
import pandas as pd
df=pd.read_csv("wh.csv")

print df.head()
df=pd.DataFrame(df.values,columns=['date','state','mon','yr','price'])

print df.head()
df['time']=df['yr']*4*12+df['mon']*4+df['date']

print df.head()
df=df.sort_values(['time'])

print df.head()

data=pd.DataFrame(df[['date','state','time','price']],columns=['date','state','time','price'])
print data.describe()
series=data[data['state']==0]

series= series[['time','price']]
print series.head
#series.plot()
"""
plt.plot(series['time'],series['price'])

series=data[data['state']==0]

series= series[['time','price']]
"""
val=series['price'].values
print len(val)
avg=[]
i=0
while i < 282:
		avg.append(sum(val[i:i+5])/5)
		i+=5
print series.shape	
plt.plot(range(len(avg)),avg)
plt.show()