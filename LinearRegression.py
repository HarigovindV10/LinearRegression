import numpy as np
import pandas as pd
import math
from scipy.stats.stats import pearsonr


class LinearRegression:
	slope = 1
	intercept = 0
	actual_output = []
	error_threshold = 0

	def __init__(self, slope = 1, intercept = 0):
		self.slope = slope
		self.intercept = intercept

	def __repr__(self):
		return f'Slope : {self.slope}\nIntercept : {self.intercept}'

	def compute_error(self, predicted_output):
		error: float = 0

		for actual, predicted in zip(self.actual_output, predicted_output):
			error += (actual - predicted) ** 2

		return math.sqrt(error)

	def compute_intercept(self, x, y):
		x_mean = np.mean(x)
		y_mean = np.mean(y)

		self.intercept = y_mean - self.slope * x_mean

		return self.intercept

	def compute_slope(self, x, y):
		x_std = np.std(x)
		y_std = np.std(y)

		if math.isnan(x_std) or math.isnan(y_std):
			raise ValueError("Standard deviation cannot be NaN")

		correlation = pearsonr(x, y)

		self.slope = correlation[0] * y_std / x_std

		return self.slope

	def gradient_descent(self):
		pass

	def train(self, x, y):
		predicted_output = []

		while True:
			for x_value, y_value in zip(x, y):
				predicted_value = self.slope * x_value + self.intercept
				predicted_output.append(predicted_value)
				self.actual_output.append(y_value)

			error = self.compute_error(self, predicted_output)

			if error <= self.error_threshold:
				break


train_data = pd.read_csv('train.csv')

# print(train_data)

x_train = np.array(train_data['x'])
y_train = np.array(train_data['y'])

# print(x_train)
# print(y_train)

linearRegression = LinearRegression()

slope = linearRegression.compute_slope(x_train, y_train)
intercept = linearRegression.compute_intercept(x_train, y_train)

# print(slope, intercept)

test_data = pd.read_csv('test.csv')

x_test = np.array(test_data['x'])
y_test = np.array(test_data['y'])

predicted_output = []

for x_value in x_test:
	predicted_output.append(slope * x_value + intercept)

for actual, prediction in zip(y_train, predicted_output):
	print(f'Actual : {actual} Predicted : {prediction} Error : {actual - prediction}')




