import numpy as np
a = np.array([[1, 2, 3],[2,3,4],[4, 5, 6]])
print(a)
print(a.shape)

b = np.array([[1, 2, 3],[2,3,4]])
print(b)
print(b.shape)
bshape = (3,2)
print(bshape)


c = np.array([[1, 2, 3],[2,3,4],[4, 5, 6]])
print(c)
d = np.resize(c, (5, 5))
print(d)

x=np.array([[1, 2, 3],[2,3,4],[4, 5, 6]])
print(np.resize(x, (2, 3)))

