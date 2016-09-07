import numpy as np
import pandas as pd


def generate_random_truth_data(order=3, sigma=1):
    res = []
    r = np.arange(0, 3, 3/order).tolist()
    p = np.random.normal(0, sigma, [order, 1]).flatten().tolist()
    for i in range(order):
        res += [p[i] + r[i]]
    return res

ser = pd.Series(generate_random_truth_data(100))
ser.to_csv('series.csv')
