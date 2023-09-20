import pandas as pd
import numpy as np

coffee = pd.read_csv('../data/starbucks_customers.csv')

## get spent feature
spent = coffee['spent']

#find the max spent
max_spent = np.max(spent)

#find the min spent
min_spent = np.min(spent)

#find the difference
spent_range = max_spent - min_spent
print(spent_range)

#normalize your spent feature
spent_normalized = (spent - min_spent) / spent_range

#print your results
print(spent_normalized)

"""
28
0      0.464286
1      0.892857
2      0.357143
3      0.250000
4      0.357143
         ...
117    0.178571
118    0.571429
119    0.071429
120    0.678571
121    0.107143
Name: spent, Length: 122, dtype: float64
"""
