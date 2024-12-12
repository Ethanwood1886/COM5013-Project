import re
from docx import Document
import numpy as np
import time

def read_tokenize(file_path):
    doc = Document(file_path)
    text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

    words = re.findall(r'\b\w+\b', text)    # Extract words from document

    words = [word.lower() for word in words]    # Make all words lowercase
    
    return words 

small_data = '100words.docx'
large_data = '1000words.docx'

token_small_data = read_tokenize(small_data)
token_large_data = read_tokenize(large_data)

# Merge Sort Start

def merge(left, right):

    merged = []                                 # Create empty list
    left_index = 0                              # For iteration through left
    right_index = 0                             # For iteration through right

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])                         # Append smaller element to merged list
            left_index += 1
        else:
            merged.append(right[right_index])                       # Append smaller element to merged list
            right_index += 1
    
    merged.extend(left[left_index:])                                # Append remaining elements
    merged.extend(right[right_index:])

    return merged

# Merge Sort function to DIVIDE array into 2 halves

def merge_sort(array):
    if len(array) <= 1:              # if array has 1 or less elements, array is sorted
        return array
    
    middle = len(array)//2           # divide the array into 2 halves
    left_side = array[:middle]
    right_side = array[middle:]
    
    left_side = merge_sort(left_side)           # Recursively sort left half
    right_side = merge_sort(right_side)         # Recursively sort right half

    return merge(left_side, right_side)
    
# Sorted Words: Merge Sort
start_time = time.time()
sorted_small_data = merge_sort(token_small_data)
end_time = time.time()
print('100 Words Merge Sort Time:', end_time - start_time)

start_time = time.time()
sorted_large_data = merge_sort(token_large_data)
end_time = time.time()
print('1000 Words Merge Sort Time:', end_time - start_time)

# Merge Sort End

# Bubble Sort Start

def bubble_sort(words):
    n = len(words)                                              # Stores list as n

    for i in range(n):

        for j in range(0, n-i-1):                               # Compares words and swaps if necessary

            if words[j] > words[j+1] :
                words[j], words[j+1] = words[j+1], words[j]

start_time = time.time()
bubble_sort(token_small_data)
end_time = time.time()
print('100 Words Bubble Sort Time', end_time - start_time)

start_time = time.time()
bubble_sort(token_large_data)
end_time = time.time()
print('1000 Words Bubble Sort Time', end_time - start_time)

# Bubble Sort End

# Quick Sort Start

def quick_sort(arr):
    if len(arr) <= 1:
        return arr                  # Array is sorted if there is 1 or fewer elements
    
    pivot = arr[-1]                 # Selects last item in array at pivot
    left = []
    right = []

    for num in arr[:-1]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right


start_time = time.time()
quick_sort(token_small_data)
end_time = time.time()
print('100 Words Quick Sort:', end_time - start_time)

start_time = time.time()
quick_sort(token_large_data)
end_time = time.time()
print('1000 Words Quick Sort:', end_time - start_time)