Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> X = np.array([1, 7, 13, 105])
>>> print("Original array:")
Original array:
>>> print(X)
[  1   7  13 105]
>>> print("Size of the memory occupied by the said array:")
Size of the memory occupied by the said array:
>>> print("%d bytes" % (X.size * X.itemsize))
16 bytes
