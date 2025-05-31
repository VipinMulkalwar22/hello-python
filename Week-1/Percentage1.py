def main():
    print("Enter Total Marks")
    value1 = int(input())
    print("Enter Obatained Marks")
    value2 = int(input())

    result = (( value2 / value1 ) * 100)
    
    print("Percentage is :",result)


if __name__ == "__main__":
    main()