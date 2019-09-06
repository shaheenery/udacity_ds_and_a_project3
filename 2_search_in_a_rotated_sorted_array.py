# Search in a Rotated Sorted Array
# You are given a sorted array which is rotated at some random pivot point.

# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

# You are given a target value to search. If found in the array return its
# index, otherwise return -1.

# You can assume there are no duplicates in the array and your algorithm's
 # runtime complexity must be in the order of O(log n).

# Example:

# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return _ra_search(input_list, number, 0, len(input_list) - 1)

def _ra_search(arr, num, low, high):
    if low > high:
        return -1

    if arr[low] == num:
        return low

    if arr[high] == num:
        return high

    mid = (low + high) // 2

    if arr[mid] == num:
        return mid

    if (num > arr[low]):
        return _ra_search(arr, num, low + 1, mid - 1)
    else:
        return _ra_search(arr, num, mid + 1, high - 1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    correct_solution = linear_search(input_list, number)
    my_solution = rotated_array_search(input_list, number)
    if correct_solution == my_solution:
        print("Pass")
    else:
        print("Fail,\nGot:\t{my_solution}\nExpected:\t{correct_solution}")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
