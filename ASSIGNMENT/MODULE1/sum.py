#Write a python program to sum of the first n positive integers.

#sum=(1,2,3,4,5,6,7,8)

n= int(input("enter N "))
sum=0

while n>0:
    sum= sum+n
    n= n-1

print("sum : ",sum )

if n>=0:
    print(n,"is +ve")
else:
    print(n,"is -ve")
