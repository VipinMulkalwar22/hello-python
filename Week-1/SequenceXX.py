PI = 3.14

def CircleArea(Rad):
    Area = PI * Rad * Rad
    return Area

def main():
    print("Enter Radius of Circle : ")
    Radius = float(input())

    result = CircleArea(Rad=Radius)    

    print("Area of Circle is :", result)

if __name__ == "__main__":
    main()