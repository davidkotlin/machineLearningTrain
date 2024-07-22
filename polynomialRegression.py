#多項式回歸
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
#x,y根據三次多項式模擬
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
#相關係數，比較y與模擬x後的y
print(r2_score(y, mymodel(x)))
print(mymodel,type(mymodel))
myline = numpy.linspace(1, 22, 100)
print(myline)
#預測
speed = mymodel(17)
print(speed)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
# plt.plot(x, mymodel(x))
plt.show()