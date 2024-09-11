# appleprice = 210
# budget = 200
# appleprice = int(input("enter apple price: "))
# budget = int(input("enter budgetL: "))
# if(appleprice <= budget):
#     print("Alex, addd 1kg apple to  the cart.")
# else:
#     print("Alexa, do not add apple to the cart")


# elif


# num = int(input("Enter your number: "))
# if(num < 0 ):
#     print("Number is Negative")
# elif(num == 0):
#     print("Number is Zero")
# elif(num == 999):
#     print("Number is Special")
# else:
#     print("Number is Posative")
# print("I'm Happy Now!")


# Nasted if statements



num = int(input("Enter Your Number: "))
if (num < 0):
    print("Number is Negative")
elif(num > 0):
    if(num <= 10):
        print("Number is Between 1-10")
    elif(num > 10 and num <=20):
        print("Number is Between 11-20")
    else:
        print("Number is Grater then 20")
else:
    print("Number is Zero")