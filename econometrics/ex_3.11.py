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
data = "F:\econometrics\Assign2\data_ex3.1.csv"
df = pd.read_csv(data)

# Data Type
print(df.dtypes)

# Summary Stat
print(df.describe())

# Variables
x = df[['ct-1']]
y = df['ct']
bias_beta1 = []
bias_beta2 = []
while True:
    sample = input("Enter Sample Size + 1 Number: ")
    if sample == "done":
        break
    try:
        ival = int(sample)
    except:
        print("Please, enter valid input")
        continue
    rept = input("Repeate: ")
    if rept == "done":
        break
    try:
        ival2 = int(rept)
    except:
        print("Please, enter valid input")
        continue

    count = 0
    count_2 = 0
    # Value Storage
    intercept = 0
    coefficient = 0
    #standard_error = []
    beta_1 = 1
    beta_2 = 0.8
    # Regression Loop
    for i in range(ival2):

        for i in range(3, ival):
            a = x[:i]
            b = y[:i]
            # print(a)
            lm.fit(a, b)
            yhat = lm.predict(a)
            count = len(a)
            print("Number of Observations =", count)
            # print(yhat)
            #rmse = sqrt(mean_squared_error(a, yhat))
            inter = lm.intercept_
            cof = lm.coef_
            print("Intercept = ", inter)
            print("Coefficient =", cof)
            #print("Standard Error =", rmse)
            print("_"*50)

            intercept = intercept + inter
            coefficient = coefficient + cof
            # standard_error.append(rmse)

        count_2 = count_2 + 1

    grand_count = count*count_2

# =============================================================================
# print(count)
# print(count_2)
# print(grand_count)
# =============================================================================
# Average
    average_intercept = (intercept/grand_count)
    average_coefficient = (coefficient/grand_count)

# =============================================================================
# print(average_intercept)
# print(average_coefficient)
# =============================================================================

# Bias of Beta1 and Beta2

    bias_beta1_hat = beta_1 - average_intercept
    bias_beta2_hat = beta_2 - average_coefficient

    bias_beta1.append(bias_beta1_hat)
    bias_beta2.append(bias_beta2_hat)

print("Bias of Beta1 =", bias_beta1)
print("Bias of Beta2 =", bias_beta2)
# First Figure
plt.plot(bias_beta1)
plt.ylabel('bias of beta1')
plt.show()
# Second Figure
plt.plot(bias_beta2)
plt.ylabel('boas of beta2')
plt.show()
exit()
