class BookStore:
    NoOfBook = 0
    def __init__(self,A,B):
        self.Name= A
        self.Author=B
        BookStore.NoOfBook= BookStore.NoOfBook+1

    def display(self):
        print("The Name of book  is:"+self.Name)
        print("Thw name of Author is:"+self.Author)
        print("The number of books:",BookStore.NoOfBook)

def main():
    obj1 = BookStore("linux system programming","Robert Love")
    obj1.display()

    obj2=BookStore("C programming","dennis Ritchie")
    obj2.display()

if __name__=="__main__":
    main()







    

        
        








    