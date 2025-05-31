from functools import reduce

CheckEven = lambda no : (no % 2 == 0) # Call back function as it is called by filter. We are not explictely calling that function.

Increase = lambda no : no + 1

Sum = lambda A,B : A + B

Data = [7,10,15,12,4,6,9,8,12,16]
print("Inpput Data : ", Data)
FData = list(filter(CheckEven,Data))
print("Filter Output : ", FData)
MData = list(map(Increase,FData))
print("Map Output :", MData)
RData = reduce(Sum,MData)
print("Reduce Output :", RData)