import numpy
arr1=numpy.array([
    [1,2,3],
    [4,5,6],
])#(2,3)
arr2=numpy.array([
    [7,8,9],
    [10,11,12],
])#(2,3)
arr3=numpy.array([
    [13,14],
    [15,16],
])#(2,2)
#合併
#第一維度
# result1=numpy.vstack((arr1,arr2))#(4,3)
# print(result1)
# #第二維度
# result2=numpy.hstack((arr1,arr2))#(2,6)
# print(result2)
#多維度
result3=numpy.concatenate((arr1,arr2,arr3),axis=1)#(2,8)
print(result3)
"""
錯誤範例
result4=numpy.concatenate((arr1,arr2,arr3),axis=0)#(4,2)
print(result4)
"""