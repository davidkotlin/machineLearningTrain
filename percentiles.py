import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
#在age裡面找出前75%的數字(43與比43年輕)
x = numpy.percentile(ages, 75)
y=numpy.percentile(ages, 90)
print(x,y)