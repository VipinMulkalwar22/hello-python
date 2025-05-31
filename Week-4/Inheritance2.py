class Circle:
    PI = 3.14

    def __init__(self,A):
        self.Radius = A
        print("Inside Circle Constructor")

    def CalcualteArea(self):
        Ans = 0.0
        Ans = Circle.PI * self.Radius * self.Radius
        return Ans

class CircleX(Circle):
    def __init__(self,B):
        super().__init__(B)
    
    def CalcualteCircumFerence(self):
        Ans = 0.0
        Ans = 2 * Circle.PI * self.Radius
        return Ans

def main():
    obj = CircleX(10.5)
    Ret = obj.CalcualteArea()
    print("Area is",Ret)
    Ret = obj.CalcualteCircumFerence()
    print("CircumFerecnce is :",Ret)
    

if __name__ == "__main__":
    main()