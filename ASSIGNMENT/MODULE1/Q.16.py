"""
Counting the frequencies in a list using a dictionary in Python.
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
"""

l = [1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]

freq = {element: l.count(element) for element in l}
print(freq)
