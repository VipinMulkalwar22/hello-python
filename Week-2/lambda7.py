def Power(x,y):
    Result = 1
    
    for i in range(y):
        Result = Result * x
        
    return Result

ret = Power(10,7)
print("Result is :", ret)
