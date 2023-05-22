# Lab 11

print("Task-1")
print()
class Shape:
    def __init__(self,sides):
        self.sides = sides

    def area(self):
        pass

class triangle(Shape):
    def __init__(self,width,height):
        super().__init__(3)
        self.width = width
        self.height = height

    def Comute_area(self):
        return 0.5 * self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        super().__init__(0)
        self.radius = radius

    def Comutee_area(self):
        return 3.142 * self.radius**2

def main():
    shape1 = triangle(2,5)
    shape2 = Circle(6)

    print("area of triangle is: ",shape1.Comute_area(),"cm")
    print("area of circle is: ", shape2.Comutee_area(),"cm")

main()

print()
print("Task-2")
print()

class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary


    def display(self):
        print("Name: ", self.name,"ID: ", self.id,"Salary: ", self.salary)
       

class BuildingManager(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id,salary)

class Procurementmanager(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id,salary)

class logisticsmanager(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id,salary)

def main():
    lst = []
    lst.append(BuildingManager("Mohib",101,10000))
    lst.append(Procurementmanager("Asad",105,12000))
    lst.append(logisticsmanager("Musa",110,15000))
    for i in lst:
        i.display()
main()


