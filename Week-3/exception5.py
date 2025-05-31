def main():
    ans = 0
    try:
        print("Enter the First no :")
        no1 = int(input())

        print("Enter the second no :")
        no2 = int(input())

        ans = no1/no2
    except ZeroDivisionError as zobj:
        print("Exception occured due to second input : ", zobj)
    
    except ValueError as vobj:
        print("Invalid data type of input :", vobj)

    except Exception as eobj:
        print("Exception occured :", eobj)


    print("Division is :",ans)

if __name__ == "__main__":
    main()