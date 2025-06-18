class Student:
    school_name = "Little Angels school"


    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def DisplayDetails(self):
        print("Student name is:",self.name)
        print("Student Roll number is :",self.roll_no)
        print("School name is :",Student.school_name)

def main():

    obj = Student('Anuja',11)
    obj.DisplayDetails()

    Student.school_name = "new english school"
    print("After changing the school name")
    obj.DisplayDetails()

if __name__ =="__main__":
    main()

    
