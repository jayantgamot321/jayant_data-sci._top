"""
Write a Python program to find the highest 3 values in a dictionary.
"""
from heapq import nlargest
d = {'a':100,'b':200,'c':300,'d':400,'e':500}


three_largest = nlargest(3,d,key=d.get)

print(three_largest)
