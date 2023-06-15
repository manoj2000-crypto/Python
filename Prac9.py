# Write a python program to create an employee.txt file and store employee name and address.
a = str(input("Enter Employee Name:"))
b = str(input("Enter Employee Address:"))

file = open('employee.txt', 'w')
file.write("Employee Details")
file.write("\n")
file.write("Employee Name: " + a)
file.write("\n")
file.write("Employee Address: " + b)
file.close()
file = open("employee.txt", "r")
print(file.read())