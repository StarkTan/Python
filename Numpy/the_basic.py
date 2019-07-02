import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
b = np.array([6, 7, 8])
print(b)
print(type(b))
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print(np.zeros((3, 4)))
print(np.ones((2, 3, 4), dtype=np.int16))

