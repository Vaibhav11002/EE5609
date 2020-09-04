#! /usr/bin/python3
import numpy as np

y = np.array([[3,2], [1,4]])

# let a = 2x + y
a = np.array([[1, 0] , [-3, 2]])

# x = (1/2)*(a-y)
x = (1/2) * (np.subtract(a,y))

print("The matrix x is : ", x)

