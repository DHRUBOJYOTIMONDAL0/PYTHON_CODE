#marks = [3,4,6,"Dhrubo", True]
#print(type(marks))
#print(marks)
#print(marks[4])
# List are changeable meaning we can alter after creating
# As we can see a single list can contain items of different data types
#print(marks[-3]) # Negative marks
#print(marks[len(marks)-3]) # Positive marks
# Check weather an item in present in the list
#if 7 in marks:
 #   print("Yes")
#else:
 #   print("No")

# Same things applies for strings as well
#if "Dh" in "Dhrubo":
 #   print("Yes")

#print("marks")
#print(marks[1:-1])
#print(marks[1:4:2]) # jump index

# List Comprehensions

#list = [i for i in range(4)]
#list = [i for i in range(10) if i%2==0]
#print(list)

# *********List Methods*****
list = [2,99,3,11,4,5,2,2,60,6]
print(list)
#list.append(7)
#list.sort(reverse=True)
#list.reverse()
#print(list.index(2))
#print(list)
#print(list.count(2))

#m = list.copy()
#m[0] = 0
#list.insert(3,888)
m = [800,900,1000]
list.extend(m)
print(list)


