# Write a Python program to sort a list of tuples in increasing order by the last element in each--
# --tuple.

my_list = {(1, 5), (3, 2), (6, 7), (4, 3)}

def last_element(tuple):
    return tuple[-1]

sorted_list = sorted(my_list, key=last_element)
print("Sorted list of tuples in increasing order by the last element is :- ", sorted_list)
