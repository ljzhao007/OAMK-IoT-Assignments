# Week 1 - Programming with Python and Numpy

#### Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

```python
import numpy as np

def ex1():
  m = np.arange(10, 22).reshape(3,4)
  print(m)

ex1()
```
```python
# Output
[[10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]]
```

#### Write a NumPy program to test whether none of the elements of a given array is zero.

```python
def ex2(arr):
  print("Does not contain zero: ", np.count_nonzero(arr) == len(arr))

ex2([1,2,3,0,5])
```
```python
# Output
Does not contain zero:  True
```

#### Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.

```python
def ex3(arr):
  arr = np.array(arr)
  print("Size of memory occupied: %d bytes" % (arr.size * arr.itemsize))

ex3([1,7,13,105])
```
```python
# Output
Size of memory occupied: 32 bytes
```

#### Write a NumPy program to create an array of the integers from 30 to 70.

```python
def ex4(start, stop):
  arr = np.arange(start, stop + 1)
  print(arr)

ex4(30, 70)
```
```python
# Output
[30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53
 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70]
```

#### Write a NumPy program to reverse an array.

```python
def ex5(start, stop):
  arr = np.arange(start, stop + 1)
  print(np.flip(arr))

ex5(30, 40)
```
```python
# Output
[40 39 38 37 36 35 34 33 32 31 30]
```

#### Write a NumPy program to sum of all the multiples of 3 or 5 below 100.

```python
def ex6(a, b, n):
  arr = np.arange(1, n)
  mtp = arr[(arr % a == 0) | (arr % b == 0)]
  print(mtp)
  print("Sum: ", sum(mtp))

ex6(3, 5, 100)
```
```python
# Output
[ 3  5  6  9 10 12 15 18 20 21 24 25 27 30 33 35 36 39 40 42 45 48 50 51
 54 55 57 60 63 65 66 69 70 72 75 78 80 81 84 85 87 90 93 95 96 99]
Sum: 2318
```

#### Add the following two NumPy arrays and Modify a result array by calculating the square root of each element.

```python
arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]]) # [7.1]
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]]) # [7.2]
```
```python
def ex7():
  arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
  arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
  arr = np.concatenate((arrayOne, arrayTwo)).flatten()
  return np.sqrt(arr)

print(ex7())
```
```python
# Output
[2.23606798 2.44948974 3.         4.58257569 4.24264069 5.19615242
 3.87298335 5.74456265 4.89897949 2.         2.64575131 1.        ]
```

#### Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10

```python
def ex8(a, b):
  arr = np.arange(a, b, 10).reshape(5,2)
  return arr

print(ex8(100, 200))
```
```python
# Output
[[100 110]
 [120 130]
 [140 150]
 [160 170]
 [180 190]]
```
#### Following is the 2-D array. Print max from axis 0 and min from axis 1

`sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])`

```python
def ex9(arr):
  print("Axis 0: ", np.amax(arr, 0))
  print("Axis 1: ", np.amin(arr, 1))

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
ex9(sampleArray)
```
```python
# Output
Axis 0:  [82 94 73]
Axis 1:  [34 12 53]
```

#### Sort following NumPy array

`[7.1] by the second row` and `[7.2] by the second column`

```python
# Arrays were not clear, so I used the ones from exercise 7
def ex10():
  arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
  arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
  print("Sorted by 2nd row: \n", arrayOne[:, arrayOne[1,:].argsort()])
  print("Sorted by 2nd column: \n", arrayTwo[arrayTwo[:,1].argsort()])

ex10()
```
```python
# Output
Sorted by 2nd row:
 [[ 6  5  9]
 [18 21 27]]
Sorted by 2nd column:
 [[ 4  7  1]
 [15 33 24]]
```
