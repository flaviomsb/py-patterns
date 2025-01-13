import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale 

current_dir = os.path.dirname(__file__)
df = pd.read_excel(os.path.join(current_dir, '../../support_files/cars.xls'))

raw_data = df[['Price', 'Mileage']]
data = scale(raw_data)

model = KMeans()

model = model.fit(data)

plt.figure(figsize=(8, 6))
plt.scatter(x=raw_data['Price'], y=raw_data['Mileage'], c=model.labels_.astype(int) if model.labels_ is not None else None)
plt.xlabel('Price')
plt.ylabel('Mileage')
plt.show()
