import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
baseball = pd.read_csv('baseball.csv')
lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()
input = baseball[['G','G_batting','AB','R', 'H', 'X2B', 'X3B', 'HR','RBI', 'SB', 'salary']].values
from sklearn import feature_selection
regr = linear_model.LinearRegression()
salary = [[x] for x in baseball['salary']]
G = [[x] for x in baseball['G']]
regr.fit(G,salary)
plt.scatter(G, salary, c='b', marker='o')
plt.plot(salary, regr.predict(salary), color='green')
plt.show()
G = [[x] for x in baseball['G_batting']]
regr.fit(G_battting,salary)
plt.scatter(G_batting, salary, c='r', marker='o')
plt.plot(salary, regr.predict(salary), color='green')
plt.show()
baseball_input = baseball._get_numeric_data()
baseball_input = baseball_input.dropna(axis=0)