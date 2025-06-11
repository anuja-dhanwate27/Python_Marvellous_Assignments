class Arithmatic:
    def __init__(self):
        self.value1=0
        self.value2=0
        
    def Accept(self):
        print("Enter the first value")
        self.value1=int(input())
        print("Enter the second value")
        self.value2=int(input())
        
    def Addition(self):
         return self.value1+self.value2
        
    def substraction(self):
        return self.value1-self.value2
        
    def multiplication(self):
        return self.value1*self.value2
        
    def division(self):
        return self.value1/self.value2
        
    
def main():
     obj1 = Arithmatic()
     obj1.Accept()
     print("The Addition is:",obj1.Addition())
     print("The substraction is:", obj1.substraction())
     print("The multiplication is:",obj1.multiplication())
     print("The division is:", obj1.division())

     print("------------------------------------------------------------")

     obj2 = Arithmatic()
     obj2.Accept()
     print("The Addition is:",obj2.Addition())
     print("The substraction is:", obj2.substraction())
     print("The multiplication is:",obj2.multiplication())
     print("The division is:", obj2.division())

     

     


if __name__=="__main__":
    main()

    
