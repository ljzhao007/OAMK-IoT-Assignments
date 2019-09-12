# Week 2: Python Functions

#### Write a function that converts from kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds in the main program.

```python
def ex1(kilos):
  rate = 2.2
  if isinstance(kilos, list):
    for kilo in kilos:
      print(kilo * rate, "lbs")
  else:
    print(kilos * rate, "lbs")

ex1([2, 4, 3.3, 7.2, 10,11])
```
``` python
# Output
4.4 lbs
8.8 lbs
7.26 lbs
15.840000000000002 lbs
22.0 lbs
24.200000000000003 lbs
```

#### Write a Python function to sum all the numbers in a list

```python
def ex2(numbers):
  sum = 0
  for num in numbers:
    sum += num
  return sum

print("Sum is:", ex2([1, 2, 6, 8]))
```
```python
# Output
Sum is: 17
```

#### Write a Python function to check whether a number is in a given range.

```python
def ex3(number, rangeStart, rangeStop):
  if number > rangeStart and number < rangeStop:
    print("True")
  else:
    print("False")

ex3(1, 0, 3)
ex3(3, 4, 8)
```
```python
# Output
True
False
```

#### Write a Python function that takes a number as a parameter and check the number is prime or not. Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

```python
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

ex4(71)
ex4(60)
ex4(199)
```
```python
# Output
Is Prime
Not prime
Is Prime
```

#### Write a Python function that checks whether a passed string is palindrome or not. *`Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.`*

```python
def ex5(string):
  string = list(string.replace(' ', ''))
  rev = list(reversed(string))
  if string == rev:
    print("Palindrome")
  else:
    print("Not Palindrome")

ex5("nurses run")
```
```python
# Output
['n', 'u', 'r', 's', 'e', 's', 'r', 'u', 'n']
['n', 'u', 'r', 's', 'e', 's', 'r', 'u', 'n']
Palindrome
```
