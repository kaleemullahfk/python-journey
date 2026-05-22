# Day 3 — Loops (for & while)

# for loop
for i in range(6):
    print("Kaleemullah")


for num in range(1,10):
    print(num)


# — Multiplication Table
number = int(input("Enter a number : "))

for t in range(1,11):
    print(number," x ",t," = ",t*number)


# while Loop
count = 1
while count < 10:
    print(count)
    count += 1


# — User Password System
password = ""
while password != "kaleem123":
    password = input("Enter your password :")
print("Access Granted")

# — Countdown Timer

count = 10
while count > 0:
    print(count)
    count -= 1
print("Time's up!")    


# Practice Program 1 — Even Numbers
num = 0
while num <=20:
    print(num)
    num += 2


# with input Practice Program 1
a = int(input("Enter a number:"))
num = 0
while num <=a:
    print(num)
    num += 2
print("Done")


# Practice Program 2 — Odd Numbers
a = int(input("Enter a number:"))
num = 1
while num <= a:
    print(num)
    num += 2

# Practice Program 3 — Sum of Numbers
count = 1
total = 0

while count <= 100:
    # print(count)
    count += 1
    total = total + count #or total += count
print("Your total =", total)


# Practice Program 4 — Guessing Game
secret = 5
guess = 0

while guess != secret:
    guess =int(input("Enter Guess number:"))    
print("Correct guess")


# Challenge 2
# Take numbers from user and calculate total UNTIL user enters 0.
n = 1
total = 0
while n != 0:
    n = int(input("Enter a number:"))
    print(" ADD another, for result enter 0")
    total += n
print("Your total sum is",total)



# Challenge 3
# Create login system:
# ask username/password repeatedly
# stop when correct
username = ""
password = ""
while username != "qamar":
    username = input("Enter username: ")
while password != "qe":
    password = input("Enter password: ")
print("Login Successfully")


##Move to for loop
# Challange - 1 Take a number from user and print its table.
num = int(input("enter number:"))

for i in range (1,11):
    print(num," x ",i," = ",num * i)


# Challenge 2 — Sum of Even Numbers
sum = 0
for i in range (2,101,2):
    sum+=i
print(sum)


# Challenge 3 — Star Pattern
for s in range (1,6):
    print("*" * s)