
import matplotlib.pyplot as plt
import numpy as np

a = np.random.random((24, 32))
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()