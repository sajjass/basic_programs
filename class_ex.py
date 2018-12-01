class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self, name):
        print "Total Employee %s" % name

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

b = Employee('sudha', '100')
b.displayCount('sudha')

c = Employee('asha', '1000')
c.displayCount('asha')
