# Problem 1: Square Root of an Integer
# Finding the Square Root of an Integer
# Find the square root of the integer without using any Python library.
# You have to find the floor value of the square root.

# For example if the given number is 16, then the answer would be 4.

# If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

# The expected time complexity is O(log(n))

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return _sqrt(number, 0, number)

def _sqrt(n, low, high):
  if low * low == n:
    return low

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



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
