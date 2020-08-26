import matplotlib.pyplot as plt
import numpy as np

fig= plt.figure(figsize=(6,3))

axes= fig.add_axes([0.1,0.1,0.8,0.8])  # this just places a graph has nothing to do with the values on the x and y axis

x= [1,2,3,4,5]   # arrays you wish to plot soon
y=[1,2,3,4,5,]

a = np.array([6, 3, 5, 2, 4, 1])
plt.plot([1, 4, 2, 5, 3, 6])
plt.plot(a)


axes.plot(x,y)

plt.show()


import sympy # this is more for jupyter lab
sympy.init_printing(use_latex='mathjax')

phi, x = sympy.symbols('\phi, x')
print(phi)
