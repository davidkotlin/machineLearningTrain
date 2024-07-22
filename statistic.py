import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#平均
# x = numpy.mean(speed)

# #中位数
# x = numpy.median(speed)

# #眾數
# x = stats.mode(speed)

# #標準差
# x = numpy.std(speed)

#變異數
x = numpy.var(speed)
print(x)