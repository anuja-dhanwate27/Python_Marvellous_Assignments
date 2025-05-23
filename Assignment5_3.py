def chkAge():
    print("Enter the Age:")
    Age = int(input())
    if(Age>18):
        print("Eligible to vote")
    else:
        print("Not Eligible")

if __name__ =="__main__":
    chkAge()

    