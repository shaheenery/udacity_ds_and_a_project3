# Data Structures and Algorithms

## Project 3

### Problem 1 - Square Root of an Integer

#### Complexity

Time: O(log(n))

Space: O(1)

#### Analysis

The time complexity of my algorithm is O(log(n)) where n the value of the integer being passed in. I use a recursive divide and conquer function which tests on each subsequent call, whether a number squared is higher or lower than our target.  In this way, we eliminate half of the remaining possibilities each pass.  The space complexity is constant, O(1) because regardless of the increase in n, the value of the integer being passed in, we will use the same amount of variables.

------

### Problem 2 - Search in a Rotated, Sorted Array

#### Complexity

Time: O(log(n))

Space: O(n)

#### Analysis

The time complexity of my algorithm is O(log(n)) where n is the size of the array being passed in.  Unlike a typical sorted array where you can divide and conquer based on the midpoint, I chose to divide on the pivot point, i.e. the first element in the array.  The average complexity is O(log(n)) and I believe the worst complexity, where the location of the leaves the most extreme ratio between the size of the higher and lower subsequences, the complexity will work out to O(log(n + x)) where n is the size of the array passed in and x is the difference between n and the size of an unrotated array that would result in the same number of possiblities after the first pass.  This would simplify to O(log(n)).

The space complexity is O(n) because the memory needs would increase linearly with the size of n.  I do not create any subarray as is common with a merge sort.  Instead I only store integers for the indexes of my ever narrowing search parameters

------

### Problem 3 - Rearrange Array Elements

#### Complexity

Time: O(n log(n))

Space: O(n)

#### Analysis

The time complexity for this problem is O(n log(n)) and the requirements dictate.  I decided to use a merge sort, albeit reversed (high to low).  A mergesort has that time complexity in the best, average, and worst cases.  Once a sorted list is obtained, the rest of my steps to divide the integers in to two arrays and then join them as characters before a final conversion to integers takes a comparatively inconsequencial amount of time on the order of O(n).

The space complexity is O(n) where n is the size of the input array, as is expected with a merge sort implementation.

------

### Problem 4 - Dutch National Flag

#### Complexity

Time: O(n)

Space: O(n)

#### Analysis

The time complexity for my algorithm is O(n) because there is a constant number of steps for each element in the input array, the size of the array being n.  Since we only have 3 possible values, we can use the middle value, 1, as a base case, and in-place swap the higher and lower values to their proper relative position.

The space complexity is also O(n).  Besides the input array,  I only store a constant number of integers for indexes. I perform an in-place swap in the original array instead of creating and filling a new one. I store the index of the value I am currently visiting, where the next "0" should be stored and where the next "2" should be stored, leaving the ones happily nested in the middle where they belong.

------

