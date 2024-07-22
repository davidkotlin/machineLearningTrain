import numpy
# data=numpy.array([
#     [1,5,2,10]
# ])
# print(data[0])
# print(data[0][2])
# #同list
# #多維
# data2=numpy.array([
#     [0,1],
#     [10,-5],
#     [2,6],
# ])
# print(data2[0])
# print(data2[1][1])
#切片
#一維
# data3=numpy.array([
#     [-1,-5,2,3],
# ])
# print(data3[0][0:3])
# print(data3[0][:2])
# print(data3[0][2:])
#多維
data4=numpy.array([
    [0,1,2],[3,4,5],
    [5,4,3],[2,1,0],
])
print(data4[1:3,0:2])
print(data4[0:2,1])
#全選
data5=numpy.array([
    [
        [8,1,3],[-5,5,2]
    ],
    [
        [0,1,6],[4,4,-3]
    ]
])
print(data5[0,...])
print(data5[...,1:3])