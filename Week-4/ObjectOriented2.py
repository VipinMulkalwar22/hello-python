class Arithmatic:
    def __init__(self,A,B):
        print("Inside Constructor")
        self.no1 = A
        self.no2 = B
    
    def __del__(self):
        print("Inside Destructor")

    def Addition(self):
        result = 0
        result = self.no1 +self.no2
        return result

def main():
    obj1 = Arithmatic(10,11)
    obj2 = Arithmatic(20,21)

    ret = obj1.Addition()
    print(ret)

    ret = obj2.Addition()
    print(ret)

if __name__ =="__main__":
    main()