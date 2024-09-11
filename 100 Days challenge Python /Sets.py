# s = {2,4,2,6}
# print(s)
#
# dhrubo = set()
# print(type(dhrubo))

s1 = {2,4,2,6}
s2 = {2,4,3,8,9}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
