import re
from docx import Document

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

# Merge Sort


    

