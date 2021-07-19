class Employee:
    def __init__(self, name, date):
        self.name = name
        self.date = date
 
    def details(self):
        print("Employee Name:",  self.name)
        print("Employee joining date:", self.date)
 
 
emp = Employee("john", "18-02-2020")
emp.details()
