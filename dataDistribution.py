import numpy
import matplotlib.pyplot as plt
#亂數產生250個介於0到5之間的數字uniform分布
x = numpy.random.uniform(0, 5, 250)

# print(x)
#產生直方圖
plt.hist(x, 5)
plt.show()
x = numpy.random.uniform(0.0, 5.0, 100000)

# plt.hist(x, 100)
# plt.show()
#常態分布numpy.random.normal(平均, 標準差, 數據數量)
x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()