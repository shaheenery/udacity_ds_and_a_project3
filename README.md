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

The time complexity for this problem is O(n log(n)) as the requirements dictate.  I decided to use a merge sort, albeit reversed (high to low).  A mergesort has that time complexity in the best, average, and worst cases.  Once a sorted list is obtained I  divide the integers in to two arrays and then join them as characters before a final conversion to integers.  These find steps takes a comparatively inconsequencial amount of time on the order of O(n).

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

### Problem 5 - Autocomplete with Tries

#### Complexity

Time:

| Method        |                                                              |
| :------------ | ------------------------------------------------------------ |
| `Trie#find`   | O(n) where *n* is the sum of the lengths of inserted words that match a given prefix |
| `Trie#insert` | O(n) where *n* is the length of the word to insert           |

 Space: O(n) where n is the sum of the lengths of all inserted words

#### Analysis

The trie data structure allows operations to be completed in O(n) time since the head of  all subsequences of a particular prefix are stored together.  The time it takes for a *find* will grow as the length of the input word increases.  The underlying storage for the *next letter in a sequence* is a dictionary, so each individual lookup is cheap O(1).

The space complexity of the trie implementation is O(n) because we only need to store one letter per node in the worst case, and in the best case where all but one of two words overlap e.g. (rocket, rockets), all but one of the nodes can be reused.

------

### Problem 6 - Unsorted Integer Array

#### Complexity

Time: O(n)

Space: O(n)

#### Analysis

The time and space complexity of my algorithm are both O(n) where *n* is the size of the array.  I only use two variables for storing the `min` and `max` which takes constant space regardless of the input.  Since only one traversal is needed, the time needed will grow linearly with the length of the input.

------

### Problem 7 - Request Routing in a Web Server with a Trie

#### Complexity

Time: O(n)

Space: O(n)

#### Analysis

This problem is equivalent in complexity and space to [problem 5.](#problem-5---autocomplete-with-tries) Instead of iterating through characters of a word we are iterating through segments of a URI path.  When two paths only differ by one final additional segment, all other nodes are shared between them.  When there is no overlap between two paths the space complexity is the (still linear) O(n + m).

There are additional checks for root path but that does not increase the complexity.  Splitting the path into segments by using `String#split` also has complexity of O(n) which is the same as complexity needed to do the additions and lookups.