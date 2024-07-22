#多維陣列形狀
import numpy
#印出資料形狀
# data=numpy.ones(10)
# print("資料:",data,"形狀:",data.shape)
# data2=numpy.array([[3,1,5],[1,2,3]])
# print("資料:",data2,"形狀:",data2.shape)
#轉置形狀
# data=numpy.array([[2,1,4],[1,5,0]])
# print("資料轉置:",data.T,"形狀轉置:",data.T.shape)
#扁平化
data=numpy.array([
    [
        [2,1,3],[1,2,3]
    ],
    [
        [0,2,1],[8,9,10]
    ]
])
# newData=data.flatten()#修改 flattened 不會影響 data，(慢)
# newData2=data.ravel()#修改 raveled 會影響 data，(快)
# print("資料扁平化:",newData,"形狀扁平化:",newData.shape)
# print("資料扁平化:",newData2,"形狀扁平化:",newData2.shape)
# #重塑資料形狀(需要與原始資料數量相同)
# #data 2x2x3=12
newData=data.reshape(3,4)
print("資料重塑:\n",newData,"\n","形狀重塑:\n",newData.shape)
#初始化
data=numpy.zeros(18).reshape(3,6)
print(data)
data2=numpy.arange(9).reshape(3,3)
print(data2)