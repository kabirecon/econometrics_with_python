import numpy as np
import pandas as pd
from linearmodels import PanelOLS
from linearmodels import RandomEffects
# =============================================================================
# from matplotlib import pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# from math import sqrt
# import seaborn as sns
# =============================================================================
# Regression construction
#lm = LinearRegression()

# Getting data and naming var
#data = r"G:\Unstructured Data\chnk file\updated_test.csv"
#df = pd.read_csv(data, encoding='utf8', engine='python')
#data = "G:\chnk file\dta.csv"
df = pd.read_csv('dta.csv', encoding = "ISO-8859-1", engine='python')
#encoding = "ISO-8859-1", engine='python'
#df.encode('utf-8').strip()

# =============================================================================
# #Data Type
# print(df.dtypes)
# 
# #Summary Stat
# print(df.describe())
# =============================================================================
print(df.head(100))
