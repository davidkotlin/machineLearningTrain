import numpy as np
#逐元運算(element wise operation)
# data1=np.array([3,2,10])
# data2=np.array([1,3,6])
# result=data1+data2
# print("加法:",result)
# #中間運算符號可以自行替換加減乘除，兩陣列需同樣維度
# result=data1>data2
# print("比較:",result)
#中間運算符號可以自行替換大於小於，兩陣列需同樣維度
# #矩陣運算(matrix operation)
# data1=np.array([[1,3]])#1x2
# data2=np.array([[2,-1,3],[-2,4,1]])#2x3
# #內積
# result=data1@data2#1x3
# print("矩陣乘法內積:",result)
# #外積
# result=np.outer(data1,data2)#2x6
# print("矩陣乘法外機:",result)
# #統計運算(statistic operation)
data1=np.array([
    [2,1,7],
    [-5,3,8]
])
"""
#總和
result=np.sum(data1)
print("總和:",result)
#最大值
result=np.max(data1)
print("最大值:",result)
#最小值
result=np.min(data1)
print("最小值:",result)
#平均
result=np.mean(data1)
print("平均:",result)
#中位數
result=np.median(data1)
print("中位數:",result)
#標準差
result=np.std(data1)
print("標準差:",result)
"""
print(data1)
#針對維度(axis不能超過維度上限)
#result=data1.sum(axis=0)
result=np.sum(data1,axis=0)#針對欄(第一個維度，直向)
print("針對維度直向加總:",result)
result=np.sum(data1,axis=1)#針對行（第二個維度，橫向）
print("針對維度橫向加總:",result)
#以此類推
result=np.max(data1,axis=0)
print("以此類推直向最大:",result)
result=np.mean(data1,axis=1)
print("以此類推橫向平均:",result)
result=np.mean(data1,axis=0)
print("以此類推直向平均:",result)
#矩陣轉置
result=np.transpose(data1)
print("矩陣轉置:",result)
#逐值累加
result=np.cumsum(data1)#由左至右一列一列累加
print("逐值累加:",result)
result=np.cumsum(data1,axis=1)#針對一列
print("逐值累加針對一列:",result)
result=np.cumsum(data1,axis=0)#針對一行
print("逐值累加針對一行:",result)