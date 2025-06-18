class Numbers:
    def __init__(self,A):
       self.Value=A
        
    def chkprime(self):
       if self.Value>1:
           for i in range(2,self.Value+1):
               if self.Value%i==0:
                  print("The number is not prime")
                  break
       else:
           print("The number is prime")
        
    def chkperfect(self):
       if self.Value == self.SumFactors():
          print("True")
       else:
          print("False")

    def Factors(self):
       for i in range(1,self.Value):
           if self.Value%i==0:
              print("The Factor of value is:",i)

    def SumFactors(self):
        self.sum=0
        for i in range(1,self.Value):
            if self.Value%i==0:
                self.sum=self.sum+i
        print("The sum of all factors of instance variable is:",self.sum)

def main():
    print("Enter number:")
    no = int(input())
    
    obj1=Numbers(no)
    obj1.chkprime()
    obj1.chkperfect()
    obj1.Factors()
    obj1.SumFactors()


if __name__=="__main__":
    main()


                