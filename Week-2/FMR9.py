from Marvellous_FMR import filterX,reduceX,mapX

CheckEven = lambda no : (no%2 == 0) # Call back function as it is called by filter. We are not explictely calling that function.
Increase = lambda no : no+1
Sum = lambda A,B : A+B

def main():

    Data = []
    print("Enter number of Element : ")
    size = int(input())

    print("Please enter numberic Values : ")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input Data : ", Data)
    FData = list(filterX(CheckEven,Data))
    print("Filter Output : ", FData)
    MData = list(mapX(Increase,FData))
    print("Map Output :", MData)
    RData = reduceX(Sum,MData)
    print("Reduce Output :", RData)

if __name__ == "__main__":
    main()