"""
n=98
print("N = ",n)
print(type(n))

a = 8976456561
b = 3546787454

print("A = ",a,"B = ",b)

print("addition = ",(a+b))
print("subtraction = ",(a-b))
print("multiplication = ",(a*b))
print("division = ",(a/b))

a = -20

if a<0:
    print(a,"is -ve")
    
n = int(input("enter N : "))

if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")

n1 = int(input("enter N1 "))
n2 = int(input("enter N2 "))

if n1>n2:
    print(n1,"is greater")
else:
    print(n2,"is greater")


n1 = int(input("enter A : "))
n2 = int(input("enter B : "))
n3 = int(input("enter C : "))

print("A = ",n1,"B = ",n2,"C = ",n3)

if n1>n2:
    if n1>n3:
        print(n1,"is greater")
    else:
        print(n3,"is greater")
else:
    if n2>n3:
        print(n2,"is greater")
    else:
        print(n3,"is greater")
"""

roll = int(input("enter roll no : "))
name = input("enter your name : ")
p = int(input("enter physics marks : "))
c = int(input("enter cheamistry marks : "))
m = int(input("enter math marks : "))
tot = p+c+m
per = tot/3

print("roll no ",roll)
print("your name ",name)
print("total ",tot)
print("percentage ",per)
print("gread is ",end="")

if per>=75:
    print("distinction")
elif per>=65:
    print("A")
elif per>=55:
    print("B")
elif per>=45:
    print("C")
else:
    print("fail")
    


















    
