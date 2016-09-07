import pandas as pd
import numpy as np
import matplotlib.pyplot as pp

iFile = "series.csv"


def get_series_from_file(file_name):
    return pd.read_csv(file_name, names=['1', 'src'])['src']


def less_squares(series):
    return np.polyfit(series.index, series, 1)

ser = get_series_from_file(iFile)
coef = less_squares(ser)
print(coef)
data = pd.DataFrame(ser)
data['appr'] = data.index*coef[0] + coef[1]
data.plot()
pp.show()