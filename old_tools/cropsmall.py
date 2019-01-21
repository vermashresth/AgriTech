# -*- coding: utf-8 -*-
"""
Created on Sun May 21 13:11:03 2017

@author: pegasus
"""

import urllib
import pandas as pd
import numpy as np
import bs4 as bs
import re

df=pd.DataFrame(columns=[])
crop=[3,4,5,1]
state=['AP','AS','GJ','HR','HP','KK','KL','MP','MH','PB','TN','UP','WB','JR','UC']
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
yr=[2015,2016,2017]
fin=np.array([])
print (len(fin))
for p,i in enumerate(crop):
    for q,j in enumerate(state):
        for k,inn in enumerate(month):
            for r,w in enumerate(yr):
                if(p<8):
                    print ("http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity="+str(i)+"&Tx_State="+j+"&Tx_District=0&Tx_Market=0&DateFrom=01-"+month[k]+"-"+str(w)+"&DateTo=01-"+month[(k+1)%6]+"-"+str(w)+"&Fr_Date=01-"+month[k]+"-"+str(w)+"&ToDate=01-"+month[(k+1)%6]+"-"+str(w)+"&Tx_Trend=0&Tx_CommodityHead=Maize&Tx_StateHead=Haryana&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--")
                    sauce=urllib.request.urlopen("http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity="+str(i)+"&Tx_State="+j+"&Tx_District=0&Tx_Market=0&DateFrom=01-"+month[k]+"-"+str(w)+"&DateTo=01-"+month[(k+1)%6]+"-"+str(w)+"&Fr_Date=01-"+month[k]+"-"+str(w)+"&ToDate=01-"+month[(k+1)%6]+"-"+str(w)+"&Tx_Trend=0&Tx_CommodityHead=Maize&Tx_StateHead=Haryana&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--").read()
                    arr=[]
                    soup = bs.BeautifulSoup(sauce, 'lxml')
                    
                    for co in soup.find_all("span",{"id":re.compile('cphBody_GridPriceData_LabModalpric_*')}):
                           arr.append(int(str(co).split('>')[1].split('<')[0].split('.')[0]))
                    #print(arr)
                    if(len(arr)!=0):
                        print(sum(arr)/len(arr))
                        val=int(sum(arr)/len(arr))
                    else:
                        val=0
                    aa=np.array([p,q,k,r,val])
                    print(i,j,inn,w)
                    if len(fin)>0:
                        #print (fin)
                        print (np.array([aa]))
                        fin=np.append(fin,np.array([aa]),axis=0)
                    else:
                        print("hhh")
                        fin=np.array([aa])  
                    #print(fin)
                    if(len(fin)%50==0):
                        print (len(fin),len)
                        df=pd.DataFrame(data=fin)
                        print(df)
                        df.to_csv("file5.csv",index=False)
                    print (fin)
df=pd.DataFrame(data=fin)
print(df)
df.to_csv("fileshort.csv",index=False)
            
    