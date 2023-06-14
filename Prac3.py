# Write a Python program to count the number of lowercase characters and uppercase characters--
# --in a string.
string = input("Enter a string :- ")
lowercase_count = 0
uppercase_count = 0
for char in string:
    if char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1
print("Number of lowercase characters :- ", lowercase_count)
print("Number of uppercase characters :- ", uppercase_count)
