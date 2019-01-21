# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 12:32:25 2017

@author: pegasus
"""

import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

from sklearn.preprocessing import OneHotEncoder


import datetime

a = '2010-01-31'

#datee = datetime.datetime.strptime(datetime.datetime.today(), "%Y-%m-%d")


Month=int(datetime.datetime.today().month)-1
State=4
Soil=0

df = pd.read_csv("final.csv")

le = preprocessing.LabelEncoder()
l1 = df["Soil"]
le.fit(l1)
newsoil = le.transform(l1)
df["Soil"]=newsoil

l2 = df["Month"]
le.fit(l2)
df["Month"]=le.transform(l2)

l3 = df["State"]
le.fit(l3)
df["State"]=le.transform(l3)

#df=df.iloc[:,1:]
#print( df.iloc[1,1:].values)
df = pd.DataFrame(data = df.iloc[:,1:].values, columns=["Soil","Month","State","Rice","Wheat","Cotton","Sugarcane","Tea","Ragi","Maize","Millet","Barley"])

#print(df.iloc[::50,:3])
feat = pd.DataFrame({"Soil": df["Soil"], "Month" : df["Month"], "State": df["State"]})
labels = pd.DataFrame(data=df.iloc[:,3:],columns=["Rice","Wheat","Cotton","Sugarcane","Tea","Ragi","Maize","Millet","Barley"])
#print(df)
#from keras.utils import np_utils
from sklearn.model_selection import train_test_split

#print(enc.fit_transform([df['Soil'].values]).toarray())
(trainData, testData, trainLabels, testLabels) = train_test_split(feat, labels, test_size=0.25, random_state=42)
#print(trainData.values)


#model.fit(trainData.values, trainLabels.values, epochs=800, batch_size=10, verbose=1)

#(loss, accuracy) = model.evaluate(testData.values, testLabels.values,	batch_size=40, verbose=1)

#print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss,accuracy * 100))

#pred = model.predict_proba(testData.values)
#df = pd.DataFrame(pred, columns=["Rice","Wheat","Cotton","Sugarcane","Tea",	"Coffee","Cashew","Rubber","Coconut","Oilseed","Ragi","Maize","Groundnut","Millet","Barley"])
#print(df)
#df['image_name'] = test_id
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()

"""
from sklearn.ensemble import RandomForestClassifier
#clf = RandomForestClassifier(max_depth=2, random_state=0)
from sklearn.tree import ExtraTreeClassifier
#clf=ExtraTreeClassifier()
from sklearn.neural_network import MLPClassifier
#clf= MLPClassifier(max_iter=3000,hidden_layer_sizes=(20,80,150,30),learning_rate="adaptive",solver='sgd',
       learning_rate_init=0.01)
#clf=sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
"""
monlist=[4,3,7,0,8,6,5,1,11,10,9,2]
#stlist=[
#print clf
#print trainData.values, trainLabels.values
clf = clf.fit(trainData.values, trainLabels.values)
val =clf.score(testData.values,testLabels.values)
soillist=[0,5,1,4,3,2]
#al red bla mou	l	des
def getcrops(Soil,Month=Month,State=State):
	#print Soil, Month, State
	try:
		hari=df[df["State"]==State][df["Soil"]==Soil][df["Month"]==monlist[Month]].values[0][3:]
		#print "found"
	except: 
		try:
			hari=df[df["State"]==State][df["Soil"]==Soil][df["Month"]==monlist[(Month+1)%12]].values[0][3:]|df[df["State"]==State][df["Soil"]==Soil][df["Month"]==monlist[(Month-1)%12]].values[0][3:]
		except:
			#print Soil,monlist[Month],State
			hari=clf.predict([[Soil,monlist[Month],State]])
	return hari









"""
newhh=df[['image_name','Type_1','Type_2','Type_3']]
newhh.to_csv('submission.csv', index=False)
"""
