"""
    Data Dictionary : It is a type of Collection

                     : It works with key/value pair pattern.
                     : No Indexing in Data Dictionary.
                     : It starts with key/value.
                     : Every Key is Unique.

                    Syntax:
                    
                     : It is use with {}

                     d = {key:'value',key:'value'.........}
                     

"""

d = {1:'Monika',2:'Jayant',3:'Urvashi',4:'Mohit',5:'Ankit'}

print(d)

print(d[4])

d1 = d.copy()
print(d1)

print(d.get(5))

print(d.keys())
print(d.values())
print(d.items())
d.pop(2)
print(d)
print(d.pop(4))
print(d)
print(d.popitem())
print(d)

d[1]='lalita'
print(d)
d[2]='jayant'
print(d)
d[2]='jay'
print(d)
d[4]='Ankit'
d[5]='Mohit'
print(d)
d2 = {'a':1,'b':2,'c':3}
print(d2)
d.update(d2)
print(d)

for i,k in d.items():
    print(i,":",k)

    



























