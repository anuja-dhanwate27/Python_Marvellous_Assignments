class Rectangle:
    def __init__(self,A,B):
        self.lenght=A
        self.width=B

    def ComputArea(self):
        Result = self.lenght * self.width
        print("Area:",Result)

    def ComputePerimeter(self):
        Result = 2*(self.lenght + self.width)
        print("Perimeter:",Result)

def main():
    obj = Rectangle(50,30)
    obj.ComputArea()
    obj.ComputePerimeter()



if __name__ =="__main__":
    main()

    
