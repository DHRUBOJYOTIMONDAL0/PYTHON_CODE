# mark = [12, 24, 30, 99, 12, 24, 30, 99, 12, 24, 30]
# #index = 0
# #for mark in mark:
# for index, mark in enumerate(mark):
#     print(mark)
#     if(index==3):
#         print("Dhrubo, Awesome")
#     #index +=1

fruits = ['Apple','Banana','Orange']
#for index, fruit in enumerate(fruits):
for index, fruit in enumerate(fruits, start=1):
    print(index,fruit)