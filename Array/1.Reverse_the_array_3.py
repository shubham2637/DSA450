"""
Write a program to reverse an array or string
Difficulty Level : Basic
Last Updated : 08 Sep, 2020

Given an array (or string), the task is to reverse the array/string.
Examples :


Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

"""

def reverse_array(array, start, end):
    while start<end:
        array[start],array[end] = array[end], array[start]
        start += 1
        end -= 1


# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverse_array(A, 0, 5)
print("Reversed list is")
print(A)