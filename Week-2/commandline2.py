import sys

def main():
    print("No of Command line arguments are : ",len(sys.argv))
    print("Data type of argv is ",type(sys.argv))
    print("First command line arguments is : ",sys.argv[0])
    print("Two command line arguments is : ",sys.argv[1])
    print("three command line arguments is : ",sys.argv[2])
    print("four command line arguments is : ",sys.argv[3])
    
if __name__ == "__main__":
    main()