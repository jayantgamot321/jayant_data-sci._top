"""
a=50

if a>0:
    print(a, "is +ve")

n = int(input("enter N : ") )

print (type (n))


if n%2==0:
   print (n,"is even")
else:
    print (n,"is odd")



n1 = int(input("enter N1") )
n2 = int(input("enter N2") )


if n1>n2:
    print (n1,"Is greater")
else:
    print (n2,"IS greater")

n1 = int(input("enter A :"))
n2 = int(input("enter B :"))
n3 = int(input("enter C :"))

print ("A =",n1, "B = ",n2, "C = ",n3)
if n1>n3:
   if n1>n3:         

      print (n1,"is greater")
   else:    
      print (n3,"is greater")

else:
      if n2>n3:
         print (n2,"is greater")
      else:
          print (n3,"is greater")
"""
roll = int(input("enter roll no : "))
name = input("inter your name :")
p = int(input("inter physics marks :"))
c = int(input("inter chemistry marks :"))
m = int(input("inter maths marks :"))
tot = p+c+m
per = tot/3

print("*"*50)
print("roll no :",roll)
print("name :",name)
print("total :",tot)
print("percentage :",per)
print("gread is :",end="")

if per>=75:
    print("distinction")
elif  per>=60:
    print("A")
elif per>=50:
    print("B")
elif per>=40:
    print("C")
else:
    print("fail")
    

