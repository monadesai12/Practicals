

from scipy.stats import poisson
data_poisson=poisson.rvs(mu=3 , size=10000)


import seaborn as sns
ax = sns.distplot(data_poisson,
                    bins=30,
                kde=False,
                color="skyblue",
                hist_kws={"linewidth": 15, 'alpha':1})
ax.set(xlabel='Poisson Distribution', ylable='Frequency')
