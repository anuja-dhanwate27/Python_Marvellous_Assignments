class BankAccount:
    def __init__(self,Account_number,name,balance):
        self.Account_number = Account_number
        self.name = name
        self.balance = balance


    def deposit(self):
        print("The deposit amount is:")
        DAmount =float(input())
        Ans = self.balance+DAmount
        print("Amount diposited successfully",Ans)

    def withdraw(self):
        print("The withdraw amount is:")
        WAmount=float(input())
        if WAmount < self.balance:
            WAmount = self.balance - WAmount
            print("the withdraw amount is :",WAmount)
    
   
def main():
    print("Enter the acoount number")
    AcNum = int(input())
    print("Enter the acoount holder name")
    Acname = input()
    print("Enter the Account Balance")
    AcBalance = int(input())

    obj = BankAccount(AcNum,Acname,AcBalance)
    obj.deposit()
    obj.withdraw()
    




if __name__=="__main__":
    main()