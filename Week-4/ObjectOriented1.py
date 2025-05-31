class Arithmatic:
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Addition(self):
        result = 0
        result = self.no1 +self.no2
        return result

def main():
    print("Enter the first no")
    value1 = int(input())

    print("Enter the first no")
    value2 = int(input())

    obj = Arithmatic(value1,value2)
    ans = obj.Addition()
    print("Addition is :", ans)

if __name__ =="__main__":
    main()