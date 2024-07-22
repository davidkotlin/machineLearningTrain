import numpy
# ndarr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# len=len(ndarr)
# print(len)
ndarr1=numpy.array([1, 2, 3])
ndarr2=numpy.array([
    [1, 2, 3],
    [4, 5, 6]
    ])
ndarr3=numpy.array([
    [
        [1, 2, 3],[4, 5, 6]
    ],
    [
        [4, 5, 6],[7, 8, 9]
    ]
])
data=numpy.zeros(9)
data=numpy.ones(9)
data=numpy.arange(9)
data=numpy.empty([3,3])
print(data)