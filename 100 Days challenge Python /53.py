#MAP
# def cube(x):
#     return x * x * x
# print(cube(2))
# l=[1, 2, 4, 6, 4, 3]
# newl=[]
# for item in l:
#     newl.append(cube(item))
# new = list(map(cube, l))
# new = list(map(lambda x: x*x*x,l))
# print(new)

#FILTER
# def filter_function(a):
#     return a>2
# l=[1,2,4,6,4,3]
# newl=[]
# newl=list(filter(filter_function, l))
# print(newl)

#REDUCE
from _functools import reduce
num = [1,2,3,4,5]
def myfun(x, y):
    return x+y
sum = reduce(myfun, num)
print(sum)

