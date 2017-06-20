import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/inflammation1.csv', delimiter=',')

print(data)

image1 = plt.plot(data)
plt.show(image1)
