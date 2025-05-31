def main():
    print("Enter your Age")
    Age = int(input())

    if (Age < 18):
        print("You can not Vote")
    else:
        print("You can Vote")

if __name__ == "__main__":
    main()