# Write a Python program to define a class Employee having members id, name, department, salary. Create a subclass -
# called manager with a member bonus. Define methods to accept and display in both classes. Create n objects of the -
# manager class and display the details of the manager having the maximum total salary (salary+bonus)

class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print("ID : ", self.id)
        print("Name : ", self.name)
        print("Department : ", self.department)
        print("Salary : ", self.salary)


class Manager(Employee):
    def __init__(self, id, name, department, salary, bonus):
        super().__init__(id, name, department, salary)
        self.bonus = bonus

    def display_details(self):
        super().display_details()
        print("Bonus : ", self.bonus)


def get_max_salary_manager(managers):
    max_salary = -1
    max_salary_manager = None

    for manager in managers:
        total_salary = manager.salary + manager.bonus
        if total_salary > max_salary:
            max_salary = total_salary
            max_salary_manager = manager

    if max_salary_manager is not None:
        print("\nManager with the maximum total salary : ")
        max_salary_manager.display_details()


n = int(input("Enter the number of managers: "))

managers = []
for i in range(n):
    print(f"\nEnter details of manager {i + 1}:")
    id = int(input("ID: "))
    name = input("Name: ")
    department = input("Department : ")
    salary = float(input("Salary : "))
    bonus = float(input("Bonus : "))

    manager = Manager(id, name, department, salary, bonus)
    managers.append(manager)
print("\nDisplaying details of all managers : ")
for manager in managers:
    manager.display_details()

get_max_salary_manager(managers)
