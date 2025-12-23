#  Using map(), reduce(), and filter() functions for processing data.

#map function
# number=[1,2,3,4,5,]
# square=list(map(lambda x: x*x,number))
# print(square)

#filtter function
# number=[1,2,3,4,5,6]
# evens=list(filter(lambda x: x % 2==0,number))
# print(evens)

#reduce function
from functools import reduce
number=[1,2,3,4,5,6]
totale=reduce(lambda a,b: a+b,number)
print(totale)

