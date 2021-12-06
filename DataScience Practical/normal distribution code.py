from scipy.stats import norm
data_normal =norm.rvs(size=10000,loc=0, scale=1)

import seaborn as sns
ax = sns.distplot(data_normal,
                    bins=100,
                kde=True,
                color="skyblue",
                hist_kws={"linewidth": 15, 'alpha':1})
ax.set(xlabel='Normal Distribution', ylable='Frequency')