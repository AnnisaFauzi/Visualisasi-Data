import matplotlib.pyplot as plt
import numpy as np
index = np.arange(5)
valuse = [5,7,3,4,6]
std = [0.8,1.0,0.4,0.9,1.3]
plt.title('Diagram Batang')
plt.bar(index,values,yerr=std,error_kw=['ecolor':'0.1','capsize':6],alpha=0.7,la)
plt.xticks(index+0.4,['A','B','C','D','E'])
plt.legend(loc=2)
plt.show()
