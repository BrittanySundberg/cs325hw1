# Brittany Sundberg
# CS 325 Fall 2020
# HW1 problem 5


import timeit


setup_code_1 = '''
import random
'''

time_code_1 = '''
n = 5000
array = []
for i in range(n):
    array.append(random.randint(0,10000))
    
for j in range(1, len(array)):
    key = array[j]
    i = j-1
    while i >= 0 and array[i] > key:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = key
    '''
print("Array size n = 5,000. Time = ", timeit.timeit(setup = setup_code_1,
                    stmt=time_code_1,
                    number=1))

setup_code_2 = '''
import random
'''

time_code_2 = '''
n = 10000
array = []
for i in range(n):
    array.append(random.randint(0,10000))

for j in range(1, len(array)):
    key = array[j]
    i = j-1
    while i >= 0 and array[i] > key:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = key
    '''
print("Array size n = 10,000. Time = ", timeit.timeit(setup=setup_code_2,
                                                     stmt=time_code_2,
                                                     number=1))

setup_code_3 = '''
import random
'''

time_code_3 = '''
n = 15000
array = []
for i in range(n):
    array.append(random.randint(0,10000))

for j in range(1, len(array)):
    key = array[j]
    i = j-1
    while i >= 0 and array[i] > key:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = key
    '''
print("Array size n = 15,000. Time = ", timeit.timeit(setup=setup_code_3,
                                                     stmt=time_code_3,
                                                     number=1))

setup_code_x = '''
import random
'''

time_code_x = '''
n = 20000
array = []
for i in range(n):
    array.append(random.randint(0,10000))

for j in range(1, len(array)):
    key = array[j]
    i = j-1
    while i >= 0 and array[i] > key:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = key
    '''
print("Array size n = 20,000. Time = ", timeit.timeit(setup=setup_code_x,
                                                     stmt=time_code_x,
                                                     number=1))



setup_code_5 = '''
import random
'''

time_code_5 = '''
n = 25000
array = []
for i in range(n):
    array.append(random.randint(0,10000))

for j in range(1, len(array)):
    key = array[j]
    i = j-1
    while i >= 0 and array[i] > key:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = key
    '''
print("Array size n = 25,000. Time = ", timeit.timeit(setup=setup_code_5,
                                                     stmt=time_code_5,
                                                     number=1))


setup_code_6 = '''
import random
'''

time_code_6 = '''
n = 30000
array = []
for i in range(n):
    array.append(random.randint(0,10000))

for j in range(1, len(array)):
    key = array[j]
    i = j-1
    while i >= 0 and array[i] > key:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = key
    '''
print("Array size n = 30,000. Time = ", timeit.timeit(setup=setup_code_6,
                                                     stmt=time_code_6,
                                                     number=1))


setup_code_7 = '''
import random
'''

time_code_7 = '''
n = 35000
array = []
for i in range(n):
    array.append(random.randint(0,10000))

for j in range(1, len(array)):
    key = array[j]
    i = j-1
    while i >= 0 and array[i] > key:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = key
    '''
print("Array size n = 35,000. Time = ", timeit.timeit(setup=setup_code_7,
                                                     stmt=time_code_7,
                                                     number=1))