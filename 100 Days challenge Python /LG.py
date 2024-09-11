# x = 4
# print(x)
#
# def hello():
#     x = 5
#     print("Hello Dhrubo")
#     print(f"THe local variable is {x}")
#
#
# print(f"THe global variable is {x}")
# hello()
# print(f"THe global variable is {x}")


x = 10 # global variable

def my_function():
    global x  # Change the global variable
    x = 4
    y = 5 # local variable

    print(y)

my_function()
print(x)
#print(y)   # this will cause an error because y is a local variable and
# is not accessible outside of the function
