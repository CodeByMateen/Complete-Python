'''
problem 1
'''

# Task: Write a program that reads a text file and:
# Counts the total number of words
# Finds the most frequent word
# Prints the number of lines

line_count = 0
word_count = 0
frequent_word_dict = {}

with open("gamma.txt", encoding="utf-8") as file:
    for line in file:
        line_count += 1
        words = line.split()
        for word in words:
            word_count += 1
            if word.lower() in frequent_word_dict:
                frequent_word_dict[word.lower()] += 1
            else:
                frequent_word_dict[word.lower()] = 1

print(f"Number of lines: {line_count}")
print(f"Total word count: {word_count}")
print(f"Frequent word dictionary: {frequent_word_dict}")

# Find the most frequent word
most_frequent_word = ""
max_count = 0

for word, count in frequent_word_dict.items():
    if count > max_count:
        max_count = count
        most_frequent_word = word

print(f"Most frequent word: '{most_frequent_word}' (appears {max_count} times)")


