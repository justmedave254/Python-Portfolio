import csv
import pandas as pd
from pandas import read_csv

path1 = r"C:\Users\User\OneDrive\Documents\Code\Py ML\IRIS.csv"
path2 = r"C:\Users\User\OneDrive\Documents\Code\Py ML\diabetes.csv"

data = read_csv(path1)
print(data.shape)
print(data[:3])

print("-----------------------------")
data2 = read_csv(path2)
print(data2.shape)
print(data2[:3])
