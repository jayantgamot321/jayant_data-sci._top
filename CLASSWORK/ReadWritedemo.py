file = open("tops2.txt","w+")
file.write("Now this is Read/Write Demo using File")
print("Current File Cursor Position",file.tell())
file.seek(10)
print(file.read())
file.close()