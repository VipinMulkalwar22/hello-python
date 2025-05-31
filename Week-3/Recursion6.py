# Input : 4
# Output : * * * *

def Display(no):
    # for i in range(no):
    #     print("*", end=" ")

    # i = 0
    # while( i < no ):
    #     print("*", end=" ")
    #     i = i + 1    

    while(no >= 1):
        print("*", end=" ")
        no = no - 1


def main():
    Display(4)

if __name__ == "__main__":
    main()