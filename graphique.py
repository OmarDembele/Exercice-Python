import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 10)
print(x)
v=np.linspace(0,2,10)
print(v)
y=v**2
plt.scatter(v, y)
plt.plot(v, y)
plt.grid()
plt.show()