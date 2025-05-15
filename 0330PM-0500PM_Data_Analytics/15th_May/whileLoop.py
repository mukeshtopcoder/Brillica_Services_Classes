# WHILE LOOP
"""
Syntax:-

initialization
while condition:
    statements
    incr/decr

#Example
a = 1
while a<=50:
    print("Hello")
    a = a+1


a = 1
while a<=10:
    print(a)
    a=a+1

# break , continue , pass

a = 1
while a<=10:
    a=a+1
    if a == 4:
        break
    print(a)

a = 1
while a<=10:
    a=a+1
    if a == 4:
        continue
    print(a)

a = 1
while a<=10:
    a=a+1
    if a == 4:
        pass
    print(a)


a = 1
while a<=5:
    print(a)
    a=a+1
    if a==3:
        continue
else:
    print(0)



# WAP to print table of a number using while loop.

num = int(input("Enter A Number : "))
a = 1
while a<=10:
    print(a*num)
    a=a+1



# WAP to add all the numbers from 1 to 100.

summ = 0
a = 1
while a<=100:
    summ = summ+a
    a = a+1

print(summ)

OR

n = 100
print( n*(n+1)/2 )


# WAP to add all even numbers only from 1 to 100.

summ = 0
a = 1
while a<=100:
    if a%2==0:
        summ = summ+a
    a = a+1

print(summ)



# WAP to calculate factorial of a number.
# 5! =>  5*4*3*2*1 -> 120

num = 7
fact = 1
a = 1
while a<=num:
    fact = fact*a
    a = a+1
print(fact)



# WAP to find all factors of a number.
# HINT :- 12 -> 1,2,3,4,6,12

num = 12
a = 1
while a<=num:
    if num%a == 0:
        print(a)
    a=a+1

"""






