import numpy as np

def ex1():
  m = np.arange(10, 22).reshape(3,4)
  print(m)

# ex1()

def ex2(arr):
  print("Does not contain zero: ", np.count_nonzero(arr) == len(arr))

# ex2([1,2,3,0,5])

def ex3(arr):
  arr = np.array(arr)
  print("Size of memory occupied: %d bytes" % (arr.size * arr.itemsize))

# ex3([1,7,13,105])

def ex4(start, stop):
  arr = np.arange(start, stop + 1)
  print(arr)

# ex4(30, 70)

def ex5(start, stop):
  arr = np.arange(start, stop + 1)
  print(np.flip(arr))

# ex5(30, 40)

def ex6(a, b, n):
  arr = np.arange(1, n)
  mtp = arr[(arr % a == 0) | (arr % b == 0)]
  print(mtp)
  print("Sum: ",sum(mtp))

# ex6(3, 5, 100)

def ex7():
  arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
  arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
  arr = np.concatenate((arrayOne, arrayTwo)).flatten()
  return np.sqrt(arr)

# print(ex7())

def ex8(a, b):
  arr = np.arange(a, b, 10).reshape(5,2)
  return arr

# print(ex8(100, 200))

def ex9(arr):
  print("Axis 0: ", np.amax(arr, 0))
  print("Axis 1: ", np.amin(arr, 1))

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
#ex9(sampleArray)

def ex10():
  arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
  arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
  print("Sorted by 2nd row: \n", arrayOne[:, arrayOne[1,:].argsort()])
  print("Sorted by 2nd column: \n", arrayTwo[arrayTwo[:,1].argsort()])

ex10()
