#-Arithmetic Operators

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)



# — Comparison Operators

age = 20
print(age == 20)
print(age != 20)
print(age >10)
print(age <  20)
print(age >= 23)
print(age <= 23)


# — Logical Operators
age = 20
a = True
print(age <23 and a)


#— Conditions (if, else, elif)

age = int(input("Enter your age:"))

if age >= 18:
    print("you can vote")
else:
        print("you can't vote")


#— elif Example
marks = int(input("Enter your marks:"))

if marks >= 90:
    print("grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


#Program 1 — Even or Odd
num = int(input("Enter your number:"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# Program 2 — Largest Number
a = int(input("First number:"))
b = int(input("Second number:"))

if a > b:
    print("First number is Larger")
else:
    print("Second number is Larger")



# Program 3 — Login System


password = input("Enter Password:")

if password == "QE":
    print("Acess granted")
else:
    print("Wrong password")


# Challenge 1 — Positive / Negative / Zero
num = int(input("Enter your number:"))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Challenge 2 — Largest Among 3 Numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a > b and a > c:
    print("First number is largest")
elif b > a and b > c:
    print("Second number is largest")
else:
    print("third number is largest")


# Challenge 3 — Simple ATM Check
balance = int(input("Enter your balance:"))

if balance >= 1000:
    print("Withdrawal Allowed")
else:
    print("Insufficient Balance")