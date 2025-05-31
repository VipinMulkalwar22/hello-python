class Employee:
    CompanyName = "Marvellous"  # Class Variable
    
    def __init__(self,A,B,C):   # Constructor
        print("Inside Constructor")
        self.name = A           # Instance Variable
        self.salary = B         # Instance Variable
        self.city = C           # Instance Variable

    def __del__(self):          # Destructor
        print("Inside Destructor")

    def DisplayInfo(self):      # Instance Method. It can access class Variable as well.
        print("Inside Instance Method")
        print("Employee Name : "+ self.name)
        print("Employee Salary : ", self.salary)
        print("Employee City : "+ self.city)
    
    @classmethod                # Decorator
    def DisplayCompanyDetails(cls): # Class Method
        print("Inside Class Method")
        print("Company name :"+ cls.CompanyName)

    @staticmethod               # Decorator
    def DisplayCompanyPolicy(): # Static Method 
        print("Inside static mathod")
        print("All employess are 18+")
        print("Working hours are 9 to 6")
        print("Holidays: Saturday and Sunday")

def main():
    print("Class variable : "+ Employee.CompanyName)
    Employee.DisplayCompanyDetails()
    
    emp1 = Employee("Rahul",15000,"Pune") # Object Creation
    emp2 = Employee("Pooja",25000,"Mumbai") # Object Creation
    
    print("Employee Name : "+emp1.name)
    print("Employee Salary :",emp1.salary)
    print("Employee City : "+emp1.city)
    
    emp2.DisplayInfo()

    Employee.DisplayCompanyPolicy()
    
    del emp1
    del emp2

if __name__ =="__main__":
    main()