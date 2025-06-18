class Employeee:
    def __init__(self,A,B,C):
        self.name=A
        self.emp_id=B
        self.salary=C

    def DisplayDetails(self):
        print("Name :",self.name,"ID :",self.emp_id,"salary:",self.salary)
        

def main():
    obj = Employeee("Rohit",101,50000)
    obj.DisplayDetails()



if __name__ =="__main__":
    main()

