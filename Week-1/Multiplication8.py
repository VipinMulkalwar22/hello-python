import Arithmatic 

def main():
    print("Enter the First No : ")
    no1 = int(input())

    print("Enter the Second No: ")
    no2 = int(input())

    ans = Arithmatic.Multiplication(no1,no2)

    print("Multiplication of First and Second no is ", ans)

if __name__ == "__main__":
    main()