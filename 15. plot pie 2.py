import matplotlib.pyplot as plt
labels = ['Lain-lain','samsung','apple','huawei','oppo','vivo']
values = [42,21,14,9,8,7]
colors = ['red','green','pink','blue','yellow','orange']
explode = [0,0,0,1,0,0] #fokus pada samsung
plt.title('Diagram pie Market Share Samsung')
plt.pie(values,labels=labels,colors=colors,expolode,shadow=True,autopot=')
plt.axis('equal')
plt.show()
