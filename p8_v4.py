import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

# Create Random Data
x = 2 * np.random.rand(100,1)

y = 4 + 3 * x + np.random.randn(100,1)

# Create Model
model = LinearRegression()

# Train Model
model.fit(x,y)

# Prediction
x_new = np.array([[0],[2]])

y_pred = model.predict(x_new)

# Graph
plt.scatter(x,y)

plt.plot(x_new,y_pred)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Linear Regression")

plt.show()