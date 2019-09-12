# Problem 1: Square Root of an Integer
# Finding the Square Root of an Integer
# Find the square root of the integer without using any Python library.
# You have to find the floor value of the square root.

# For example if the given number is 16, then the answer would be 4.

# If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

# The expected time complexity is O(log(n))

def msg():
  return "Please enter a positive integer"

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    try:
      number = int(number)
    except Exception as e:
      return msg()

    if number < 0:
      return msg()

    return _sqrt(number, 0, number)

def _sqrt(n, low, high):
  if high * high == n:
    return high

  if high - low == 1:
    return low

  mid = (low + high) // 2
  if mid * mid > n:
    return _sqrt(n, low, mid)
  elif mid * mid < n:
    return _sqrt(n, mid, high)
  else:
    return mid

print (sqrt(9))
# 3
print (sqrt(0))
# 0
print (sqrt(16))
# 4
print (sqrt(1))
# 1
print (sqrt(27))
# 5
print (sqrt(1000112))
# 1000

# Edge case: string with valid integer
print (sqrt("27"))
# 5

# Edge case: string with decimal
print (sqrt("27.2"))
# Please enter a valid integer

# Edge case: string
print (sqrt("one"))
# Please enter a valid integer

# Edge case: negative integer
print (sqrt(-42))
# Please enter a valid integer
