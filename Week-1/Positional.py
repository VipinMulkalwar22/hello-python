def CalculatePercentage(Total,Obtained):
    output = (( Obtained / Total ) * 100)
    return output

def main():
    print("Enter Total Marks")
    value1 = int(input())
    print("Enter Obatained Marks")
    value2 = int(input())

    result = CalculatePercentage(value1,value2) # Positional Argument
    print("Percentage is :",result)

if __name__ == "__main__":
    main()