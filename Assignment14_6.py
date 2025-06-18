class calculator:
    def __init__(self,Num1,Num2):
        self.num1=Num1
        self.num2=Num2

    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1/self.num2
    
def main():

    print("enter the first number")
    Num1 = int(input())
    print("enter the second number")
    Num2 = int(input())

    obj = calculator(Num1,Num2)


    print("choose operatrion: +,-,*,/")
    print("enter your choice:")
    operation = input()

    if operation == "+":
        print("Result :",obj.add())
    elif operation == "-":
        print("Result:",obj.subtract())
    elif operation == "*":
        print("Result:",obj.multiply())
    elif operation == "/":
        print("Result:",obj.divide())
    else:
        print("incorrect operation")


if __name__ == "__main__":
    main()
    

    
    
