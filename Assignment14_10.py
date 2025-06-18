class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self._department = department
        self.__salary = salary

    def Details(self):
        print("Name:",self.name)
        print("Department:",self._department)
        print("Salary:",self.__salary)


def main():
    obj = Employee("Anuja","HR",50000)
    print("public - Name:",obj.name)
    print("Protected - Department:",obj._department)
    
    obj.Details()


if __name__ =="__main__":
    main()


