# Rearrange Array Elements

# Rearrange Array Elements so as to form two numbers such that their sum is
# maximum. Return these two numbers. You can assume that all array elements
# are in the range [0, 9]. The number of digits in both the numbers cannot
# differ by more than 1. You're not allowed to use any sorting function that
# Python provides and the expected time complexity is O(nlog(n)).

# for e.g. [1, 2, 3, 4, 5]

# The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

def msg():
    return "Please provide a list of integers with at least two elements"

def reverse_mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    l_sorted = reverse_mergesort(left)
    r_sorted = reverse_mergesort(right)

    return high2low_merge(l_sorted, r_sorted)

def high2low_merge(left, right):
    l_index = 0
    r_index = 0
    merged = []

    while l_index < len(left) and r_index < len(right):
        if left[l_index] >= right[r_index]:
            merged.append(left[l_index])
            l_index += 1
        else:
            merged.append(right[r_index])
            r_index += 1

    merged += left[l_index:]
    merged += right[r_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if ((type(input_list) is not list) or
           (len(input_list) < 2)):
        return msg()

    for elem in input_list:
        if type(elem) is not int:
            return msg()

    ordered = reverse_mergesort(input_list)

    one = []
    two = []

    for i in range(len(ordered)):
        if i % 2 == 0:
            one.append(str(ordered[i]))
        else:
            two.append(str(ordered[i]))

    return (int("".join(one)), int("".join(two)))

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Edge case: only two elements (should work)
print (rearrange_digits([1,2]))
# (2, 1)

# Edge case: only one element (error msg)
print (rearrange_digits([1]))
# Please provide a list of integers with at least two elements

# Edge case: empty list
print (rearrange_digits([]))
# Please provide a list of integers with at least two elements

# Edge case: non-integer list elements
print (rearrange_digits(["1", 2,3,4]))
# Please provide a list of integers with at least two elements
