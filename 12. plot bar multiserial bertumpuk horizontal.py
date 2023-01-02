import matplotlib.pyplot as plt
import numpy as np
index = np.arange(5)
series1 = np.array([3,4,5,3])
series2 = np.array([1,2,2,5])
series3 = np.array([2,3,3,4])
index = np.arange(4)
plt.axis([-0,15,-0.5,3.5])
plt.title('Diagram Batang Bertumpuk Multiserial')
plt.bar(index,series1,color='r')
plt.bar(index,series2,color='b',left=series1)
plt.bar(index,series3,color='g',left=(series2+series1))
plt.yticks(index+0.4,['Sep21','okt21','Nov21','Des21'])
plt.show()
