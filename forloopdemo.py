"""
for i in range(10):
    print(i)

for i in range(1,10):
    print(i)
    

n = int(input("enter N = "))

for i in range(1,n+1):
    print(i)


for i in range(1,15,2):
    print(i)


for i in range(15,0,-1):
    print(i)


n = int(input("enter N : "))
sum=0

while n>0:
    sum=sum+n
    n = n-1
print("sum = ",sum)    


n = int(input("enter N "))
sum=0
for i in range(1,n+1):
    sum = sum+i
print("sum = ",sum)    
"""
n = int(input("enter N "))
evensum=0
oddsum=0

for i in range(1,n+1):
    if i%2==0:
        evensum = evensum+i
    else:
        oddsum = oddsum+i
print("evensum = ",evensum)
print("oddsum = ",oddsum)



























