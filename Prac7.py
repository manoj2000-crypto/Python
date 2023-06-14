# Write a Python program to find the number of characters, words, spaces and lines in a file.
n_of_words = 0
n_of_lines = 0
with open("Prac1.py", "r") as file:
    for l in file:
        n_of_words += len(l.split())
        n_of_lines += 1
print("No of words :- ", n_of_words)
print("No of lines :- ", n_of_lines)

same_file = open("Prac1.py", "r")
data = same_file.read()
no_of_char = len(data)
print('Number of characters in a file :- ', no_of_char)
