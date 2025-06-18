class product:
    def __init__(self,name,price):
        self.name = name 
        self.price=price

    def __eq__(self,other_price):
        return self.price == other_price
    
def main():
    obj1 = product("pen",20)
    obj2 = product("pencil",20)

    if obj1 == obj2:
        print("Both products have same price")
    else:
        print("product have different price")

if __name__=="__main__":
    main()


    
