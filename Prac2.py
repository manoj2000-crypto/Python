# Write a Python program to find the number--
# --of occurrences of an element in List.

x = ['Apple', 'Apple', 'Banana', 'Peach', 'Strawberry', 'Grapes', 'Apple', 'Cherry', 'Cherry']
n = input("Enter the item you want to count :- ")
count = 0
for i in x:
    if i == n:
        count = count + 1
print("The Number of Occurrence of ", n, "in this list is: ", count)
