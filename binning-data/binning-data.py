import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

coffee = pd.read_csv('../data/starbucks_customers.csv')
ages = coffee['age']

print(np.min(ages))
print(np.max(ages))

age_bins = [12, 20, 30, 40, 71]

coffee['binned_ages'] = pd.cut(coffee['age'], age_bins, right = False)

print(coffee['binned_ages'].head(10))

coffee['binned_ages'].value_counts().plot(kind='bar')

plt.show()

# to run type in command line:
# python binning-data.py

"""
13
70
0    [40, 71)
1    [30, 40)
2    [20, 30)
3    [20, 30)
4    [20, 30)
5    [20, 30)
6    [20, 30)
7    [20, 30)
8    [20, 30)
9    [20, 30)
Name: binned_ages, dtype: category
Categories (4, interval[int64, left]): [[12, 20) < [20, 30) < [30, 40) < [40, 71)]
"""
