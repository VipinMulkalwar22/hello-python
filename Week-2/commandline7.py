import sys

def Addition(no1, no2):
    Ans = 0
    Ans = no1 + no2
    return Ans

def main():

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This application is used to perform the addition of number")
            return
        
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Execute the code as ")
            print("python Filename.py First_Input Second_Input")
            return
            
    if(len(sys.argv) != 3):
        print("Insufficient number of Argument")
        print("You can use --h for help and --u for usage")
        return

    print("First Numebr :",sys.argv[1])
    value1 = int(sys.argv[1])
    print("Second Numebr :",sys.argv[2])
    value2 = int(sys.argv[2])

    Result = Addition(value1, value2)
    print("Addition is :",Result)
    
if __name__ == "__main__":
    main()