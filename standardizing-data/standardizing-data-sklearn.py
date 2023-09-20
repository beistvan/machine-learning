import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

coffee = pd.read_csv('../data/starbucks_customers.csv')
ages = coffee['age']

## data analysis usin sklearn

scaler = StandardScaler()

ages_reshaped = np.array(ages).reshape(-1,1)

ages_scaled = scaler.fit_transform(ages_reshaped)

print(np.mean(ages_scaled)) # 1.7290358580227847e-16
print(np.std(ages_scaled))  # 0.9999999999999999
