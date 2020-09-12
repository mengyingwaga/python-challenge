# import python modules
import os
import re
import csv

#locate the file path
txtpath = os.path.join("raw_data", "paragraph_1.txt")

# open csv file
with open(txtpath, 'r') as txtfile:
    # test if the file was correctly read by Python
    print(txtfile)
    
    # word count within the file
    num_words = 1
    for word in txtfile:
        words = word.split()
        num_words += len(words)
    print("word count:", num_words)

    # letter count in words, from above, words = ["xx", "xx", "xxxx", "xxx" ...]
    letter_count = 0
    for word in words:
        letter_count += len(word)
    print("letter count:", str(round(letter_count/num_words, 2)))

with open(txtpath, 'r') as txtfile:
    
    # sentence count
    paragraph_1 = txtfile.read()
    sentences = re.split("(?<=[.!?]) +", paragraph_1)
    print("sentence count:", len(sentences))

    # average sentence length by words
    print("sentence length:", str(round(num_words/len(sentences), 2)))

print("Paragraph Analysis")
print("---------------------")
print(f'Approximate Word Count: {num_words}')
print(f'Approximate Sentence Count: {len(sentences)}')
print(f'Average Letter Count: {round(letter_count/num_words, 2)}')
print(f'Average Sentence Length: {round(num_words/len(sentences), 2)}')