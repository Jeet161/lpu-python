import numpy as np
a =np.array([10, 20, 30, 40])
b =np.array([1, 2, 3, 4])
weighted_avg =np.average(a, weights=b)
print("Weighted average of a with weights b:", weighted_avg)

