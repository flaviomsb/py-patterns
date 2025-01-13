import pandas as pd
import numpy as np
import statsmodels.api as sm
import os
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
current_dir = os.path.dirname(__file__)
df = pd.read_excel(os.path.join(current_dir, '../../support_files/cars.xls'))

df1 = df[['Mileage', 'Price']]
bins = np.arange(0, 50000, 10000) # break 50k rows into 10k chunks starting from 0
groups = df1.groupby(pd.cut(df1['Mileage'], bins), observed=True).mean()
print(groups.head())

x_fields = ['Mileage', 'Cylinder', 'Doors']

X = df[x_fields]
y = df['Price']

X[x_fields] = scale.fit_transform(X[x_fields])

X = sm.add_constant(X)

print(X)

est = sm.OLS(y, X).fit()

print(est.summary())
