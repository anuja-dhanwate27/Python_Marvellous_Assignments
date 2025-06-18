class person:
    def __init__(self,name ,age):
        self.name=name
        self.age=age

    def DisplayP(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Teacher(person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject=subject
        self.salary=salary

    def DisplayT(self):
        self.DisplayP()
        print("Subject:",self.subject)
        print("Salary:",self.salary)

def main():
    print("Enter the name:")
    name = input()
    print("Enter the age")
    Age = int(input())
    print("Enter the subject")
    sub = input()
    print("Enter the salary")
    salary = float(input())

    obj = Teacher(name,Age,sub,salary)
    print("print the teachers details")
    obj.DisplayT()




if __name__=="__main__":
    main()


