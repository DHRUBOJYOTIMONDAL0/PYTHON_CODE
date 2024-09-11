import time
a1 = time.strftime("%H:%M:%S")
print("a1")
a2 = time.strftime("%H")
print("Hour is:", a2)
a3 = time.strftime("%M")
print("Minute is:", a3)
a4 = time.strftime("%S")
print("Second is:", a4)
 # MORNING TO NIGHT SECTION
name = input("Enter your name Sir:")
h=int(time.strftime("%H"))
if(6>=h<12):
    print("Good Morning Sir")
elif(12>=h<5):
    print("Good Afternoon Sir")
elif(5>=h<7):
    print("Good Evening sir")
else:
    print("Good Night sir")