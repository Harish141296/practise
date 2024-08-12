"""
Lets learn lambda functions.

Lambda functions are small anonymous functions defined using the lambda keyword. They can have any number of arguments but ONLY ONE expression(or logic). They are commonly used for short operations or as arguments to higher-order functions.
"""

# Syntax: lambda arguments: expression

def addition(a, b):
    return a + b 

print(addition(5, 3)) # output : 8

add = lambda a, b : a + b 
print(type(add))  # <class 'function'>
print(add(7, 3))  # output: 10

def even(num):
    if num %2 == 0:
        return True 
    return False 

print(even(24))  # output: True
even1 = lambda num: num % 2 == 0
print(even1(24)) # output: True


def addition(x, y, z):
    return x + y + z 


print( addition(1, 4, 3)) # output: 8 

addition = lambda x, y, z : x + y + z 
print(addition(1, 4, 3))  # output: 8


# map() - function applies a given function to all items in an input list (or any other iterable) and returns a map object (an iterator). This is particularly useful for transforming data in a list comprehensively.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def square(numbers):
    new_list = []
    for number in numbers:
        new_list.append(number ** 2 )
    return new_list

print(square(numbers))
 
print("before squaring: ", numbers)
print("after squaring using lambda: ",list(map(lambda x: x ** 2, numbers)))

numbers1 = [1,2,3]
numbers2 = [4,5,6]

# Map multiple iterables
added_numbers = map(lambda x, y : x + y, numbers1, numbers2)
print(list(added_numbers))

# map() to convert list of strings to integer.
str_numbers = ['1','2','3']

print(list(map(int, str_numbers)))

words = ['jerry','krishnamoorthi','love']
upper_word = list(map(str.upper, words))
print(upper_word)

def get_name(person):
    return person['name']

people = [
    {'name':'jerry', 'age': 27},
    {'name':'harry', 'age':28},
]

print(list(map(get_name, people)))


"""
Conclusion: Map() function is a powerful tool for applying transformations to iterale data structures. It can be used with regular functions, lambda functions, and even multiple iterables, provining a versatile approach to data processing in python. By understanding and utilizing map(), you can write more efficient and readable code.
"""
# Filter() - constructs an iterator from elements of an iterable for which a function return true. it is used to filter out items from a list ( or any other iterable) based on a condition .


def even(num):
    if num %2 == 0:
        return True 
    return False 


print(even(27))

lst = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(list(filter(even, lst))) # filters only which return True.

print(list(filter(lambda x: x > 5, lst)))

# filter with lambda and multiple condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_and_greater_than_five = list(filter(lambda x: (x>5 and x %2 == 0), numbers))
print(even_and_greater_than_five)


# Filter() to check if the age is greater than 25 in dictionaries.

people = [
    {'name': 'vishwa', 'age':1},
    {'name':'jerry', 'age' : 27},
    {'name': 'harry', 'age': 28},
    {'name':'amutha_ma', 'age': 50},
]

def age_greater_than_25(people):
    return people['age'] > 25


print(list(filter(age_greater_than_25, people)))