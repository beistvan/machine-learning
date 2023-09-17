# to run: python centered-data.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn 

coffee = pd.read_csv('starbucks_customers.csv')

ages = coffee['age']

min_age = np.min(ages)
print(min_age)

max_age = np.max(ages)
print(max_age)

print(max_age - min_age)

mean_age = np.mean(ages)
print(mean_age)

centered_ages = ages - mean_age
print(centered_ages)

plt.hist(centered_ages)
plt.show()

#output:

"""
13
70
57
27.33606557377049
0      24.663934
1       7.663934
2       1.663934
3       0.663934
4       0.663934
         ...
117    -5.336066
118    -5.336066
119    -7.336066
120    -7.336066
121   -13.336066
Name: age, Length: 122, dtype: float64
"""