class Demo:
    value = 110
    def __init__(self,A,B):
        self.no1=A
        self.no2=B

    def fun(self):
        print("value of no1 is:",self.no1)
        print("value of no2 is:",self.no2)

    def Gun(self):
        print("value of no1 is:",self.no1)
        print("value of no2 is:",self.no2)


def main():

    obj1=Demo(11,21)
    obj2=Demo(51,101)

    obj1.fun()
    obj2.fun()
    obj1.Gun()
    obj2.Gun()

if __name__=="__main__":
    main()