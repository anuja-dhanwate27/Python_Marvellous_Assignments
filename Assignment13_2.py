class BankAccount:
    ROI=10.5
    def __init__(self):
        print("The Name is:")
        A = input()
        self.Name=A
        print("The Amount is:")
        B=float(input())
        self.Amount=B

    def deposit(self):
        print("The deposit amount is:")
        DAmount =float(input())
        Ans = self.Amount+DAmount
        print("Amount diposited successfully",Ans)
        
    def Withdraw(self):
        print("The withdraw amount is:")
        WAmount=float(input())
        if WAmount < self.Amount:
            WAmount = self.Amount - WAmount
            print("the withdraw amount is :",WAmount)

            

    def calculateInterest(self):
        interest = (self.Amount*BankAccount.ROI)/100
        print("interest on your amount is :",interest)

    def Display(self):
        print("name:"+self.Name)
        print("Amount:",self.Amount)
def main():
    obj1=BankAccount()
    #obj1.Display()
    obj1.deposit()
    obj1.Withdraw()
    obj1.calculateInterest()
    obj1.Display()


if __name__=="__main__":
    main()










