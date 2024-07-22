#線性回歸
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
xarray = np.array(x)
yarray = np.array(y)
# #線性回歸，用不到的參數可以用_代替，ex:slope, intercept, _, _, _ = stats.linregress(x, y)
slope, intercept, r, p, std_err = stats.linregress(xarray, yarray)
"""
slope:回歸線的斜率。
intercept:回歸線的截距。
r:相關係數。
p:p 值，表示統計顯著性。
std_err:斜率的標準誤差。
"""
def myfunc(x):
  return slope * x + intercept
#對 x 中的每一個值應用 myfunc 函數
mymodel = list(map(myfunc, xarray))

plt.scatter(xarray, yarray)
plt.plot(xarray, mymodel)
plt.show()
print(r)

#用線性回歸預測x = 10
#需先看r判斷相關性
speed = myfunc(10)

print(speed)