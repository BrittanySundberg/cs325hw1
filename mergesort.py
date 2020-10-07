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

for i in range(0, len(all_arrays)):
    replacement = merge_sort(all_arrays[i])
    all_arrays[i] = replacement



with open('merge.open', 'w') as outfile:
    for array in all_arrays:
        string_out = ""
        for element in array:
            string_out += str(element)
            string_out += " "
        outfile.write(string_out)