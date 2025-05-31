import sys

def main():
    print("No of Command line arguments are : ",len(sys.argv))
    
    print("List of command line argumnets are : ")
 
    for value in sys.argv:
        print(value)

if __name__ == "__main__":
    main()