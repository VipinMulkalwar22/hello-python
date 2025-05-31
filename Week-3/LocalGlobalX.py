no = 11

def fun():
    global no
    print("Inside Fun")
    x = 21
    print("Value of x is :",x) # 21
    no = no + 1
    print("Value of no :", no) # 11

def main():
    fun()

if __name__ == "__main__":
    print("Value of no before fun",no)
    main()
    print("Value of no after fun",no)
