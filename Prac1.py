# Write a Python Program to print Fibonacci series of 'n' terms.

num = int(input("Enter upper range :- "))
a = 0
b = 1
print(f"Fibonacci series upto {num} :- ", a, b, end=" ")
for i in range(3, num+1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
