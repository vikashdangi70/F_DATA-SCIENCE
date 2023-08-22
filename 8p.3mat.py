Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.arange(10,22).reshape((3, 4))
>>> a = np.arange(10,22).reshape((3, 4))
>>> print("Original array:")
Original array:
>>> print(a)
[[10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]]
>>> print("Each element of the array is:")
Each element of the array is:
>>> for x in np.nditer(a):
...      print(x,end=" ")
... 
...      
10 11 12 13 14 15 16 17 18 19 20 21 
