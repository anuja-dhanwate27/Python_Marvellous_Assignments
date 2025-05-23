def Fahrengeit(C):
    F = (C * 9/5)+32 
    return F          


def main():
    print("Temperature in celsius:")
    num = float(input())
    Ans = Fahrengeit(num)
    print("Temperature in Fahrengeit:",Ans)

if __name__ == "__main__":
    main()

