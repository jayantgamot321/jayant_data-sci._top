number = [1,2,3,4,56,45,12,2,8,9,6,5,4,7,2,3]

unique= list()

for num in number:
    if num not in unique:
        unique= unique+[num]
        
print("unique num are : ")

for num in unique:
    print(num)

