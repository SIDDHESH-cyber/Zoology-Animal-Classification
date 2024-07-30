import random

print("Number Gussing Game")

number = random.randint(1,10)
print(number)
count = 1

# num = random.randrange(1,11)
# num = random.randint(1,10)
# print(num)

user = int(input("Enter Number From 1 - 100 : "))

while(user!=number):
    if user > number:
        user = int(input("Enter Number A Lower Number : "))
    else:
        user = int(input("Enter Number A Higher Number : "))

    count += 1

if count <= 3:
    print("You Completed The Game With The Best Score In : ", count ,"Times")
elif count <= 5:
    print("You Completed The Game With The Good Score In : ", count ,"Times")
else:
    print("You Completed The Game With The Okayish Score In : ", count ,"Times")
