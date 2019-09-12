import math as m
import string as s

def ex1(kilos):
  rate = 2.2
  if isinstance(kilos, list):
    for kilo in kilos:
      print(kilo * rate, "lbs")
  else:
    print(kilos * rate, "lbs")

# ex1([2, 4, 3.3, 7.2, 10,11])

def ex2(numbers):
  sum = 0
  for num in numbers:
    sum += num
  return sum

# print("Sum is:", ex2([1, 2, 6, 8]))

def ex3(number, rangeStart, rangeStop):
  if number > rangeStart and number < rangeStop:
    print("True")
  else:
    print("False")

# ex3(1, 0, 3)
# ex3(3, 4, 8)

def ex4(number):
  x = 2
  d = 0
  for x in range(x, int(m.sqrt(number)) + 1):
    if number % x == 0:
      d = d + 1
  if d >= 1 or number == 1:
    print("Not prime")
  else:
    print("Is Prime")

# ex4(71)
# ex4(60)
# ex4(199)

def ex5(string):
  string = list(string.replace(' ', ''))
  rev = list(reversed(string))
  if string == rev:
    print("Palindrome")
  else:
    print("Not Palindrome")

ex5("nurses run")