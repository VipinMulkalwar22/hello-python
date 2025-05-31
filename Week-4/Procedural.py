def Addition(A,B):
    result = 0
    result = A+B 
    return result

def main():
    print("Enter the first no")
    no1 = int(input())

    print("Enter the first no")
    no2 = int(input())

    ans = Addition(no1,no2)
    print("Addition is :", ans)

if __name__ =="__main__":
    main()