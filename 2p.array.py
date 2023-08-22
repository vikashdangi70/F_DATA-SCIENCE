Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> x =np.array([1,2,3,4,5])
>>> print("original array: \n",x)
original array: 
 [1 2 3 4 5]
>>> print ("test if none of the elements of the array is zero: \n",np.all(x))
test if none of the elements of the array is zero: 
 True
>>> import numpy as np
>>> x =np.array([0,2,3,4,5])
>>> print("original array: \n",x)
original array: 
 [0 2 3 4 5]
>>> print("test if none of the elements of the said aray is zero:\n",np.all(x))
test if none of the elements of the said aray is zero:
 False
