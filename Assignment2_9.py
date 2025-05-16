def checkdigit():
    print("enter the number")
    no = input()
    count = 0
    for i in range(len(no)):
        count = count +1
    print("The number of digit is:",count)

if __name__=="__main__":
    checkdigit()



