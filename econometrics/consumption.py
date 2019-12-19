import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
import seaborn as sns
# Regression construction
lm = LinearRegression()
 
# Getting data and naming var
data = "F:\econometrics\Assign2\data1.csv"
df = pd.read_csv(data)

#Data Type
#print(df.dtypes)

#Summary Stat
#print(df.describe())

#Variables
x = df[['yt']]
y = df['ct']

lst1 = []
lst2 = []
lst3 = []
yhat = []
count = 0
# Regression Loop
for i in range(3, 201):
    a = x[:i]
    b = y[:i]
    #print(a)
    lm.fit(a, b)
    yhat = lm.predict(a)
    count = len(a)
    print("Number of Observations =",count)
    #print(type(yhat))
    #print(yhat)
    rmse = sqrt(mean_squared_error(a, yhat))
    inter = lm.intercept_
    cof = lm.coef_
    print("Intercept = ", inter)
    print("Coefficient =", cof)
    print("Standard Error =", rmse)
    print("_"*50)
    lst1.append(inter)
    lst2.append(cof)
    lst3.append(rmse)
   
print("_"*65)
print("Intercept: ", lst1)
print("_"*65)
print("Coefficient: ", lst2)
print("_"*65)
print("Standard Error: ", lst3)
print("_"*65)

#First Figure
plt.plot(lst3)
plt.ylabel('residual')
plt.show()
#Second Figure
plt.plot(lst2)
plt.ylabel('coef')
plt.show()
