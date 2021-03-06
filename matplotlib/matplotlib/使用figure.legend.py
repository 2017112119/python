import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10)
y = np.linspace(0,10)
z = np.sin(x/3)**2*98

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y,'-',label='Quantity 1')

ax2 = ax.twinx()
ax2.plot(x,z,'-r',label='Quantity 2')
fig.legend(loc=1,bbox_to_anchor=(1,1), bbox_transform=ax.transAxes)

ax.set_xlabel("x [units]")
ax.set_ylabel(r"Quantity 1")
ax2.set_ylabel(r"Quantity 2")
plt.show()
plt.savefig('2.png')
