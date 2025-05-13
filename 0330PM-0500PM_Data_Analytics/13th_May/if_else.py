# Conditional Statements.
# if , if_else , Nested if_else , elif, Complex Cond.
# Looping :- for , while

"""
if
Syntax:-
if condition:
    statements

# Example

if 10>50:
    print("Hello India")

if_else
Syntax:-
if condition :
    statements
else :
    statements
    

# Example
if 10>50:
    print("Hello India")
else:
    print("Hello World")



# WAP to check an entered number is even or odd.

num = int(input("Enter A Number : "))

if num%2 == 0:
    print("Even")
else:
    print("Odd")



# WAP to find greater value between two.

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
if b>a:
    print(b)
else:
    print(a)
    
"""

# Nested if_else
"""
syntax:-
if condition:
    if condition:
        true Statement
    else:
        false Statements
else:
    if condition:
        true statement
    else:
        true statement


# WAP to check an entered number is positive,
# negative or zero.

num = int(input("Enter A Number : "))
# 0
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")



# WAP to check an entered character is vowel or not.
# a , e , i , o , u
ch = input("Enter A Character : ") 
if ch=='a': 
    print('Vowel')
else:
    if ch=='e':
        print("Vowel")
    else:
        if ch=='i':
            print("Vowel")
        else:
            if ch=='o':
                print("Vowel")
            else:
                if ch=='u':
                    print("Vowel")
                else:
                    print("Consonant")

# elif
Syntax:-
if condition:
    statement
elif condition:
    statement
else:
    statement


# WAP to check an entered character is vowel or not.
# a , e , i , o , u
ch = input("Enter A Character : ") 
if ch=='a': 
    print('Vowel')
elif ch=='e':
    print("Vowel")
elif ch=='i':
    print("Vowel")
elif ch=='o':
    print("Vowel")
elif ch=='u':
    print("Vowel")
else:
    print("Consonant")


# complex condition
# WAP to check an entered character is vowel or not.
# a , e , i , o , u

ch = input("Enter A Character : ")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("Vowel")
else:
    print("Consonant")


ch = input("Enter A Character : ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

 """   



