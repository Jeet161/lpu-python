import numpy as np
data = np.array([[3, 7, 5], [7, 9, 11], [13, 19, 15]])
print(data)
print(np.median(data))
print(np.median(data, axis=1)) #row wise median
print(np.median(data, axis=0)) #column wise median

#median with even number
a =np.array([[30, 65 ,70,34],
             [80, 90, 60, 34],
             [50, 90, 60, 34]])
print(a)
print(np.median(a))
print(np.median(a, axis=0)) #row wise median
print(np.median(a, axis=1)) #column wise median


