l = [1,2,3,4,5,6,7,1.1,2.2,3.3,"python",False,0,"programing",1.1,2.2,True,1.1,20,32,50,3.3]

print(l)

l.append(100)
print(l)

l1 = l.copy()
print(l1)

l1.append(200)
print(l1)

l1.append(300)
print(l1)

l1.pop()
print(l1)

print(l.count(1))
print(l.count(0))

l2 = [1000,2000,3000]
l1.extend(l2)
print(l1)

print(l.index(1))
l1.insert(4,"tops")
print(l1)

l1.reverse()
print(l1)

for i in l:
    print(i)







