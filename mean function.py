import numpy as np
a =np.array([[30, 65 ,70,34],
             [80, 90, 60, 34],
             [50, 90, 60, 34]])
print(a)
print(np.mean(a))
print(np.mean(a, axis=0)) #row wise mean
print(np.mean(a, axis=1)) #column wise mean