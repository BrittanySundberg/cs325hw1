# Brittany Sundberg
# CS 325 Fall 2020
# HW1 problem 5


import timeit

setup_code_1 = '''
import random
'''
time_code_1 = '''
def Merge(array_a, array_b):
    index_a = 0
    index_b = 0
    sorted_array = []
    while index_a < len(array_a) and index_b < len(array_b):
        if array_a[index_a] < array_b[index_b]:  #if the current index at a is smaller, add it to the sorted array, then increase a's index
            sorted_array.append(array_a[index_a])
            index_a += 1
        else:    #if the current index at b is smaller, add it to to the sorted array, then increase b's index.
            sorted_array.append(array_b[index_b])
            index_b += 1
    #after one is empty, put the rest of the other one in the sorted array
    sorted_array += array_a[index_a:]
    sorted_array += array_b[index_b:]
    return sorted_array

def merge_sort(array_1):
    if len(array_1) == 1:
        return array_1
    else:
        array_first_half = merge_sort(array_1[:(len(array_1)//2)])
        array_second_half = merge_sort(array_1[(len(array_1)//2):])
        return Merge(array_first_half, array_second_half)

n_1 = 5000
array_1 = []

for i in range(n_1):
    array_1.append(random.randint(0,10000))

new_array_1 = merge_sort(array_1)
'''
print("Array size n = 5,000. Time = ", timeit.timeit(setup = setup_code_1,
                    stmt=time_code_1,
                    number=1))


setup_code_2 = '''
import random
'''
time_code_2 = '''
def Merge(array_a, array_b):
    index_a = 0
    index_b = 0
    sorted_array = []
    while index_a < len(array_a) and index_b < len(array_b):
        if array_a[index_a] < array_b[index_b]:  #if the current index at a is smaller, add it to the sorted array, then increase a's index
            sorted_array.append(array_a[index_a])
            index_a += 1
        else:    #if the current index at b is smaller, add it to to the sorted array, then increase b's index.
            sorted_array.append(array_b[index_b])
            index_b += 1
    #after one is empty, put the rest of the other one in the sorted array
    sorted_array += array_a[index_a:]
    sorted_array += array_b[index_b:]
    return sorted_array

def merge_sort(array_1):
    if len(array_1) == 1:
        return array_1
    else:
        array_first_half = merge_sort(array_1[:(len(array_1)//2)])
        array_second_half = merge_sort(array_1[(len(array_1)//2):])
        return Merge(array_first_half, array_second_half)

n_2 = 10000

array_2 = []


for i in range(n_2):
    array_2.append(random.randint(0,10000))

new_array_2 = merge_sort(array_2)
'''
print("Array size n = 10,000. Time = ", timeit.timeit(setup = setup_code_2,
                    stmt=time_code_2,
                    number=1))


setup_code_3 = '''
import random
'''
time_code_3 = '''
def Merge(array_a, array_b):
    index_a = 0
    index_b = 0
    sorted_array = []
    while index_a < len(array_a) and index_b < len(array_b):
        if array_a[index_a] < array_b[index_b]:  #if the current index at a is smaller, add it to the sorted array, then increase a's index
            sorted_array.append(array_a[index_a])
            index_a += 1
        else:    #if the current index at b is smaller, add it to to the sorted array, then increase b's index.
            sorted_array.append(array_b[index_b])
            index_b += 1
    #after one is empty, put the rest of the other one in the sorted array
    sorted_array += array_a[index_a:]
    sorted_array += array_b[index_b:]
    return sorted_array

def merge_sort(array_1):
    if len(array_1) == 1:
        return array_1
    else:
        array_first_half = merge_sort(array_1[:(len(array_1)//2)])
        array_second_half = merge_sort(array_1[(len(array_1)//2):])
        return Merge(array_first_half, array_second_half)

n_3 = 15000

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = merge_sort(array_3)
'''
print("Array size n = 15,000. Time = ", timeit.timeit(setup = setup_code_3,
                    stmt=time_code_3,
                    number=1))



