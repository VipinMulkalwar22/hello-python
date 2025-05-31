class Employee:
    CompanyName = "Marvellous"
    
    def __init__(self,A,B,C):
        print("Inside Constructor")
        self.name = A
        self.salary = B
        self.city = C

    def __del__(self):
        print("Inside Destructor")

def main():

    print("Class variable : "+ Employee.CompanyName)
    
    emp1 = Employee("Rahul",15000,"Pune")
    emp2 = Employee("Pooja",25000,"Mumbai")
    
    print("Employee Name : "+emp1.name)
    print("Employee Salary :",emp1.salary)
    print("Employee City : "+emp1.city)
    
if __name__ =="__main__":
    main()