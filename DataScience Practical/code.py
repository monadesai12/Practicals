from scipy.stats import randint
import numpy as np
import matplotlib.pyplot as plt

low ,high = 7,31
mean, var, skew, kurt = randint.stats(low ,high,moments='mvsk')

x = np.arange(randint.ppf(0.01,low,high),
           randint.ppf(0.99,low,high))
ax.plot(x,randint.pmf(x,low,high),'bo' ,ms=8, lable='randint pmf')
ax.values(x, 0, randint.pmf(x ,low ,high),colors='b', lw=5 ,alpha=0.5)

rv=randint(low, high)
ax.values(x, 0, rv.pmf(x), colors='K' , linestyles='-' ,lw=1, lable='frozen pmf')
ax.legent(loc='best', frameon=False)
plt.show()
   
prob=randint.cdf(x, low ,high)
np.allclose(x, randint.ppf(prob ,low, high))
   
r=randint.rvs(low ,high, size=1000)
