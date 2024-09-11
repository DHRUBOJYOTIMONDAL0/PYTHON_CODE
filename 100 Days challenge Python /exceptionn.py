# a = input("Enter your number: ")
# print(f"multification table of {a} is:")
# try:
#   for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a) * i}")
# except Exception as e:
#     print("Sorry some error occurred")
# print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [6, 4]
    print(a[num])
except ValueError:
    print("Number is not an integer")
except IndexError:
    print("Index error")