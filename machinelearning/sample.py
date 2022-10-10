import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

#Regression
x,y = make_regression(n_samples=200,n_features=1,noise=30)
plt.scatter(x,y)