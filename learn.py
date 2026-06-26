import random

a = random.randint(1, 5)
b = random.randint(1, 5)
c = random.randint(1, 5)

print(a,b,c)

if a == 1 and b == 1 and c == 1:
    print("You won!")
if a == 2 and b == 2 and c == 2:
    print("You won!")
if a == 3 and b == 3 and c == 3:
    print("You won!")
if a == 4 and b == 4 and c == 4:
    print("You won!")
if a == 5 and b == 5 and c == 5:
    print("You won!")

else:
    print("You lost!")