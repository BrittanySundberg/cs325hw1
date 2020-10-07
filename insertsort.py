# Brittany Sundberg
# CS 325 Fall 2020
# HW1 problem 4


infile = open('data.txt', 'r')
all_arrays = []

with open('data.txt', 'r') as infile:
    temp_array = []
    for line in infile:
        string = line.strip()
        list = string.split()
        for i in range(0, len(list)):
            list[i] = int(list[i])
        list.pop(0)
        all_arrays.append(list)


for array in all_arrays:
    for j in range(1, len(array)):
        key = array[j]
        i = j-1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key



with open('insert.open', 'w') as outfile:
    for array in all_arrays:
        string_out = ""
        for element in array:
            string_out += str(element)
            string_out += " "
        outfile.write(string_out)