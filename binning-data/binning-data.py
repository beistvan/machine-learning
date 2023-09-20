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
