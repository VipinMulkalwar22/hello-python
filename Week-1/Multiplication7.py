def Multiplication(Value1, Value2):
    result = Value1 * Value2
    return result

def main():
    print("Enter the First No : ")
    no1 = int(input())

    print("Enter the Second No: ")
    no2 = int(input())

    ans = Multiplication(no1,no2)

    print("Multiplication of First and Second no is ", ans)

if __name__ == "__main__":
    main()