import pandas as pd
a=pd.read_csv("file.csv")
#print a.values
#a=pd.DataFrame(data=a.iloc[:,1:])
import sklearn
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
enc = OneHotEncoder()
enc.fit(a.iloc[:,:2])
soilcrop=enc.transform(a.iloc[:,:2]).toarray()
#print soilcrop.shape
#print a.iloc[:,2:4].values.shape
p=pd.DataFrame(data=soilcrop)
q=pd.DataFrame(data=a.iloc[:,2:4].values)
data_x=pd.concat([p,q],axis=1)
#print data_x
#print data_x.shape
data_y=a.iloc[:,4]
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
"""from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM"""
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


(trainData, testData, trainLabels, testLabels) = train_test_split(data_x, data_y, test_size=0.20, random_state=42)
"""clf=LinearRegression()
clf.fit(trainData.values,trainLabels.values)
val=clf.score(testData.values,testLabels.values)
print val
look_back = 1"""

"""
model = Sequential()
model.add(LSTM(4, input_shape=(None,20)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainData.values,trainLabels.values, epochs=100, batch_size=1, verbose=2)
"""
"""
regr = RandomForestRegressor(max_depth=2, random_state=0)
regr.fit(trainData.values,trainLabels.values)
val=regr.score(testData.values,testLabels.values)
print val

regr = LogisticRegression()
regr.fit(trainData.values,trainLabels.values)
val=regr.score(testData.values,testLabels.values)
print val
"""
from sklearn.ensemble import GradientBoostingRegressor
regr = GradientBoostingRegressor()
regr.fit(trainData.values,trainLabels.values)
val=regr.score(testData.values,testLabels.values)
#print val
ff=enc.transform([[3,4]]).toarray()
#print ff
#print np.append(ff,[1,3])
gg=regr.predict([np.append(ff,[1,3])])
#print gg

cost=pd.read_csv("cost.csv")
comp=[0,1,2,3,4,5,6,7,8]
cropsi=[0,3,4,5,6,12,1,2,13]
cropsm=[3,7,0,8,10,4,2,1,6]

def getprofit(cropsindex):
	ff=enc.transform([[cropsi[cropsindex],3]]).toarray()
	
	month=cost.iloc[1+cropsm[cropsindex],4]
	sell=regr.predict([np.append(ff,[(4+month//2)%6,2+(4+month//2)//6])])
	cp=cost.iloc[1+cropsm[cropsindex],1]
	y=cost.iloc[1+cropsm[cropsindex],3]
	profit=sell*y-cp
	return cp

