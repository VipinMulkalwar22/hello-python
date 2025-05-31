def CalculatePercentage(Obtained=400,Total=500):
    output = (( Obtained / Total ) * 100)
    return output

def main():
    result = CalculatePercentage(350,450) # Default Argument
    print("Percentage is :",result)

    result = CalculatePercentage(350) # Default Argument
    print("Percentage is :",result)

    result = CalculatePercentage() # Default Argument
    print("Percentage is :",result)

if __name__ == "__main__":
    main()