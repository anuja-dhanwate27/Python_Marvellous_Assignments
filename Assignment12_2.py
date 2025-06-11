class circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        print("Enter the radius of circle")
        self.Radius=float(input())
        

    def calculateArea(self):
        self.Area= circle.PI*self.Radius*self.Radius
        
        

    def calculateCircumference(self):
        self.Circumference = 2*circle.PI*self.Radius
        
    

    def Display(self):
        print("The  radius of circle is:",self.Radius)
        print("The area of the circle is:",self.Area)
        print("The circumference of circle is:",self.Circumference)


def main():

    obj1 = circle()
    obj1.Accept()
    obj1.calculateArea()
    obj1.calculateCircumference()
    obj1.Display()

    print("----------------------------------------------------")

    obj2 = circle()
    obj2.Accept()
    obj2.calculateArea()
    obj2.calculateCircumference()
    obj2.Display()




if __name__=="__main__":
    main()







    
