# Python Basics Chapter 9:
# ========================

# 1. What is List Comprehension

# With the help of list comprehension we can create list in one line.

# Create a list of squares from 1 to 10 -

# squares = [i**2 for i in range(1, 11)]
# print(squares)

# Create a list of negative numbers from 1 to 10 -

# negatives = [-i for i in range(1, 11)]
# print(negatives)

# Create a list of first character of each name from names list -
# Input : 
# names = ['Anshul', 'Manya', 'Neha', 'Nidhi']
# Output : 
# names_first_chars = ['A', 'M', 'N', 'N'] 

# names = ['Anshul', 'Manya', 'Neha', 'Nidhi']

# names_first_chars = [name[0] for name in names]
# print(names_first_chars)

# 2. Exercise - 1

# Define a function that take list of strings.
# It returns a list containing reverse of every string.

# Note: Use List Comprehension    

# 3. Exercise - 1 Solution

#de f reverse_string(l):
 #    return [s[::-1] for s in l]

# print(reverse_string(['abc', 'xyz', '123']))

# 4. List Comprehension With If Statement

# Create a list of even numbers from 1 to 10 -

# evens = [num for num in range(1, 11) if num % 2 == 0]
# print(evens)

# Create a list of odd numbers from 1 to 10 -

# odds = [num for num in range(1, 11) if num % 2 != 0]
# print(odds)

# 5. Exercise - 2

# Number to String.
# Define a function.

# Example :
# Input -> [True, False, [1, 2, 3], 1, 1.0, 3]
# Output -> ['1', '1.0', '3']

# 6. Exercise - 2 Solution

# def num_to_string(l):
#     return [str(num) for num in l if type(num) == int or type(num) == float]

# print(num_to_string([True, False, [1, 2, 3], 1, 1.0, 3]))

# 7. List Comprehension With If - Else Statements

# Create a list of negative odd numbers with double the even numbers from nums list.

# Input : nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output : neg_odd_double_even = [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]

# def neg_odd_double_even(l):
#     return [num*2 if num % 2 == 0 else -num for num in l]

# print(neg_odd_double_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 8. Nested List Comprehension

# Create a nested list of 3 lists having 3 elements 1, 2 and 3.  
# Output : nested = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# nested = [ [i for i in range(1, 4)] for j in range(3) ]
# print(nested)

# nested = []

# l = []

# for i in range(1, 4):
#     l.append(i)
    
# for j in range(3):
#     nested.append(l)

# print(nested)
