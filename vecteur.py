import numpy as np
import matplotlib.pyplot as plt
a = [10 , 20, 30, 40]
y=np . array (a)
print(y)
plt.bar(range(1, y.size+1), y)
plt.xlabel('NBRE')
plt.ylabel('BASES')
plt.show()