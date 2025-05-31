import multiprocessing
import time
import os

def SumEven(no):
    sum = 0
    print("Sum Even Process is :", os.getpid()) # 500
    print("Sum Even (Main) Parent Process is :", os.getppid()) #101
    for i in range(2,no+1,2):
        sum = sum + i
    print(sum)

def SumOdd(no):
    sum = 0
    print("Sum Odd Process is :", os.getpid()) #505
    print("Sum Odd (Main) Parent Process is :", os.getppid()) #101
    for i in range(1,no+1,2):
        sum = sum + i
    print(sum)

def main():
    
    print("Demonstration of Parallel Execution")
    print("PID of Main process is :", os.getpid()) #101
    print("PPID of CMD process is :", os.getppid()) #101

    start_time = time.time()
    P1 = multiprocessing.Process(target=SumEven,args=(900000000,))
    P2 = multiprocessing.Process(target=SumOdd,args=(900000000,))

    P1.start()
    P2.start()

    P1.join()
    P2.join()
    end_time = time.time()

    print("Time Required for execution is :", end_time - start_time)
    
    print("End of Main")

if __name__ == "__main__":
    main()  