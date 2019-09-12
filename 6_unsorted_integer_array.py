# Problem 6: Unsorted Integer Array
# Max and Min in a Unsorted Array

# In this problem, we will look for smallest and largest integer from a list of
# unsorted integers. The code should run in O(n) time. Do not use Python's
# inbuilt functions to find min and max.

# Bonus Challenge: Is it possible to find the max and min in a single traversal?

def msg():
    return "Please pass a list of ints with the size of at least 1"

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) < 1:
        return msg()

    min = None
    max = None

    for i in ints:
        if type(i) is not int:
            return msg()

        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i

    return (min, max)




## Example Test Case of Ten Integers
import random

li= [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(li)

print (get_min_max(li))
# (0, 9)

li= [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(li)

print (get_min_max(li))
# (0, 99)

li= [i for i in range(-50, 50)]  # a list containing 0 - 9
random.shuffle(li)

print (get_min_max(li))
# (-50, 49)

li= [i for i in range(-99, 0)]  # a list containing 0 - 9
random.shuffle(li)

print (get_min_max(li))
# (-99, -1)

# Edge Case: just one element (should work)
print (get_min_max([1]))
# (1, 1)

# Edge Case: empty list
print (get_min_max([]))
# Please pass a list of ints with the size of at least 1

# Edge Case: non ints
print (get_min_max([1,2,3,4, "seventeen"]))
# Please pass a list of ints with the size of at least 1
