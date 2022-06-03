#numpy array creation 
import numpy as np
#create numpy array
arr = np.array([[1,2,32,4,5]],np.int8)
print(arr)
#shape o0f array
print(arr.shape)
print(arr.dtype)
zeros = np.zeros((2, 5))
print(zeros)
rng = np.arange(15)
print(rng)
lspace = np.linspace(1,4,4)
print(lspace)
emp = np.empty((4,6))
print(emp)
emp_like = np.empty_like(lspace)
print(emp_like)
ide = np.identity(3)
print(ide)
