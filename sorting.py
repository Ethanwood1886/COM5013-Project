import re
from docx import Document
import numpy as np

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

print('Tokenised 100 Words:', token_small_data)
print('Tokenised 1000 Words:', token_large_data)

def merge(left_right)

# Merge Sort function to DIVIDE array into 2 halves

def merge_sort(array):
    if len(array) <= 1:              # if array have 1 or less elements, array is sorted
        return array
    
    middle = len(array)//2           # divide the array into 2 halves
    left_side = array[:middle]
    right_side = array[middle:]
    
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    return merge(left_side, right_side)
    

