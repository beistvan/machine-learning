import pandas as pd
import numpy as np

coffee = pd.read_csv('../data/starbucks_customers.csv')
ages = coffee['age']

## set up variables
mean_age = np.mean(ages)
std_dev_age = np.std(ages)

## standardize ages
ages_standardized = (ages - mean_age) / std_dev_age

## print the results
print(np.mean(ages_standardized)) # 1.7290358580227847e-16
print(np.std(ages_standardized)) # 0.9999999999999999
