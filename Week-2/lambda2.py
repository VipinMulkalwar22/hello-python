def chkEven(value):
    if (value % 2 == 0):
        return True
    else:
        return False
  
ret = chkEven(10)

if ret == True:
    print("Nummber is Even")
else:
    print("Numebr is Odd")