setup_code_4 = '''
import random
'''
time_code_4 = '''
def Merge(array_a, array_b):
    index_a = 0
    index_b = 0
    sorted_array = []
    while index_a < len(array_a) and index_b < len(array_b):
        if array_a[index_a] < array_b[index_b]:  #if the current index at a is smaller, add it to the sorted array, then increase a's index
            sorted_array.append(array_a[index_a])
            index_a += 1
        else:    #if the current index at b is smaller, add it to to the sorted array, then increase b's index.
            sorted_array.append(array_b[index_b])
            index_b += 1
    #after one is empty, put the rest of the other one in the sorted array
    sorted_array += array_a[index_a:]
    sorted_array += array_b[index_b:]
    return sorted_array

def merge_sort(array_1):
    if len(array_1) == 1:
        return array_1
    else:
        array_first_half = merge_sort(array_1[:(len(array_1)//2)])
        array_second_half = merge_sort(array_1[(len(array_1)//2):])
        return Merge(array_first_half, array_second_half)

n_3 = 20000

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = merge_sort(array_3)
'''
print("Array size n = 20,000. Time = ", timeit.timeit(setup=setup_code_4,
                                                     stmt=time_code_4,
                                                     number=1))



setup_code_5 = '''
import random
'''
time_code_5 = '''
def Merge(array_a, array_b):
    index_a = 0
    index_b = 0
    sorted_array = []
    while index_a < len(array_a) and index_b < len(array_b):
        if array_a[index_a] < array_b[index_b]:  #if the current index at a is smaller, add it to the sorted array, then increase a's index
            sorted_array.append(array_a[index_a])
            index_a += 1
        else:    #if the current index at b is smaller, add it to to the sorted array, then increase b's index.
            sorted_array.append(array_b[index_b])
            index_b += 1
    #after one is empty, put the rest of the other one in the sorted array
    sorted_array += array_a[index_a:]
    sorted_array += array_b[index_b:]
    return sorted_array

def merge_sort(array_1):
    if len(array_1) == 1:
        return array_1
    else:
        array_first_half = merge_sort(array_1[:(len(array_1)//2)])
        array_second_half = merge_sort(array_1[(len(array_1)//2):])
        return Merge(array_first_half, array_second_half)

n_3 = 25000

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = merge_sort(array_3)
'''
print("Array size n = 25,000. Time = ", timeit.timeit(setup=setup_code_5,
                                                     stmt=time_code_5,
                                                     number=1))


setup_code_6 = '''
import random
'''
time_code_6 = '''
def Merge(array_a, array_b):
    index_a = 0
    index_b = 0
    sorted_array = []
    while index_a < len(array_a) and index_b < len(array_b):
        if array_a[index_a] < array_b[index_b]:  #if the current index at a is smaller, add it to the sorted array, then increase a's index
            sorted_array.append(array_a[index_a])
            index_a += 1
        else:    #if the current index at b is smaller, add it to to the sorted array, then increase b's index.
            sorted_array.append(array_b[index_b])
            index_b += 1
    #after one is empty, put the rest of the other one in the sorted array
    sorted_array += array_a[index_a:]
    sorted_array += array_b[index_b:]
    return sorted_array

def merge_sort(array_1):
    if len(array_1) == 1:
        return array_1
    else:
        array_first_half = merge_sort(array_1[:(len(array_1)//2)])
        array_second_half = merge_sort(array_1[(len(array_1)//2):])
        return Merge(array_first_half, array_second_half)

n_3 = 30000

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = merge_sort(array_3)
'''
print("Array size n = 30,000. Time = ", timeit.timeit(setup=setup_code_6,
                                                     stmt=time_code_6,
                                                     number=1))



setup_code_7 = '''
import random
'''
time_code_7 = '''
def Merge(array_a, array_b):
    index_a = 0
    index_b = 0
    sorted_array = []
    while index_a < len(array_a) and index_b < len(array_b):
        if array_a[index_a] < array_b[index_b]:  #if the current index at a is smaller, add it to the sorted array, then increase a's index
            sorted_array.append(array_a[index_a])
            index_a += 1
        else:    #if the current index at b is smaller, add it to to the sorted array, then increase b's index.
            sorted_array.append(array_b[index_b])
            index_b += 1
    #after one is empty, put the rest of the other one in the sorted array
    sorted_array += array_a[index_a:]
    sorted_array += array_b[index_b:]
    return sorted_array

def merge_sort(array_1):
    if len(array_1) == 1:
        return array_1
    else:
        array_first_half = merge_sort(array_1[:(len(array_1)//2)])
        array_second_half = merge_sort(array_1[(len(array_1)//2):])
        return Merge(array_first_half, array_second_half)

n_3 = 35000

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = merge_sort(array_3)
'''
print("Array size n = 35,000. Time = ", timeit.timeit(setup=setup_code_7,
                                                     stmt=time_code_7,
                                                     number=1))