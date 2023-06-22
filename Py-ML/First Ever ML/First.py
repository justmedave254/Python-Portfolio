import csv
from pandas import read_csv
from pandas import set_option
from matplotlib import pyplot
from threading import Thread

path1 = r"C:\Users\User\OneDrive\Documents\Code\Py ML\IRIS.csv"
path2 = r"C:\Users\User\OneDrive\Documents\Code\Py ML\diabetes.csv"

print("Prints data from the csv file and its shape")
data = read_csv(path1)
print(data.shape)
print(data[:3])

print("-----------------------------")
data2 = read_csv(path2)
print(data2.shape)
print(data2[:3])

print("-----------------------------")
print(data2.dtypes)

print("-----------------------------")
set_option('display.width', 100)
set_option('display.precision', 2)  #up to 2dp
print(data2.shape)
print(data2.describe())


print("-----------------------------")
print("Prints the correlations between the pairs in the matrix")
correlations = data2.corr(method='pearson')
print(correlations)

print("-----------------------------")
print("Using skew function to determine skew")
print(data2.skew())

print("-----------------------------")
print("Using hist function to generate a histogram")
data2.hist()
pyplot.show()

print("-----------------------------")
print("Generating a Density Plot")
data2.plot(kind='density', subplots=True,  layout=(3,3), sharex=False)
pyplot.show()
