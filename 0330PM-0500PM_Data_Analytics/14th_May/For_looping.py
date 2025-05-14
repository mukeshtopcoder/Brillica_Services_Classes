"""
Control Statements:-
if , if_else , Nested if_else , elif , Complex Cond.
Looping:- for , while

Looping:-
Loop is used to perform a task again and again.

FOR_LOOP
Syntax:-
for variable_name in range(start,stop,step):
    statements

for a in range(1,5,1):
    print("Hello")

num = int(input("Enter A Number : "))
for a in range(1,11,1):
    print(a*num)

for a in range(5,10,2):
    print(a)


# by default value step = 1.
for a in range(5,10):
    print(a)

    
# by default value step = 1.
# by default value start = 0.
for a in range(5):
    print(a)


# break , continue , pass

for a in range(1,5):
    if a == 3:
        break   # Exit from the current loop
    print(a)

for a in range(1,5):
    if a == 3:
        continue   # Skip the code
    print(a)

for a in range(1,5):
    if a == 3:
        pass    # do nothing
    print(a)


for a in range(1,5):
    print(a)
    if a==3:
        break
else:
    print(0)


# WAP to print counting from 1 to 10.
num = 10
for a in range(1,num+1):
    print(a)
# WAP to print table of a number.
num = 19
for a in range(1,11):
    print(a*num)


# WAP to find all the factors of number.
# HINT :-   12  ->  1,2,3,4,6,12

num = 12
for a in range(1,num+1):
    if num%a == 0:
        print(a)


# WAP to count factors of a number.
# Hint:-   12 -> 1,2,3,4,6,12 -> 6 Factors


num = 12
count = 0
for a in range(1,num+1):
    if num%a==0:
        count=count+1

print(count)


# WAP to check an entered number is prime or not.

num = 17
count = 0
for a in range(1,num+1):
    if num%a==0:
        count=count+1

if count == 2:
    print("Prime")
else:
    print("Not Prime")


# Nested _ Loop
# WAP to print Table from 1 to 10.

for num in range(1,11):
    for a in range(1,11):
        print(a*num,end=" ")
    print()
"""











