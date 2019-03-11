# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: Three instances of Employee are created with values passed to them.
# The accessor methods are called returning the string values for each attribute.

class Employee:
    # attributes
    def __init__(self, name=None, id=None, dept=None, title=None):
        self.__name = name
        self.__ID = id
        self.__department = dept
        self.__jobtitle = title
    # methods
    def setName(self, name: str):
        """setName--
        sets the name of employee object give name argument"""
        self.__name = name

    def getName(self) -> str:
        """getName--
        returns the name of employee object"""
        return self.__name

    def setID(self, id: int):
        """setID--
        sets the ID of employee object give id argument"""
        self.__ID = id

    def getID(self) -> int:
        """getID--
        returns the ID of employee object"""
        return self.__ID

    def setDept(self, dept: str):
        """setDept--
        sets the department of employee object give dept argument"""
        self.__department = dept

    def getDept(self) -> str:
        """getDept--
        returns the department of employee object"""
        return self.__department

    def setTitle(self, title: str):
        """setTitle--
        sets the title of employee object give title argument"""
        self.__jobtitle = title

    def getTitle(self) -> str:
        """getTitle--
        returns the title of employee object"""
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
