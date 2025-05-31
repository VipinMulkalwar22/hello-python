def main():
    print("Enter the First no :")
    no1 = int(input())

    print("Enter the second no :")
    no2 = int(input())

    ans = 0
    try:
        ans = no1/no2
    except ZeroDivisionError as zobj:
        print(zobj)
        print("Exception occured due to second input")
    
    print("Division is :",ans)

if __name__ == "__main__":
    main()