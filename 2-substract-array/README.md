# Substract an array from another array

## Task

Your goal is to implement a difference function in Python 3 that subtracts a list from another and returns the result. It should remove all values from list "a", which are present in list "b" keeping their order.
Eg.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]
After implementing the array_diff() function, be sure to create a unit test using the below test values to make sure it works properly:
([1,2], [1]) == [2]([1,2,2], [1]) == [2,2]([1,2,2], [2]) == [1]([1,2,2], []) == [1,2,2]([], [1,2]) == []([1,2,3], [1, 2]) == [3]

## Solution

```bash
➜  2-substract-array git:(main) ✗ python3 ./difference.py                                                         
Tests passed
```
