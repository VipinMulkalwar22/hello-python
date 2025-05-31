def StudentInfo(**other):
    print(other)
    for i,j in other.items():
        print(i,j)

def add(*no):
    ans = 0
    for i in no:
        ans = ans + i
    return ans

print("Demonstration of Variable no of Arguments")
ret = add(10,20)
print("Addition is :",ret)

ret = add(10,20,30)
print("Addition is :",ret)

ret = add(10,20,30,40,50)
print("Addition is :",ret)


print("Demonstration of Keyword Variable number of Arguments")
StudentInfo(age=31, address="wakad", mobile=758885258, company="Marvellous")