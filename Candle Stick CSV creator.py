import pandas as pd
import numpy as np
df = pd.read_csv ("D:\Data Science\ADANIPORTS__EQ__NSE__NSE__MINUTE - Copy.csv") 
hRow = "timestamp,open,high,low,close,volume"
rdata = df.to_numpy()

tRow = rdata.shape[0] # total rows
bn = 5 #binning required...in multiple of records in csv(tRow)
rRow = tRow/bn  # total rows in output... non fractional INT
data = rdata.reshape(rRow,bn,6)

dates = data[:,-1,0:1].reshape(rRow)
o = data[:,1,1:2].reshape(rRow)
h = data[:,:,2:3].max(axis=1).reshape(rRow)
l = data[:,:,3:4].min(axis=1).reshape(rRow)
c = data[:,-1,4:5].reshape(rRow).reshape(rRow)
v = data[:,:,5:6].sum(axis=1).reshape(rRow)
newArray = np.array([dates, o, h,l,c,v]).T

np.savetxt("D:\Data Science\export.csv", newArray , delimiter=',', header=hRow, comments="", fmt='%s')
