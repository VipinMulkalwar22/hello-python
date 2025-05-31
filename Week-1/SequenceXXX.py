def CircleArea(Rad, PI = 3.14):
    Area = PI * Rad * Rad
    return Area

def main():
    print("Enter Radius of Circle : ")
    Radius = float(input())

    #result = CircleArea(Radius)    
    result = CircleArea(Radius,7.28)    

    print("Area of Circle is :", result)

if __name__ == "__main__":
    main()