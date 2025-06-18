class Book:
    def __init__(self,A):
        self.__price=A

    def getprice(self):
        print("book price :", self.__price)
    
    def setprice(self,NewPrice):
        if NewPrice >=0:
            self.__price = NewPrice
            print("the new price of book is:",self.__price)
        else:
            print("Invalid price ")

def main():
    print("Enter the price of book")
    p = int(input())
    obj = Book(p)
    obj.getprice()
    print("Enter new price of book:")
    NewPrice1 = int(input())
    obj.setprice(NewPrice1)

    
if __name__ =="__main__":
    main()

    