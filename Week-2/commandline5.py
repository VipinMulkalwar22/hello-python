def Addition(no1, no2):
    Ans = 0
    Ans = no1 + no2
    return Ans

def main():
    value1 = int(input("Enter the first no : "))
    value2 = int(input("Enter the Second no : "))

    Result = Addition(value1, value2)
    print("Addition is :",Result)

if __name__ == "__main__":
    main()