Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> x = np.array([3, 5])
>>> y = np.array([2, 5])
>>> print("Original numbers:")
Original numbers:
>>> print(x)
[3 5]
>>> print(y)
[2 5]
>>> print("Comparison - greater")
... 
Comparison - greater
>>> print(np.greater(x, y))
[ True False]
>>> print("Comparison - greater_equal")
Comparison - greater_equal
>>> print(np.greater_equal(x, y))
[ True  True]
>>> print("Comparison - less")
Comparison - less
>>> print(np.less(x, y))
[False False]
>>> print("Comparison - less_equal")
Comparison - less_equal
>>> print(np.less_equal(x, y))
[False  True]
