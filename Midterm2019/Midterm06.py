# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

class Employee:
    # attributes
    def __init__(self, name=None, id=None, dept=None, title=None):
        self.__name = name
        self.__ID = id
        self.__department = dept
        self.__jobtitle = title
    # methods
    def setName(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setID(self, id: int):
        self.__ID = id

    def getID(self) -> int:
        return self.__ID

    def setDept(self, dept: str):
        self.__department = dept

    def getDept(self) -> str:
        return self.__department

    def setTitle(self, title: str):
        self.__jobtitle = title

    def getTitle(self) -> str:
        return self.__jobtitle

def main():
    employee = Employee()
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rodgers", 81774, "Manufacturing", "Engineer")

    employee.setName("Susan Meyers")
    employee.setID(47899)
    employee.setDept("Accounting")
    employee.setTitle("Vice President")

    print("Hello " + employee.getName())
    print("Your ID is: " + str(employee.getID()))
    print("You are the " + employee.getTitle() + " of " + employee.getDept())

    print("Hello " + employee2.getName())
    print("Your ID is: " + str(employee2.getID()))
    print("You are the " + employee2.getTitle() + " for " + employee2.getDept())

    print("Hello " + employee3.getName())
    print("Your ID is: " + str(employee3.getID()))
    print("You are the " + employee3.getTitle() + " for " + employee3.getDept())

    return

if __name__ == "__main__":
    main()
