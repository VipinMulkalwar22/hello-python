import sys

def main():
    print("No of Command line arguments are : ",len(sys.argv))
    
    print("List of command line argumnets are : ")

    for value in range(1,len(sys.argv)):
        print(sys.argv[value])
    
    
if __name__ == "__main__":
    main()